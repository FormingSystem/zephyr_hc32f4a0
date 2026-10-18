---
id: learning.zephyr-docs.flash-reference.page-7
title: Flash驱动操作结构
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Flash驱动操作结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__driver__api.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

驱动操作（Driver Operations）：Flash 驱动的操作集合。

```c
#include <zephyr/drivers/flash.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：Flash 驱动的操作集合。这是所有 Flash 驱动都需要定义的驱动 API 结构体，包含驱动实现的操作函数指针，以及其他驱动专用常量数据。标为必填（Required，REQ）的成员必须由驱动设置；标为可选（Optional，OPT）的成员可以省略。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_aa3f58e76ce1a1bacf57d874a4e190480"></a>

```c
flash_api_read read
```

相关声明：[flash_api_read](P002_Flash驱动后端接口.md#ga358404d040b7ef30c8d24106e97bc290)、[read](#aa3f58e76ce1a1bacf57d874a4e190480)。

必填（REQ）：从闪存读取数据。

<a id="r_aa799a18761bbe6d43a82dc12a8de44c4"></a>

```c
flash_api_write write
```

相关声明：[flash_api_write](P002_Flash驱动后端接口.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)、[write](#aa799a18761bbe6d43a82dc12a8de44c4)。

必填（REQ）：将缓冲区内容写入闪存。

<a id="r_acaf3275b42cb048eca00818026f10f15"></a>

```c
flash_api_erase erase
```

相关声明：[flash_api_erase](P002_Flash驱动后端接口.md#ga2178a2338e652396ba9811ca449f4cb5)、[erase](#acaf3275b42cb048eca00818026f10f15)。

可选（OPT）：擦除部分或全部闪存。

<a id="r_a2696431e3b94db2f8a830e3142a577fc"></a>

```c
flash_api_get_parameters get_parameters
```

相关声明：[flash_api_get_parameters](P002_Flash驱动后端接口.md#ga2dee3874cb1be4ef4dab599963c30e70)、[get_parameters](#a2696431e3b94db2f8a830e3142a577fc)。

必填（REQ）：取得 `flash_parameters` 结构体指针。

<a id="r_aa59f704dfaa541860983a89731a47302"></a>

```c
flash_api_get_size get_size
```

相关声明：[flash_api_get_size](P002_Flash驱动后端接口.md#ga97ab6540136589aaafbe049cf4302285)、[get_size](#aa59f704dfaa541860983a89731a47302)。

可选（OPT）：取得设备容量，单位为字节。

<a id="r_a82b03b535d86e98c083b701176a5556b"></a>

```c
flash_api_pages_layout page_layout
```

相关声明：[flash_api_pages_layout](P002_Flash驱动后端接口.md#ga7576411536217c9ec3e167e7a5ca82a5)、[page_layout](#a82b03b535d86e98c083b701176a5556b)。

必填（REQ）：取得闪存设备布局。

<a id="r_a0d8122a16fe671099cb9c13459fc022c"></a>

```c
flash_api_sfdp_read sfdp_read
```

相关声明：[flash_api_sfdp_read](P002_Flash驱动后端接口.md#gac7b802015885044df6a1872513b89ab5)、[sfdp_read](#a0d8122a16fe671099cb9c13459fc022c)。

可选（OPT）：从串行闪存可发现参数（SFDP）区域读取数据。

<a id="r_add4026f7bd3a49de6de1dfee7c43d57b"></a>

```c
flash_api_read_jedec_id read_jedec_id
```

相关声明：[flash_api_read_jedec_id](P002_Flash驱动后端接口.md#ga088369ef7593aa7c1fbe4cdad6e5b994)、[read_jedec_id](#add4026f7bd3a49de6de1dfee7c43d57b)。

可选（OPT）：从兼容闪存设备读取 JEDEC 标识。

<a id="r_a8914c40aef441921123ee8ff6aee94c2"></a>

```c
flash_api_ex_op ex_op
```

相关声明：[flash_api_ex_op](P002_Flash驱动后端接口.md#gacff972cc16c1afa0a85e3118eff0afb2)、[ex_op](#a8914c40aef441921123ee8ff6aee94c2)。

可选（OPT）：执行闪存驱动的厂商专用扩展操作。

## 7.2\_详细说明（Detailed Documentation）

<a id="acaf3275b42cb048eca00818026f10f15"></a>

### `erase`

```c
flash_api_erase flash_driver_api::erase
```

可选（OPT）：擦除部分或全部闪存。

<a id="a8914c40aef441921123ee8ff6aee94c2"></a>

### `ex_op`

```c
flash_api_ex_op flash_driver_api::ex_op
```

可选（OPT）：执行闪存驱动的厂商专用扩展操作。

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_EX_OP_ENABLED` 时可用。

<a id="a2696431e3b94db2f8a830e3142a577fc"></a>

### `get_parameters`

```c
flash_api_get_parameters flash_driver_api::get_parameters
```

必填（REQ）：取得 `flash_parameters` 结构体指针。

<a id="aa59f704dfaa541860983a89731a47302"></a>

### `get_size`

```c
flash_api_get_size flash_driver_api::get_size
```

可选（OPT）：取得设备容量，单位为字节。

<a id="a82b03b535d86e98c083b701176a5556b"></a>

### `page_layout`

```c
flash_api_pages_layout flash_driver_api::page_layout
```

必填（REQ）：取得闪存设备布局。

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

> 译注——源码核对：REQ 要求适用于该成员存在的配置。头文件在 CONFIG_FLASH_PAGE_LAYOUT 或文档生成条件 __DOXYGEN__ 下声明此成员，不能要求未启用该配置的结构初始化器填写不存在的字段。

<a id="aa3f58e76ce1a1bacf57d874a4e190480"></a>

### `read`

```c
flash_api_read flash_driver_api::read
```

必填（REQ）：从闪存读取数据。

<a id="add4026f7bd3a49de6de1dfee7c43d57b"></a>

### `read_jedec_id`

```c
flash_api_read_jedec_id flash_driver_api::read_jedec_id
```

可选（OPT）：从兼容闪存设备读取 JEDEC 标识。

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_JESD216_API` 时可用。

<a id="a0d8122a16fe671099cb9c13459fc022c"></a>

### `sfdp_read`

```c
flash_api_sfdp_read flash_driver_api::sfdp_read
```

可选（OPT）：从串行闪存可发现参数（SFDP）区域读取数据。

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_JESD216_API` 时可用。

<a id="aa799a18761bbe6d43a82dc12a8de44c4"></a>

### `write`

```c
flash_api_write flash_driver_api::write
```

必填（REQ）：将缓冲区内容写入闪存。

## 7.3\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

> 译注——条件声明与展示：本次API网页列出九个后端操作类型和九个驱动成员；[官方源码浏览译文](P010_Flash公共头文件源码.md)同时包含CONFIG_FLASH_HAS_DRIVER_FILL条件下的flash_api_fill与fill。去掉注释和展示空白后，该源码页与本次读取的main头文件代码一致，因此不能将API摘要未展示fill归因于版本不同。应按实际编译配置判断成员是否存在。

## 7.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](P010_Flash公共头文件源码.md)
- [flash_api_read](P002_Flash驱动后端接口.md#ga358404d040b7ef30c8d24106e97bc290)
- [flash_api_write](P002_Flash驱动后端接口.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)
- [flash_api_erase](P002_Flash驱动后端接口.md#ga2178a2338e652396ba9811ca449f4cb5)
- [flash_api_get_parameters](P002_Flash驱动后端接口.md#ga2dee3874cb1be4ef4dab599963c30e70)
- [flash_parameters](P004_Flash存储参数结构.md)
- [flash_api_get_size](P002_Flash驱动后端接口.md#ga97ab6540136589aaafbe049cf4302285)
- [flash_api_pages_layout](P002_Flash驱动后端接口.md#ga7576411536217c9ec3e167e7a5ca82a5)
- [flash_api_sfdp_read](P002_Flash驱动后端接口.md#gac7b802015885044df6a1872513b89ab5)
- [flash_api_read_jedec_id](P002_Flash驱动后端接口.md#ga088369ef7593aa7c1fbe4cdad6e5b994)
- [flash_api_ex_op](P002_Flash驱动后端接口.md#gacff972cc16c1afa0a85e3118eff0afb2)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [CONFIG_FLASH_EX_OP_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_EX_OP_ENABLED)
- [CONFIG_FLASH_PAGE_LAYOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_PAGE_LAYOUT)
- [CONFIG_FLASH_JESD216_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_JESD216_API)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_Flash页布局结构.md) · [返回大纲](大纲.md) · [下一章](P008_Flash扩展操作目录.md)
