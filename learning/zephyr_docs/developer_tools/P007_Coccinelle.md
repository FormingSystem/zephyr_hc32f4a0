---
id: learning.zephyr-docs.developer-tools.cocci
title: Coccinelle
kind: reference
status: maintained
domains: [zephyr, tools, development]
source_url: https://docs.zephyrproject.org/latest/develop/tools/coccinelle.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Coccinelle

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/tools/coccinelle.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。


<a id="id1"></a>
<a id="coccinelle"></a>

Coccinelle是用于模式匹配（Pattern Matching）和文本变换（Text Transformation）的工具，在内核开发中用途广泛，包括应用复杂的全源码树补丁，以及检测有问题的编程模式。

> 注意（Note）：支持Linux和macOS开发环境，不支持Windows。

<a id="getting-coccinelle"></a>

## 7.1\_获取Coccinelle

内核中的语义补丁（Semantic Patch）使用Coccinelle 1.0.0-rc11及更高版本提供的功能和选项。由于Coccinelle文件及`coccicheck`使用的选项名称已经更新，使用更早版本会失败。

许多发行版的软件包管理器提供Coccinelle，例如Debian、Fedora、Ubuntu、OpenSUSE、Arch Linux、NetBSD和FreeBSD。

部分发行版软件包已经过时，推荐使用[Coccinelle主页](https://coccinelle.lip6.fr/)发布的最新版本，或从[GitHub仓库](https://github.com/coccinelle/coccinelle)获取。

获取后，以普通用户运行：

```shell
./autogen
./configure
make
```

然后使用下列命令安装：

```shell
sudo make install
```

从源码构建的详细安装说明见[install.txt](https://github.com/coccinelle/coccinelle/blob/master/install.txt)。

<a id="supplemental-documentation"></a>

## 7.2\_补充文档

语义补丁语言（Semantic Patch Language，SmPL）的语法文档见[Coccinelle文档](https://coccinelle.gitlabpages.inria.fr/website/documentation.html)。

<a id="using-coccinelle-on-zephyr"></a>

## 7.3\_在Zephyr中使用Coccinelle

`coccicheck`检查器是Coccinelle基础设施的前端，提供多种模式。四种基本模式为`patch`、`report`、`context`和`org`，通过`--mode=<mode>`或`-m=<mode>`指定。

- `patch`：在可能时提出修复。
- `report`：按`file:line:column-column: message`格式生成列表，即文件、行、列范围及消息。
- `context`：以类似差异（Diff）的样式突出相关行及其上下文；相关行用`-`标示。
- `org`：生成Emacs Org模式格式的报告。

并非所有语义补丁都实现所有模式。为便于使用，默认模式为`report`。

另外两种模式提供常用组合：

- `chain`：按上述顺序尝试各模式，直到有一种成功。
- `rep+ctxt`：依次运行`report`和`context`模式。原文说明它应与后文所述的`C`选项配合使用，按文件检查代码。

> 译注：本页后文没有给出`C`选项的具体用法，此处保留原文引用，不补造参数。实际包装脚本的参数可对照[仓库中的coccicheck](../../../scripts/coccicheck)。

<a id="examples"></a>

### 示例（Examples）

为每个语义补丁生成报告，运行：

```shell
./scripts/coccicheck --mode=report
```

要生成补丁，运行：

```shell
./scripts/coccicheck --mode=patch
```

`coccicheck`目标会将`scripts/coccinelle`子目录中的所有语义补丁应用于整个源码树。

每个语义补丁都会提出一条提交消息，描述该补丁所检查的问题，并包含对Coccinelle的引用。

与其他静态代码分析器一样，Coccinelle也会产生误报（False Positive）。因此必须仔细检查报告，并审查补丁。

要启用详细消息，设置`--verbose=1`，例如：

```shell
./scripts/coccicheck --mode=report --verbose=1
```

<a id="coccinelle-parallelization"></a>

## 7.4\_Coccinelle并行化

默认情况下，`coccicheck`尽可能并行运行。可通过`--jobs=<number>`修改并行度。例如，在4个CPU上运行：

```shell
./scripts/coccicheck --mode=report --jobs=4
```

从Coccinelle 1.0.2起，Coccinelle使用OCaml的`parmap`进行并行化；检测到相应支持时，即可受益于`parmap`并行处理。

启用`parmap`时，`coccicheck`通过`--chunksize 1`启用动态负载均衡（Dynamic Load Balancing），逐项给线程分配工作，避免大部分工作仅由少数线程完成。提前完成的线程会继续获得更多工作。

启用`parmap`时，如果Coccinelle发生错误，其错误值会向上传递，由`coccicheck`命令的返回值捕获。

<a id="using-coccinelle-with-a-single-semantic-patch"></a>

## 7.5\_使用单个语义补丁

`--cocci`选项可用于检查单个语义补丁，此时其值必须设置为要应用的语义补丁名称。例如：

```shell
./scripts/coccicheck --mode=report --cocci=<example.cocci>
```

或者：

```shell
./scripts/coccicheck --mode=report --cocci=./path/to/<example.cocci>
```

<a id="controlling-which-files-are-processed-by-coccinelle"></a>

## 7.6\_控制处理哪些文件

默认检查整个源码树。要将Coccinelle应用于特定目录，将该目录路径作为参数传入。例如检查`drivers/usb/`：

```shell
./scripts/coccicheck --mode=patch drivers/usb/
```

默认模式为`report`，可使用前述`--mode=<mode>`选择其他模式。

<a id="debugging-coccinelle-smpl-patches"></a>

## 7.7\_调试Coccinelle SmPL补丁

最好使用`coccicheck`，因为它在`spatch`命令行中提供与内核编译时相匹配的包含选项。使用详细输出选项可以了解这些参数，再手动运行Coccinelle并添加调试选项。

也可以通过重定向标准错误（stderr）调试Coccinelle对SmPL补丁的处理。原文此处写作“将stderr重定向到stderr”；默认情况下，stderr被重定向到`/dev/null`。若希望捕获stderr，可以给`coccicheck`指定`--debug=file.err`。例如：

```shell
rm -f cocci.err
./scripts/coccicheck --mode=patch --debug=cocci.err
cat cocci.err
```

调试支持仅适用于Coccinelle 1.0.2及以上版本。

<a id="additional-flags"></a>

## 7.8\_附加标志

可通过`SPFLAGS`变量向`spatch`传递附加标志。发生选项冲突时，Coccinelle采用最后传入的标志，因此这种方式可以覆盖先前选项。

```shell
./scripts/coccicheck --sp-flag="--use-glimpse"
```

Coccinelle也支持`idutils`，但需要1.0.6及以上版本。如果没有指定ID文件，Coccinelle假定ID数据库位于内核顶层的`.id-utils.index`文件中。Coccinelle提供`scripts/idutils_index.sh`脚本，使用以下命令创建数据库：

```shell
mkid -i C --output .id-utils.index
```

如果数据库使用其他文件名，也可以创建名为`.id-utils.index`的符号链接。

```shell
./scripts/coccicheck --sp-flag="--use-idutils"
```

也可以显式指定数据库文件名，例如：

```shell
./scripts/coccicheck --sp-flag="--use-idutils /full-path/to/ID"
```

> 译注：`/full-path/to/ID`是官方示例中用于数据库位置的占位路径，不是作者机器目录。应按实际数据库位置设置。

有时，由于定义不完整，Coccinelle无法识别或解析复杂宏变量。为了使其可解析，可以用`---macro-file-builtins <headerfile.h>`标志显式提供复杂宏的原型。

`<headerfile.h>`应包含复杂宏的完整原型，供`spatch`引擎提取变换所需的类型信息。

例如，Coccinelle无法识别`Z_SYSCALL_HANDLER`，于是将其原型放入头文件，例如`mymacros.h`：

```shell
$ cat mymacros.h
#define Z_SYSCALL_HANDLER int xxx
```

在变换时传入`mymacros.h`：

```shell
./scripts/coccicheck --sp-flag="---macro-file-builtins mymacros.h"
```

> 译注：原文说明及命令都将`---macro-file-builtins`写成三个前导连字符，此处保留原例；使用前请通过当前版本的`spatch --help`核对选项拼写。

更多`spatch`选项见`spatch --help`。

`--use-glimpse`和`--use-idutils`需要外部工具建立代码索引，因此默认都未启用。不过，使用其中一种工具建立索引后，视所用cocci文件而定，`spatch`可能更快处理整个代码库。

<a id="smpl-patch-specific-options"></a>

## 7.9\_SmPL补丁专用选项

SmPL补丁可能对传入Coccinelle的选项有自身要求。可以在补丁顶部指定这些选项，例如：

```text
// Options: --no-includes --include-headers
```

<a id="proposing-new-semantic-patches"></a>

## 7.10\_提出新的语义补丁

内核开发者可以提出并提交新的语义补丁。为了组织清晰，应将其放在`scripts/coccinelle/`的子目录中。

cocci脚本应满足以下要求：

1. 必须提供`report`模式。
2. 开头几行应使用`///`注释说明脚本用途。基于脚本提出补丁时，这段消息通常作为提交日志。

<a id="example"></a>

例如：

```text
/// Use ARRAY_SIZE instead of dividing sizeof array with sizeof an element
```

3. 可以使用`//#`注释列出更详细的信息，包括特殊情况或误报（如有）。

<a id="id2"></a>

例如：

```text
//# This makes an effort to find cases where ARRAY_SIZE can be used such as
//# where there is a division of sizeof the array by the sizeof its first
//# element or by any indexed element or the element type. It replaces the
//# division of the two sizeofs by ARRAY_SIZE.
```

上述注释说明：该脚本寻找可使用`ARRAY_SIZE`的情况，例如用数组的`sizeof`除以首元素、任意索引元素或元素类型的`sizeof`，并用`ARRAY_SIZE`替换两个`sizeof`相除的表达式。

4. **置信度（Confidence）**：指定脚本准确程度的属性，根据观察到的误报数量，可设为高（`High`）、中等（`Moderate`）或低（`Low`）。

<a id="id3"></a>

例如：

```text
// Confidence: High
```

5. **虚拟规则（Virtual Rules）**：用于支持脚本中的各种模式。脚本中指定的虚拟规则应具有对应的模式处理规则。

<a id="id4"></a>

例如：

```text
virtual context

@depends on context@
type T;
T[] E;
@@
(
* (sizeof(E)/sizeof(*E))
|
* (sizeof(E)/sizeof(E[...]))
|
* (sizeof(E)/sizeof(T))
)
```

<a id="detailed-description-of-the-report-mode"></a>

## 7.11\_report模式详解

`report`按以下格式生成列表：

```text
file:line:column-column: message
```

<a id="id5"></a>

### 示例（Example）

运行：

```shell
./scripts/coccicheck --mode=report --cocci=scripts/coccinelle/array_size.cocci
```

会执行SmPL脚本的以下部分：

```text
<smpl>

@r depends on (org || report)@
type T;
T[] E;
position p;
@@
(
(sizeof(E)@p /sizeof(*E))
|
(sizeof(E)@p /sizeof(E[...]))
|
(sizeof(E)@p /sizeof(T))
)

@script:python depends on report@
p << r.p;
@@

msg="WARNING: Use ARRAY_SIZE"
coccilib.report.print_report(p[0], msg)

</smpl>
```

该SmPL片段在标准输出中生成条目，如下所示：

```text
ext/hal/nxp/mcux/drivers/lpc/fsl_wwdt.c:66:49-50: WARNING: Use ARRAY_SIZE
ext/hal/nxp/mcux/drivers/lpc/fsl_ctimer.c:74:53-54: WARNING: Use ARRAY_SIZE
ext/hal/nxp/mcux/drivers/imx/fsl_dcp.c:944:45-46: WARNING: Use ARRAY_SIZE
```

<a id="detailed-description-of-the-patch-mode"></a>

## 7.12\_patch模式详解

如果提供`patch`模式，它会为每个发现的问题提出修复。

<a id="id6"></a>

### 示例（Example）

运行：

```shell
./scripts/coccicheck --mode=patch --cocci=scripts/coccinelle/misc/array_size.cocci
```

会执行SmPL脚本的以下部分：

```text
<smpl>

@depends on patch@
type T;
T[] E;
@@
(
- (sizeof(E)/sizeof(*E))
+ ARRAY_SIZE(E)
|
- (sizeof(E)/sizeof(E[...]))
+ ARRAY_SIZE(E)
|
- (sizeof(E)/sizeof(T))
+ ARRAY_SIZE(E)
)

</smpl>
```

该SmPL片段在标准输出中生成补丁块（Patch Hunk），如下所示：

```diff
diff -u -p a/ext/lib/encoding/tinycbor/src/cborvalidation.c b/ext/lib/encoding/tinycbor/src/cborvalidation.c
--- a/ext/lib/encoding/tinycbor/src/cborvalidation.c
+++ b/ext/lib/encoding/tinycbor/src/cborvalidation.c
@@ -325,7 +325,7 @@ static inline CborError validate_number(
static inline CborError validate_tag(CborValue *it, CborTag tag, int flags, int recursionLeft)
{
  CborType type = cbor_value_get_type(it);
-    const size_t knownTagCount = sizeof(knownTagData) / sizeof(knownTagData[0]);
+    const size_t knownTagCount = ARRAY_SIZE(knownTagData);
   const struct KnownTagData *tagData = knownTagData;
   const struct KnownTagData * const knownTagDataEnd = knownTagData + knownTagCount;
```

<a id="detailed-description-of-the-context-mode"></a>

## 7.13\_context模式详解

`context`以类似差异的样式突出相关行及其上下文。

> 注意（Note）：这种类似差异的输出**不是可应用的补丁**。`context`模式旨在突出重要行，以减号`-`标记，并给出周围一些上下文。可使用Emacs的Diff模式查看此输出并审查代码。

<a id="id7"></a>

### 示例（Example）

运行：

```shell
./scripts/coccicheck --mode=context --cocci=scripts/coccinelle/array_size.cocci
```

会执行SmPL脚本的以下部分：

```text
<smpl>

@depends on context@
type T;
T[] E;
@@
(
* (sizeof(E)/sizeof(*E))
|
* (sizeof(E)/sizeof(E[...]))
|
* (sizeof(E)/sizeof(T))
)

</smpl>
```

该SmPL片段在标准输出中生成差异块（Diff Hunk），如下所示：

```diff
diff -u -p ext/lib/encoding/tinycbor/src/cborvalidation.c /tmp/nothing/ext/lib/encoding/tinycbor/src/cborvalidation.c
--- ext/lib/encoding/tinycbor/src/cborvalidation.c
+++ /tmp/nothing/ext/lib/encoding/tinycbor/src/cborvalidation.c
@@ -325,7 +325,6 @@ static inline CborError validate_number(
static inline CborError validate_tag(CborValue *it, CborTag tag, int flags, int recursionLeft)
{
  CborType type = cbor_value_get_type(it);
-    const size_t knownTagCount = sizeof(knownTagData) / sizeof(knownTagData[0]);
   const struct KnownTagData *tagData = knownTagData;
   const struct KnownTagData * const knownTagDataEnd = knownTagData + knownTagCount;
```

<a id="detailed-description-of-the-org-mode"></a>

## 7.14\_org模式详解

`org`生成Emacs Org模式格式的报告。

<a id="id8"></a>

### 示例（Example）

运行：

```shell
./scripts/coccicheck --mode=org --cocci=scripts/coccinelle/misc/array_size.cocci
```

会执行SmPL脚本的以下部分：

```text
<smpl>

@r depends on (org || report)@
type T;
T[] E;
position p;
@@
(
(sizeof(E)@p /sizeof(*E))
|
(sizeof(E)@p /sizeof(E[...]))
|
(sizeof(E)@p /sizeof(T))
)

@script:python depends on org@
p << r.p;
@@
coccilib.org.print_todo(p[0], "WARNING should use ARRAY_SIZE")

</smpl>
```

该SmPL片段在标准输出中生成Org条目，如下所示：

```text
* TODO [[view:ext/lib/encoding/tinycbor/src/cborvalidation.c::face=ovl-face1::linb=328::colb=52::cole=53][WARNING should use ARRAY_SIZE]]
```

> 译注：原文不同示例分别使用`scripts/coccinelle/array_size.cocci`和`scripts/coccinelle/misc/array_size.cocci`，并展示旧的`ext/`布局；保留原例以便对照。当前仓库中的参照脚本位于[array_size.cocci](../../../scripts/coccinelle/array_size.cocci)，实际运行应以所用源码版本的目录为准。

<a id="coccinelle-mailing-list"></a>

## 7.15\_Coccinelle邮件列表

可在[此处订阅Coccinelle邮件列表](https://systeme.lip6.fr/mailman/listinfo/cocci)。归档可通过以下位置查阅：

- [lore.kernel.org归档](https://lore.kernel.org/cocci/)
- [systeme.lip6.fr归档](https://systeme.lip6.fr/pipermail/cocci/)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：STM32CubeIDE](P006_STM32CubeIDE.md) · [本模块主线目录](../reading/developer_tools.md) · [全部主线](../reading/README.md) · [下一篇：Kapa.ai文档助手](P008_Kapa_AI.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：STM32CubeIDE](P006_STM32CubeIDE.md) · [返回大纲](大纲.md) · [下一章：Kapa.ai文档助手](P008_Kapa_AI.md)

</details>

<!-- reading-navigation:end -->
