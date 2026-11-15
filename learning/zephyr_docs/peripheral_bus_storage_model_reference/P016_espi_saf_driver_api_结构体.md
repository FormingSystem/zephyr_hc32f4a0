---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-16
title: espi_saf_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_espi\_saf\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：eSPI SAF驱动操作。

```c
#include <zephyr/drivers/espi_saf.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：eSPI 从设备附接 Flash（SAF）驱动操作。这是每个 eSPI SAF 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a4deef8ca71ecf0f602069b00110433d7"></a>

```c
espi_saf_api_config config
```

相关声明：[espi_saf_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga5f422a48cf008d7a737ec6a3fd0f0400)、[config](#a4deef8ca71ecf0f602069b00110433d7)。

`REQ`：配置 eSPI 控制器的运行方式。

<a id="r_a40236a94bc0381a2c24ac2a7ea313df7"></a>

```c
espi_saf_api_set_protection_regions set_protection_regions
```

相关声明：[espi_saf_api_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#gaeb3c1ee73f50fd05737f28a75013c2a8)、[set_protection_regions](#a40236a94bc0381a2c24ac2a7ea313df7)。

`REQ`：设置一个或多个从设备附接 Flash（Slave Attached Flash，SAF）保护区域。

<a id="r_a2e8edf284a31c4a64df5e6a663e0a237"></a>

```c
espi_saf_api_activate activate
```

相关声明：[espi_saf_api_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga03a72ef8a19738d90681114f478ff068)、[activate](#a2e8edf284a31c4a64df5e6a663e0a237)。

`REQ`：激活 SAF 模块。

<a id="r_a088327a328a6007a08d46a657b5eb559"></a>

```c
espi_saf_api_get_channel_status get_channel_status
```

相关声明：[espi_saf_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6ac9186c5b022f79dd8671594450efff)、[get_channel_status](#a088327a328a6007a08d46a657b5eb559)。

`REQ`：查询 SAF 是否就绪。

<a id="r_a3c6cebf1dec4d5335f9a063369f5668f"></a>

```c
espi_saf_api_flash_read flash_read
```

相关声明：[espi_saf_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6154711885b4edc54db016ba9826c176)、[flash_read](#a3c6cebf1dec4d5335f9a063369f5668f)。

`OPT`：发送从设备附接 Flash 的读取请求包。

<a id="r_a8b6ce9775a5852c8ca9bd495f809598c"></a>

```c
espi_saf_api_flash_write flash_write
```

相关声明：[espi_saf_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga24498afe1639bd7c5192215dc8bbbed9)、[flash_write](#a8b6ce9775a5852c8ca9bd495f809598c)。

`OPT`：发送从设备附接 Flash 的写入请求包。

<a id="r_aa8e94dd0a6e7fadaddadf98395b8e592"></a>

```c
espi_saf_api_flash_erase flash_erase
```

相关声明：[espi_saf_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga4e8a12a1311d6604a61d1a9e57573e17)、[flash_erase](#aa8e94dd0a6e7fadaddadf98395b8e592)。

`OPT`：发送从设备附接 Flash 的擦除请求包。

<a id="r_aabb50eb69906fe5b37b68981899de3c0"></a>

```c
espi_saf_api_flash_unsuccess flash_unsuccess
```

相关声明：[espi_saf_api_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga7c1aef03f238ced4e64c6e3be7ad643c)、[flash_unsuccess](#aabb50eb69906fe5b37b68981899de3c0)。

`OPT`：针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应。

<a id="r_ab6a07068dc41aa04087d56fa3b70deea"></a>

```c
espi_saf_api_manage_callback manage_callback
```

相关声明：[espi_saf_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga20ae708179a104c9334fe8fd554e5e05)、[manage_callback](#ab6a07068dc41aa04087d56fa3b70deea)。

`OPT`：管理应用程序回调，包括添加和移除。

## 16.2\_详细说明（Detailed Documentation）

<a id="a2e8edf284a31c4a64df5e6a663e0a237"></a>

### `activate`

```c
espi_saf_api_activate espi_saf_driver_api::activate
```

`REQ`：激活 SAF 模块。

<a id="a4deef8ca71ecf0f602069b00110433d7"></a>

### `config`

```c
espi_saf_api_config espi_saf_driver_api::config
```

`REQ`：配置 eSPI 控制器的运行方式。

<a id="aa8e94dd0a6e7fadaddadf98395b8e592"></a>

### `flash_erase`

```c
espi_saf_api_flash_erase espi_saf_driver_api::flash_erase
```

`OPT`：发送从设备附接 Flash 的擦除请求包。

<a id="a3c6cebf1dec4d5335f9a063369f5668f"></a>

### `flash_read`

```c
espi_saf_api_flash_read espi_saf_driver_api::flash_read
```

`OPT`：发送从设备附接 Flash 的读取请求包。

<a id="aabb50eb69906fe5b37b68981899de3c0"></a>

### `flash_unsuccess`

```c
espi_saf_api_flash_unsuccess espi_saf_driver_api::flash_unsuccess
```

`OPT`：针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应。

<a id="a8b6ce9775a5852c8ca9bd495f809598c"></a>

### `flash_write`

```c
espi_saf_api_flash_write espi_saf_driver_api::flash_write
```

`OPT`：发送从设备附接 Flash 的写入请求包。

<a id="a088327a328a6007a08d46a657b5eb559"></a>

### `get_channel_status`

```c
espi_saf_api_get_channel_status espi_saf_driver_api::get_channel_status
```

`REQ`：查询 SAF 是否就绪。

<a id="ab6a07068dc41aa04087d56fa3b70deea"></a>

### `manage_callback`

```c
espi_saf_api_manage_callback espi_saf_driver_api::manage_callback
```

`OPT`：管理应用程序回调，包括添加和移除。

<a id="a40236a94bc0381a2c24ac2a7ea313df7"></a>

### `set_protection_regions`

```c
espi_saf_api_set_protection_regions espi_saf_driver_api::set_protection_regions
```

`REQ`：设置一个或多个从设备附接 Flash（Slave Attached Flash，SAF）保护区域。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi_saf.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi_saf.h](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html)
- [espi_saf_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga5f422a48cf008d7a737ec6a3fd0f0400)
- [espi_saf_api_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#gaeb3c1ee73f50fd05737f28a75013c2a8)
- [espi_saf_api_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga03a72ef8a19738d90681114f478ff068)
- [espi_saf_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6ac9186c5b022f79dd8671594450efff)
- [espi_saf_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6154711885b4edc54db016ba9826c176)
- [espi_saf_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga24498afe1639bd7c5192215dc8bbbed9)
- [espi_saf_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga4e8a12a1311d6604a61d1a9e57573e17)
- [espi_saf_api_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga7c1aef03f238ced4e64c6e3be7ad643c)
- [espi_saf_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga20ae708179a104c9334fe8fd554e5e05)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_espi_saf_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_espi_saf_packet_结构体.md)
