---
id: learning.zephyr-docs.api-file-display-management-reference.page-16
title: zephyr__drivers__uaol.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_uaol.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB音频卸载链路（USB Audio Offload Link，UAOL）驱动的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

USB音频卸载链路（USB Audio Offload Link，UAOL）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_uaol_5Fcapabilities"></a>

```c
struct uaol_capabilities
```

相关声明：[uaol_capabilities](../audio_video_model_reference/P048_uaol_capabilities_结构体.md)。

USB音频卸载链路（UAOL）的硬件能力。

<a id="r_uaol_5Fconfig"></a>

```c
struct uaol_config
```

相关声明：[uaol_config](../audio_video_model_reference/P049_uaol_config_结构体.md)。

USB音频卸载链路（UAOL）的流配置数据。

<a id="r_uaol_5Fep_5Ftable_5Fentry"></a>

```c
struct uaol_ep_table_entry
```

相关声明：[uaol_ep_table_entry](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md)。

USB音频卸载链路（UAOL）的流端点表条目。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.2\_枚举（Enumerations）

<a id="r_afeaa6e0eee46713a5161fd2873ed58be"></a>

```c
enum uaol_direction { UAOL_DIR_PLAYBACK = 0 , UAOL_DIR_CAPTURE = 1 }
```

相关声明：[uaol_direction](#afeaa6e0eee46713a5161fd2873ed58be)、[UAOL_DIR_PLAYBACK](#afeaa6e0eee46713a5161fd2873ed58bea218584a3855ec83ec440aa3321743bad)、[UAOL_DIR_CAPTURE](#afeaa6e0eee46713a5161fd2873ed58bea373ab76b5d7dcfce76b11d8258055c92)。

UAOL 流／端点方向（Stream/Endpoint Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.3\_函数（Functions）

<a id="r_ab5a0787faab515bbc7b91972590c1ae8"></a>

```c
static int uaol_config (const struct device *dev, int stream, struct uaol_config *cfg)
```

相关声明：[uaol_config](#ab5a0787faab515bbc7b91972590c1ae8)、[device](../device_reference/P002_设备对象结构.md)。

设置 UAOL 单个流的配置（Individual Stream Configuration）。

<a id="r_abf3c266455b0dc363cf2b81fedc07f12"></a>

```c
static int uaol_start (const struct device *dev, int stream)
```

相关声明：[uaol_start](#abf3c266455b0dc363cf2b81fedc07f12)、[device](../device_reference/P002_设备对象结构.md)。

启动 UAOL 单个流的运行（Individual Stream Operation）。

<a id="r_ab698e232c95fedfb9a8e53ee1d99111c"></a>

```c
static int uaol_stop (const struct device *dev, int stream)
```

相关声明：[uaol_stop](#ab698e232c95fedfb9a8e53ee1d99111c)、[device](../device_reference/P002_设备对象结构.md)。

停止 UAOL 单个流的运行（Individual Stream Operation）。

<a id="r_a282748f7d70638f48223093fdee7ca3d"></a>

```c
static int uaol_program_ep_table (const struct device *dev, int stream, struct uaol_ep_table_entry entry, bool valid)
```

相关声明：[uaol_program_ep_table](#a282748f7d70638f48223093fdee7ca3d)、[device](../device_reference/P002_设备对象结构.md)、[uaol_ep_table_entry](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为 UAOL 单个流写入端点表项（Endpoint Table Entry）。

<a id="r_a6e466003dc004e341d726cd528c0db84"></a>

```c
static int uaol_get_capabilities (const struct device *dev, struct uaol_capabilities *caps)
```

相关声明：[uaol_get_capabilities](#a6e466003dc004e341d726cd528c0db84)、[device](../device_reference/P002_设备对象结构.md)、[uaol_capabilities](../audio_video_model_reference/P048_uaol_capabilities_结构体.md)。

查询 UAOL 硬件能力（Hardware Capabilities）。

<a id="r_a6c3e2c3cad9764baa4271237cf493eb3"></a>

```c
int uaol_get_mapped_hda_link_stream_id (const struct device *dev, int uaol_stream_id)
```

相关声明：[uaol_get_mapped_hda_link_stream_id](#a6c3e2c3cad9764baa4271237cf493eb3)、[device](../device_reference/P002_设备对象结构.md)。

获取硬件中映射到 UAOL 流 ID 的高保真音频（HDA）链路流 ID（Link Stream ID）。

## 16.4\_详细说明（Detailed Documentation）

<a id="afeaa6e0eee46713a5161fd2873ed58be"></a>

### `uaol_direction`

```c
enum uaol_direction
```

UAOL 流／端点方向（Stream/Endpoint Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UAOL_DIR_PLAYBACK` | 从主机到设备的 USB 端点（Host-to-device Endpoint）。 |
| `UAOL_DIR_CAPTURE` | 从设备到主机的 USB 端点（Device-to-host Endpoint）。 |

<a id="ab5a0787faab515bbc7b91972590c1ae8"></a>

### `uaol_config()`

```c
int uaol_config ( const struct device * dev, int stream, struct uaol_config * cfg )
```

声明属性：`inline`、`static`。

设置 UAOL 单个流的配置（Individual Stream Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `stream` | UAOL 流索引（Stream Index）。 |
| `cfg` | 要应用的配置（Configuration）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。

<a id="a6e466003dc004e341d726cd528c0db84"></a>

### `uaol_get_capabilities()`

```c
int uaol_get_capabilities ( const struct device * dev, struct uaol_capabilities * caps )
```

声明属性：`inline`、`static`。

查询 UAOL 硬件能力（Hardware Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `caps` | 要返回的能力数据（Capabilities Data）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。

<a id="a6c3e2c3cad9764baa4271237cf493eb3"></a>

### `uaol_get_mapped_hda_link_stream_id()`

```c
int uaol_get_mapped_hda_link_stream_id ( const struct device * dev, int uaol_stream_id )
```

获取硬件中映射到 UAOL 流 ID 的高保真音频（HDA）链路流 ID（Link Stream ID）。

可在任何时候调用，例如在设备探测（Device Probe）之前。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `uaol_stream_id` | UAOL 流 ID（Stream ID）。 |

**返回（Returns）**：返回值：成功时返回 HDA 链路流 ID（Link Stream ID），否则返回 -1。

<a id="a282748f7d70638f48223093fdee7ca3d"></a>

### `uaol_program_ep_table()`

```c
int uaol_program_ep_table ( const struct device * dev, int stream, struct uaol_ep_table_entry entry, bool valid )
```

声明属性：`inline`、`static`。

为 UAOL 单个流写入端点表项（Endpoint Table Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `stream` | UAOL 流索引（Stream Index）。 |
| `entry` | 要写入端点表（EP Table）的数据。 |
| `valid` | 标记表项有效或无效的标志（Valid/Invalid Flag）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。

<a id="abf3c266455b0dc363cf2b81fedc07f12"></a>

### `uaol_start()`

```c
int uaol_start ( const struct device * dev, int stream )
```

声明属性：`inline`、`static`。

启动 UAOL 单个流的运行（Individual Stream Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `stream` | UAOL 流索引（Stream Index）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。

<a id="ab698e232c95fedfb9a8e53ee1d99111c"></a>

### `uaol_stop()`

```c
int uaol_stop ( const struct device * dev, int stream )
```

声明属性：`inline`、`static`。

停止 UAOL 单个流的运行（Individual Stream Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | UAOL 设备实例（Device Instance）。 |
| `stream` | UAOL 流索引（Stream Index）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。


## 16.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P878_uaol.h_源码浏览.md)
- [uaol_capabilities](../audio_video_model_reference/P048_uaol_capabilities_结构体.md)
- [uaol_config](../audio_video_model_reference/P049_uaol_config_结构体.md)
- [uaol_ep_table_entry](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="afeaa6e0eee46713a5161fd2873ed58bea218584a3855ec83ec440aa3321743bad"></a>
<a id="afeaa6e0eee46713a5161fd2873ed58bea373ab76b5d7dcfce76b11d8258055c92"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_zephyr__drivers__uart__serial_test.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__net__wifi_credentials.h_文件参考.md)
