---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-15
title: 调制解调器 UBX 协议（Modem Ubx）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_调制解调器 UBX 协议（Modem Ubx）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器 UBX 协议（Modem Ubx）

<a id="details"></a>

调制解调器 UBX（Modem Ubx）。**引入版本（Since）：**3.7。**版本（Version）：**1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_modem_5Fubx_5Fmatch"></a>

```c
struct modem_ubx_match
```

相关声明：[modem_ubx_match](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md)。

<a id="r_modem_5Fubx_5Fscript"></a>

```c
struct modem_ubx_script
```

相关声明：[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)。

<a id="r_modem_5Fubx"></a>

```c
struct modem_ubx
```

相关声明：[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

<a id="r_modem_5Fubx_5Fconfig"></a>

```c
struct modem_ubx_config
```

相关声明：[modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga8a37614e3a9cf6d4773b9e74de79d340"></a>

```c
#define MODEM_UBX_MATCH_ARRAY_DEFINE(_name, ...)
```

相关声明：[MODEM_UBX_MATCH_ARRAY_DEFINE](#ga8a37614e3a9cf6d4773b9e74de79d340)。

<a id="r_ga4c04f643a1ea9f0fc940d286713be30e"></a>

```c
#define MODEM_UBX_MATCH_DEFINE(_class_id, _msg_id, _handler)
```

相关声明：[MODEM_UBX_MATCH_DEFINE](#ga4c04f643a1ea9f0fc940d286713be30e)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_gae0bfe22e7e8d7d38ae9f41648f7fcfda"></a>

```c
typedef void(* modem_ubx_match_callback) (struct modem_ubx *ubx, const struct ubx_frame *frame, size_t len, void *user_data)
```

相关声明：[modem_ubx_match_callback](#gae0bfe22e7e8d7d38ae9f41648f7fcfda)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.4\_函数（Functions）

<a id="r_ga4e459f955e34c9059702c3d7f9794948"></a>

```c
int modem_ubx_attach (struct modem_ubx *ubx, struct modem_pipe *pipe)
```

相关声明：[modem_ubx_attach](#ga4e459f955e34c9059702c3d7f9794948)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

将管道（Pipe）连接到 Modem Ubx。

<a id="r_ga68210f4afd5880c532d82fd0bac1d933"></a>

```c
void modem_ubx_release (struct modem_ubx *ubx)
```

相关声明：[modem_ubx_release](#ga68210f4afd5880c532d82fd0bac1d933)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

从 Modem Ubx 实例（Instance）释放管道（Pipe）。

<a id="r_gaf49363fb4decb4656566b508a061212f"></a>

```c
int modem_ubx_init (struct modem_ubx *ubx, const struct modem_ubx_config *config)
```

相关声明：[modem_ubx_init](#gaf49363fb4decb4656566b508a061212f)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)。

初始化 Modem Ubx 实例（Instance）。

<a id="r_ga770650b055fd597f000a1d4f9daaf712"></a>

```c
int modem_ubx_run_script (struct modem_ubx *ubx, struct modem_ubx_script *script)
```

相关声明：[modem_ubx_run_script](#ga770650b055fd597f000a1d4f9daaf712)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)。

写入 `script.request` 中的 UBX 帧（UBX Frame），并在有响应时读回其响应（Response）。

<a id="r_ga0fd0def90f6304e679c4123e3c8d0c3f"></a>

```c
int modem_ubx_run_script_for_each (struct modem_ubx *ubx, struct modem_ubx_script *script, struct ubx_frame *array, size_t array_size)
```

相关声明：[modem_ubx_run_script_for_each](#ga0fd0def90f6304e679c4123e3c8d0c3f)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)、[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。

## 15.5\_详细说明（Detailed Documentation）

<a id="ga8a37614e3a9cf6d4773b9e74de79d340"></a>

### `MODEM_UBX_MATCH_ARRAY_DEFINE`

```c
#define MODEM_UBX_MATCH_ARRAY_DEFINE ( _name, ... )
```

```c
#include <zephyr/modem/ubx.h>
```

展开值（Value）：

```c
struct modem_ubx_match _name[] = {__VA_ARGS__};
```

<a id="ga4c04f643a1ea9f0fc940d286713be30e"></a>

### `MODEM_UBX_MATCH_DEFINE`

```c
#define MODEM_UBX_MATCH_DEFINE ( _class_id, _msg_id, _handler )
```

```c
#include <zephyr/modem/ubx.h>
```

展开值（Value）：

```c
{                                                                                                  \
        .filter = {                                                                                \
                .class = _class_id,                                                                \
                .id = _msg_id,                                                                     \
        },                                                                                         \
        .handler = _handler,                                                                       \
}
```

<a id="gae0bfe22e7e8d7d38ae9f41648f7fcfda"></a>

### `modem_ubx_match_callback`

```c
typedef void(* modem_ubx_match_callback) (struct modem_ubx *ubx, const struct ubx_frame *frame, size_t len, void *user_data)
```

```c
#include <zephyr/modem/ubx.h>
```

<a id="ga4e459f955e34c9059702c3d7f9794948"></a>

### `modem_ubx_attach()`

```c
int modem_ubx_attach ( struct modem_ubx * ubx, struct modem_pipe * pipe )
```

```c
#include <zephyr/modem/ubx.h>
```

将管道（Pipe）连接到 Modem Ubx。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ubx` | 调制解调器 UBX 实例（Modem Ubx Instance）。 |
| `pipe` | 要将调制解调器 UBX 实例关联到的管道实例（Pipe Instance）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno` 错误码。

**说明（Note）**：**注意（Note）：**成功时会启用调制解调器 UBX 实例（Modem Ubx Instance）。

<a id="gaf49363fb4decb4656566b508a061212f"></a>

### `modem_ubx_init()`

```c
int modem_ubx_init ( struct modem_ubx * ubx, const struct modem_ubx_config * config )
```

```c
#include <zephyr/modem/ubx.h>
```

初始化 Modem Ubx 实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ubx` | 调制解调器 UBX 实例（Modem Ubx Instance）。 |
| `config` | 要应用到调制解调器 UBX 实例（Modem Ubx Instance）的配置（Configuration）。 |

**说明（Note）**：**注意（Note）：**调制解调器 UBX 实例（Modem Ubx Instance）必须关联到管道实例（Pipe Instance）。

<a id="ga68210f4afd5880c532d82fd0bac1d933"></a>

### `modem_ubx_release()`

```c
void modem_ubx_release ( struct modem_ubx * ubx)
```

```c
#include <zephyr/modem/ubx.h>
```

从 Modem Ubx 实例（Instance）释放管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ubx` | 调制解调器 UBX 实例（Modem Ubx Instance）。 |

<a id="ga770650b055fd597f000a1d4f9daaf712"></a>

### `modem_ubx_run_script()`

```c
int modem_ubx_run_script ( struct modem_ubx * ubx, struct modem_ubx_script * script )
```

```c
#include <zephyr/modem/ubx.h>
```

写入 `script.request` 中的 UBX 帧（UBX Frame），并在有响应时读回其响应（Response）。

对于每个发出的 UBX 帧（Frame），设备可能不响应，也可能以下列一种或两种方式响应：

- 设备发回 UBX-ACK 帧，表示“确认”（Acknowledge）或“未确认”（Not-acknowledge）。注意：由 UBX-ACK 帧的消息 ID 决定设备是否确认。例如，发送 UBX-CFG 帧后，设备以 UBX-ACK 帧响应。
- 设备发回与发送给它的帧相同类型的帧，并填充其载荷（Payload），用于获取与所发帧对应的当前配置。例如，“获取”（Get）或“轮询”（Poll）类 UBX 帧以这种方式响应。如果收到此响应，将其写入 `script.response`。

本函数写出 `script.request` 中的 UBX 帧，然后读取响应。如果 `script.match` 不为 `NULL`，会将从设备收到的每个 UBX 帧与 `script.match` 比较，以检查是否匹配。可将脚本期望收到的 UBX-ACK 填入 `script.match`，据此匹配设备发回的 UBX-ACK 帧。

出现以下任一情况时，脚本（Script）终止：

- 成功接收并匹配 `script.match`。
- 发生由 `script.timeout` 指定的超时（Timeout）。

**参数（Parameters）：**`ubx` 为调制解调器 UBX 实例（Modem Ubx Instance），`script` 为要执行的脚本。

**注意（Note）：**`script.request` 中 UBX 帧的长度不得超过 `UBX_FRAME_SZ_MAX`。调制解调器 UBX 实例必须关联到管道实例（Pipe Instance）。

**返回值（Returns）：**成功返回 `0`，失败返回负 `errno` 错误码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ubx` | 调制解调器 UBX 实例（Modem Ubx Instance）。 |
| `script` | 要执行的脚本（Script）。 |

**说明（Note）**：**注意（Note）：**`script.request` 中 UBX 帧的长度不得超过 `UBX_FRAME_SZ_MAX`。调制解调器 UBX 实例（Modem Ubx Instance）必须关联到管道实例（Pipe Instance）。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno` 错误码。

<a id="ga0fd0def90f6304e679c4123e3c8d0c3f"></a>

### `modem_ubx_run_script_for_each()`

```c
int modem_ubx_run_script_for_each ( struct modem_ubx * ubx, struct modem_ubx_script * script, struct ubx_frame * array, size_t array_size )
```

```c
#include <zephyr/modem/ubx.h>
```


## 15.6\_原页交叉引用（Cross References）

- [modem_ubx_match](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md)
- [modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)
- [modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)
- [modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)
- [ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)
- [zephyr/modem/ubx.h](../api_file_service_reference/P058_zephyr__modem__ubx.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructmodem__ubx__match_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_调制解调器管道链接（Modem pipelink）.md) · [返回大纲](大纲.md) · [下一章](P016_网络 MIDI 2.0（Network MIDI 2.0）.md)
