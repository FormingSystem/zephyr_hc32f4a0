---
id: learning.zephyr-docs.platform-security-model-reference.page-20
title: nxp_flexio_child_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnxp__flexio__child.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_nxp\_flexio\_child\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnxp__flexio__child.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含FlexIO所需子设备数据（Child Data）的结构。

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

<a id="details"></a>

包含FlexIO所需子设备数据（Child Data）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a1befee43b0d6a378983a8207fdb23b10"></a>

```c
nxp_flexio_child_isr_t isr
```

相关声明：[nxp_flexio_child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gaf11959c4e7c7a5ef56b082fcf0b7f42c)、[isr](#a1befee43b0d6a378983a8207fdb23b10)。

从 FlexIO 控制器的 IRQ 处理函数调用的中断服务例程（ISR）。

<a id="r_a9490af6c5e89d9994a0419c80757b14e"></a>

```c
void * user_data
```

相关声明：[user_data](#a9490af6c5e89d9994a0419c80757b14e)。

调用 `isr` 函数时传入的不透明指针。

<a id="r_ae1c82ed160a226d48dee0ad6607cde34"></a>

```c
struct nxp_flexio_child_res res
```

相关声明：[nxp_flexio_child_res](P021_nxp_flexio_child_res_结构体.md)、[res](#ae1c82ed160a226d48dee0ad6607cde34)。

资源需求以及由 `nxp_flexio_child_attach()` 填写的输出索引。

## 20.2\_详细说明（Detailed Documentation）

<a id="a1befee43b0d6a378983a8207fdb23b10"></a>

### `isr`

```c
nxp_flexio_child_isr_t nxp_flexio_child::isr
```

从 FlexIO 控制器的 IRQ 处理函数调用的中断服务例程（ISR）。

如果子设备不需要 IRQ 通知，可以为 `NULL`。

<a id="ae1c82ed160a226d48dee0ad6607cde34"></a>

### `res`

```c
struct nxp_flexio_child_res nxp_flexio_child::res
```

资源需求以及由 `nxp_flexio_child_attach()` 填写的输出索引。

<a id="a9490af6c5e89d9994a0419c80757b14e"></a>

### `user_data`

```c
void* nxp_flexio_child::user_data
```

调用 `isr` 函数时传入的不透明指针。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/nxp_flexio/nxp_flexio.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/nxp_flexio/nxp_flexio.h](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h_source.html)
- [nxp_flexio_child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gaf11959c4e7c7a5ef56b082fcf0b7f42c)
- [nxp_flexio_child_res](P021_nxp_flexio_child_res_结构体.md)
- [nxp_flexio_child_attach()](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga1208ad4ef70419ff61a87b8b1ff8d446)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_msix_vector_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_nxp_flexio_child_res_结构体.md)
