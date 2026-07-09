---
title: pnpm patch
date: 2026-06-17 16:38:57
tags:
  - js
---

# 使用 `pnpm patch` 修改 `antd@6.4.4` 的步骤总结

## 背景

Ant Design 的 GitHub 源码是 TypeScript / TSX，但 npm 发布包里实际被项目消费的是编译后的 JavaScript 产物。

因此通过 `pnpm patch` 修改依赖时，改的是 npm 包中的发布内容，例如：

```text
es/tag/index.js
es/tag/style/index.js
lib/tag/index.js
lib/tag/style/index.js
```

而不是 AntD 仓库源码里的：

```text
components/tag/index.tsx
components/tag/style/index.ts
```

## 1. 创建 patch 工作目录

```bash
pnpm patch antd@6.4.4
```

pnpm 会输出一个临时目录，例如：

```text
node_modules/.pnpm_patches/antd@6.4.4
```

之后所有修改都在这个目录里进行。

## 2. 修改 AntD Tag 的样式文件

Tag 的样式主要在：

```text
node_modules/.pnpm_patches/antd@6.4.4/es/tag/style/index.js
node_modules/.pnpm_patches/antd@6.4.4/lib/tag/style/index.js
```

可以在 `genBaseStyle` 中修改 Tag 的基础样式，例如：

```js
backgroundColor: '#ff00aa',
backgroundImage: 'linear-gradient(135deg, #ff007f 0%, #ffea00 45%, #00f0ff 100%)',
border: `${unit(3)} ${token.lineType} #ff00ff`,
borderRadius: 999,
color: '#fff',
fontWeight: 900,
letterSpacing: 1,
textTransform: 'uppercase',
boxShadow: '0 0 0 2px #fff, 0 0 16px #ff00ff, 0 0 28px #00f0ff',
textShadow: '0 1px 0 #000, 0 0 8px #000',
transform: 'rotate(-2deg) scale(1.08)',
```

注意：

- `es/` 是 ESM 产物，Vite 通常会用它。
- `lib/` 是 CommonJS 产物，也建议一起改，避免不同构建环境不一致。

## 3. 如果样式没显示，需要改 Tag 组件的 inline style

AntD 的 Tag 在使用 `color`、preset/status color 等场景下，可能会生成 `customTagStyle`，并通过 inline style 覆盖 CSS-in-JS 里的基础样式。

所以除了改 `style/index.js`，还可以直接改：

```text
node_modules/.pnpm_patches/antd@6.4.4/es/tag/index.js
node_modules/.pnpm_patches/antd@6.4.4/lib/tag/index.js
```

在 `tagStyle` 的 `React.useMemo` 中追加样式覆盖，例如：

```js
nextTagStyle = {
  ...nextTagStyle,
  backgroundColor: '#ff00aa',
  backgroundImage: 'linear-gradient(135deg, #ff007f 0%, #ffea00 45%, #00f0ff 100%)',
  border: '3px solid #ff00ff',
  borderRadius: 999,
  color: '#fff',
  fontWeight: 900,
  letterSpacing: 1,
  textTransform: 'uppercase',
  boxShadow: '0 0 0 2px #fff, 0 0 16px #ff00ff, 0 0 28px #00f0ff',
  textShadow: '0 1px 0 #000, 0 0 8px #000',
  transform: 'rotate(-2deg) scale(1.08)',
};
```

这样可以保证最终渲染到 DOM 上的 inline style 也带有 patch 后的样式。

## 4. 提交 patch

修改完成后执行：

```bash
pnpm patch-commit node_modules/.pnpm_patches/antd@6.4.4
```

执行后会生成 patch 文件，例如：

```text
patches/antd@6.4.4.patch
```

同时 pnpm 会更新：

```text
pnpm-workspace.yaml
pnpm-lock.yaml
```

其中 `pnpm-workspace.yaml` 中会出现：

```yaml
patchedDependencies:
  antd@6.4.4: patches/antd@6.4.4.patch
```

`pnpm-lock.yaml` 中也会记录 patch hash。

## 5. 应用 patch

通常执行：

```bash
pnpm install
```

如果想尽量避免联网，可以执行：

```bash
pnpm install --offline
```

如果 pnpm 认为依赖已经是最新，但实际链接没有刷新，可以尝试：

```bash
pnpm install --force
```

## 6. 确认当前项目使用的是 patched antd

可以检查 workspace 下的 `antd` 链接是否指向带 `patch_hash` 的目录。

例如：

```bash
pnpm --filter @gis-mesh/examples why antd
```

或查看实际路径：

```text
examples/frontend/node_modules/antd
```

它应该指向类似：

```text
node_modules/.pnpm/antd@6.4.4_patch_hash=xxxx/node_modules/antd
```

如果还是指向没有 `patch_hash` 的目录，说明 patch 没有被当前项目实际用上。

## 7. 清理 Vite 依赖预构建缓存

Vite 会把依赖预构建到：

```text
examples/frontend/node_modules/.vite/deps/
```

即使 pnpm patch 已经成功，正在运行的 dev server 也可能继续使用旧的预构建文件。

所以需要停掉 dev server，然后删除 Vite 缓存。

macOS / Linux：

```bash
rm -rf examples/frontend/node_modules/.vite
```

Windows PowerShell：

```powershell
Remove-Item -Recurse -Force examples/frontend/node_modules/.vite
```

然后重新启动：

```bash
pnpm dev
```

## 8. 验证 patch 是否进入 Vite 预构建文件

可以搜索 Vite 预构建后的 `antd.js`：

```bash
grep -R "ff00aa" examples/frontend/node_modules/.vite/deps/antd.js
```

如果能搜到类似：

```js
backgroundColor: "#ff00aa"
```

说明 Vite 已经吃到了 patched antd。

也可以搜索 patch hash：

```bash
grep -R "patch_hash" examples/frontend/node_modules/.vite/deps/antd.js
```

如果路径中包含：

```text
antd@6.4.4_patch_hash=xxxx
```

说明 Vite 当前预构建使用的是 patched 版本。

## 9. 构建验证

可以执行：

```bash
pnpm --filter @gis-mesh/examples build
```

如果构建成功，说明 patch 至少没有破坏生产构建。

## 10. 常见问题

### 1. 为什么 AntD 源码是 TS，但 patch 里是 JS？

因为 `pnpm patch` 修改的是 npm 发布包，而不是 AntD GitHub 仓库源码。

npm 包中实际被项目消费的是编译后的 JS：

```text
es/
lib/
```

TS 类型则通过 `.d.ts` 提供。

### 2. 为什么 patch 文件生成了，但页面没变化？

常见原因：

1. Vite dev server 没重启。
2. `examples/frontend/node_modules/.vite` 里还有旧的预构建缓存。
3. 当前项目的 `antd` 没有指向带 `patch_hash` 的目录。
4. 只改了 `tag/style/index.js`，但 Tag 的 inline style 覆盖了 CSS-in-JS 样式。
5. 页面中看到的 Tag 不是来自当前 patched 的 `antd@6.4.4`。

### 3. 为什么要同时改 `es` 和 `lib`？

因为不同工具链可能使用不同入口：

- Vite / ESM 环境通常使用 `es/`
- CommonJS / Node / 某些测试环境可能使用 `lib/`

为了 patch 行为一致，建议两边都改。

## 最终需要提交的文件

通常需要提交：

```text
patches/antd@6.4.4.patch
pnpm-workspace.yaml
pnpm-lock.yaml
```

如果为了演示额外加了页面上的测试 Tag，例如：

```jsx
<Tag>123</Tag>
```

是否提交取决于是否需要保留这个演示代码。
