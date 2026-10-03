<!-- SPDX-License-Identifier: Apache-2.0 -->

# P01 教学课件维护

正式课件为本目录的 `P01_准备UCRT64环境与下载Zephyr.pptx`，当前共 28 页，在作者原有内容的 ZIP 下载页前补充一页代理配置。
历史审阅副本不随仓库发布，修改时以本目录正式课件为准。正文、图片、表格与讲解备注均可在 PowerPoint 内编辑；
代码页使用白底和语法配色，正文页使用自动幻灯片编号，封面不编号。

## 源码与重建

`src/` 保存正式课件的原生 Open XML 源码和内嵌素材，`source.json` 记录实际页序、标题及文件清单。
`src/ppt/slides/` 为页面内容与排版，`src/ppt/notesSlides/` 为讲解备注，`src/ppt/media/` 为图片。
页序以 `source.json` 为准，不以 XML 文件名猜测。字体为 Noto Sans SC 与 Consolas。

本目录的 `.gitattributes` 保留包内文件原始字节与 CRLF 行尾，保证 Git 检出后仍能重建相同部件。

在本目录的 PowerShell 或 CMD 中运行，需 Python 3.10 或更高版本，无第三方库依赖：

```powershell
python build.py build --force
```

这会将源码打包为本目录的正式课件，保留原生可编辑对象、代码颜色和自动页码。
`--force` 表示覆盖已有正式课件；也可以用 `--output 新文件.pptx` 输出另一份文件。

## 在 PowerPoint 中修改后同步

先保存并关闭课件，再同步源码。推荐始终编辑正式课件：

```powershell
python build.py sync
```

如果另行建立并修改了上一级审阅副本，可显式指定它：

```powershell
python build.py sync --input ../review-v3.pptx
python build.py build --force
```

同步会更新源码和页序清单，保留手工删减及排版，后续重建不会恢复已删除的页面。
新增页面时可复制带有自动页码的正文页；同步脚本会检查正文页是否带有自动编号。
正式课件更新后，如需继续保留一致的审阅副本，在 PowerShell 中执行：

```powershell
Copy-Item -LiteralPath ./P01_准备UCRT64环境与下载Zephyr.pptx -Destination ../review-v3.pptx -Force
```

教程正文仍在上一级 Markdown 文件中，保留详细操作说明；PPT 源码单独维护，不从长篇教程自动扩写页面。
