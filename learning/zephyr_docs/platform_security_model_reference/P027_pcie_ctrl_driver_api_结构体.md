---
id: learning.zephyr-docs.platform-security-model-reference.page-27
title: pcie_ctrl_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ctrl__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_pcie\_ctrl\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ctrl__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：PCIe控制器（Controller）驱动操作。

```c
#include <zephyr/drivers/pcie/controller.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：PCI Express（PCIe）控制器驱动操作。这是每个 PCIe 控制器驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a20c1faf02c71e88da165c889550a76ae"></a>

```c
pcie_ctrl_conf_read_t conf_read
```

相关声明：[pcie_ctrl_conf_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gac3d0f7e90bcc30996ce23324d2d7356a)、[conf_read](#a20c1faf02c71e88da165c889550a76ae)。

必需（REQ）：从端点配置空间读取一个 32 位字。

<a id="r_a46fa0fd3a759fe2dc960546b49c53979"></a>

```c
pcie_ctrl_conf_write_t conf_write
```

相关声明：[pcie_ctrl_conf_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga3241acc7de4af2b73cf3f47a25349109)、[conf_write](#a46fa0fd3a759fe2dc960546b49c53979)。

必需（REQ）：向端点配置空间写入一个 32 位字。

<a id="r_a46191bf9aad7ab7ac1319918873b8b29"></a>

```c
pcie_ctrl_region_allocate_t region_allocate
```

相关声明：[pcie_ctrl_region_allocate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga62ce18e7495256c148168b773eabd37d)、[region_allocate](#a46191bf9aad7ab7ac1319918873b8b29)。

必需（REQ）：为端点的基地址寄存器（BAR）分配内存区域的一个子范围。

<a id="r_a5d7687cd738bd86a785fc281781d2759"></a>

```c
pcie_ctrl_region_get_allocate_base_t region_get_allocate_base
```

相关声明：[pcie_ctrl_region_get_allocate_base_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa9d5bd27c841e36f65e65dec0b057e9a)、[region_get_allocate_base](#a5d7687cd738bd86a785fc281781d2759)。

必需（REQ）：获取为端点 BAR 分配的内存子区域的当前分配基地址。

<a id="r_a71a4d13492bb3098bdb2c0e0ff7b94cf"></a>

```c
pcie_ctrl_region_translate_t region_translate
```

相关声明：[pcie_ctrl_region_translate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gab144356b1c3ec3754aae0008634f2d2f)、[region_translate](#a71a4d13492bb3098bdb2c0e0ff7b94cf)。

可选（OPT）：将端点 BAR 中以总线为参照的地址转换为物理地址。

<a id="r_a1263e43fa575cc76a48bcd463b84e3a6"></a>

```c
pcie_ctrl_msi_device_setup_t msi_device_setup
```

相关声明：[msi_device_setup](#a1263e43fa575cc76a48bcd463b84e3a6)。

必需（REQ）：配置指定的 PCI 端点，使其产生消息信号中断（MSI）。

## 27.2\_详细说明（Detailed Documentation）

<a id="a20c1faf02c71e88da165c889550a76ae"></a>

### `conf_read`

```c
pcie_ctrl_conf_read_t pcie_ctrl_driver_api::conf_read
```

必需（REQ）：从端点配置空间读取一个 32 位字。

<a id="a46fa0fd3a759fe2dc960546b49c53979"></a>

### `conf_write`

```c
pcie_ctrl_conf_write_t pcie_ctrl_driver_api::conf_write
```

必需（REQ）：向端点配置空间写入一个 32 位字。

<a id="a1263e43fa575cc76a48bcd463b84e3a6"></a>

### `msi_device_setup`

```c
pcie_ctrl_msi_device_setup_t pcie_ctrl_driver_api::msi_device_setup
```

必需（REQ）：配置指定的 PCI 端点，使其产生消息信号中断（MSI）。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_PCIE_MSI`。

<a id="a46191bf9aad7ab7ac1319918873b8b29"></a>

### `region_allocate`

```c
pcie_ctrl_region_allocate_t pcie_ctrl_driver_api::region_allocate
```

必需（REQ）：为端点的基地址寄存器（BAR）分配内存区域的一个子范围。

<a id="a5d7687cd738bd86a785fc281781d2759"></a>

### `region_get_allocate_base`

```c
pcie_ctrl_region_get_allocate_base_t pcie_ctrl_driver_api::region_get_allocate_base
```

必需（REQ）：获取为端点 BAR 分配的内存子区域的当前分配基地址。

<a id="a71a4d13492bb3098bdb2c0e0ff7b94cf"></a>

### `region_translate`

```c
pcie_ctrl_region_translate_t pcie_ctrl_driver_api::region_translate
```

可选（OPT）：将端点 BAR 中以总线为参照的地址转换为物理地址。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/controller.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/controller.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h_source.html)
- [pcie_ctrl_conf_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gac3d0f7e90bcc30996ce23324d2d7356a)
- [pcie_ctrl_conf_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga3241acc7de4af2b73cf3f47a25349109)
- [pcie_ctrl_region_allocate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga62ce18e7495256c148168b773eabd37d)
- [pcie_ctrl_region_get_allocate_base_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa9d5bd27c841e36f65e65dec0b057e9a)
- [pcie_ctrl_region_translate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gab144356b1c3ec3754aae0008634f2d2f)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [CONFIG_PCIE_MSI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_pcie_ctrl_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_pcie_dev_结构体.md)
