---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-20
title: zephyr__mgmt__osdp.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_mgmt\_\_osdp.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

开放监控设备协议（Open Supervised Device Protocol，OSDP）的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <stdint.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

开放监控设备协议（Open Supervised Device Protocol，OSDP）的公共API头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_osdp_5Fcmd_5Foutput"></a>

```c
struct osdp_cmd_output
```

相关声明：[osdp_cmd_output](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md)。

控制面板（CP）发送的命令，用于控制外设（PD）的数字输出。

<a id="r_osdp_5Fcmd_5Fled_5Fparams"></a>

```c
struct osdp_cmd_led_params
```

相关声明：[osdp_cmd_led_params](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md)。

LED参数子结构（Parameters Sub-Structure）。

<a id="r_osdp_5Fcmd_5Fled"></a>

```c
struct osdp_cmd_led
```

相关声明：[osdp_cmd_led](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md)。

由控制面板（CP）发送至外设（PD），用于控制其板载LED的行为。

<a id="r_osdp_5Fcmd_5Fbuzzer"></a>

```c
struct osdp_cmd_buzzer
```

相关声明：[osdp_cmd_buzzer](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md)。

由控制面板（CP）发送，用于控制外设（PD）中蜂鸣器的行为。

<a id="r_osdp_5Fcmd_5Ftext"></a>

```c
struct osdp_cmd_text
```

相关声明：[osdp_cmd_text](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md)。

用于操控外设（PD）所支持任意显示单元（Display Units）的命令。

<a id="r_osdp_5Fcmd_5Fcomset"></a>

```c
struct osdp_cmd_comset
```

相关声明：[osdp_cmd_comset](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md)。

作为对COMSET命令的响应发送。

<a id="r_osdp_5Fcmd_5Fkeyset"></a>

```c
struct osdp_cmd_keyset
```

相关声明：[osdp_cmd_keyset](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md)。

此命令将加密密钥（Encryption Key）从控制面板（CP）传输到外设（PD）。

<a id="r_osdp_5Fcmd"></a>

```c
struct osdp_cmd
```

相关声明：[osdp_cmd](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md)。

开放监控设备协议（OSDP）的命令结构。

<a id="r_osdp_5Fevent_5Fcardread"></a>

```c
struct osdp_event_cardread
```

相关声明：[osdp_event_cardread](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md)。

开放监控设备协议（OSDP）的读卡事件（Cardread）。

<a id="r_osdp_5Fevent_5Fkeypress"></a>

```c
struct osdp_event_keypress
```

相关声明：[osdp_event_keypress](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md)。

开放监控设备协议（OSDP）的键盘事件（Keypad）。

<a id="r_osdp_5Fevent"></a>

```c
struct osdp_event
```

相关声明：[osdp_event](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md)。

开放监控设备协议（OSDP）的事件结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_acfd9e52e3ca23e6ef3d1cb55a0fa5714"></a>

```c
#define OSDP_CMD_TEXT_MAX_LEN 32
```

相关声明：[OSDP_CMD_TEXT_MAX_LEN](#acfd9e52e3ca23e6ef3d1cb55a0fa5714)。

文本命令中文本的最大长度。

<a id="r_a04a0aa00cbe34e1723be1a4763f63e94"></a>

```c
#define OSDP_CMD_KEYSET_KEY_MAX_LEN 32
```

相关声明：[OSDP_CMD_KEYSET_KEY_MAX_LEN](#a04a0aa00cbe34e1723be1a4763f63e94)。

密钥设置（Keyset）命令中密钥数据的最大长度。

<a id="r_af531800483155468768b89d20c3377d6"></a>

```c
#define OSDP_EVENT_MAX_DATALEN 64
```

相关声明：[OSDP_EVENT_MAX_DATALEN](#af531800483155468768b89d20c3377d6)。

事件数据的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 20.3\_类型定义（Typedefs）

<a id="r_a6a71149ab51996f345c20ad34d725803"></a>

```c
typedef int(* pd_command_callback_t) (void *arg, struct osdp_cmd *cmd)
```

相关声明：[pd_command_callback_t](#a6a71149ab51996f345c20ad34d725803)、[osdp_cmd](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

外设（PD）命令通知的回调。

<a id="r_aa02ec1fa8d7da5d694d5c2ae163e03cd"></a>

```c
typedef int(* cp_event_callback_t) (void *arg, int pd, struct osdp_event *ev)
```

相关声明：[cp_event_callback_t](#aa02ec1fa8d7da5d694d5c2ae163e03cd)、[osdp_event](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md)。

控制面板（CP）事件通知的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.4\_枚举（Enumerations）

<a id="r_a97ee0d8eb19e4e37ac89b2b6d338b84e"></a>

```c
enum osdp_led_color_e { OSDP_LED_COLOR_NONE , OSDP_LED_COLOR_RED , OSDP_LED_COLOR_GREEN , OSDP_LED_COLOR_AMBER , OSDP_LED_COLOR_BLUE , OSDP_LED_COLOR_SENTINEL }
```

相关声明：[osdp_led_color_e](#a97ee0d8eb19e4e37ac89b2b6d338b84e)、[OSDP_LED_COLOR_NONE](#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7)、[OSDP_LED_COLOR_RED](#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584)、[OSDP_LED_COLOR_GREEN](#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4)、[OSDP_LED_COLOR_AMBER](#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c)、[OSDP_LED_COLOR_BLUE](#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66)、[OSDP_LED_COLOR_SENTINEL](#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a)。

OSDP 为 `on_color`/`off_color` 参数规定的 LED 颜色。

<a id="r_abd8555e895d9370da1400f76c931ba21"></a>

```c
enum osdp_cmd_e { OSDP_CMD_OUTPUT = 1 , OSDP_CMD_LED , OSDP_CMD_BUZZER , OSDP_CMD_TEXT , OSDP_CMD_KEYSET , OSDP_CMD_COMSET , OSDP_CMD_SENTINEL }
```

相关声明：[osdp_cmd_e](#abd8555e895d9370da1400f76c931ba21)、[OSDP_CMD_OUTPUT](#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b)、[OSDP_CMD_LED](#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42)、[OSDP_CMD_BUZZER](#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03)、[OSDP_CMD_TEXT](#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01)、[OSDP_CMD_KEYSET](#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f)、[OSDP_CMD_COMSET](#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289)、[OSDP_CMD_SENTINEL](#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea)。

OSDP 向应用程序公开的命令。

<a id="r_a976512dfb1a4dc3ea9326d72a0abb5e7"></a>

```c
enum osdp_event_cardread_format_e { OSDP_CARD_FMT_RAW_UNSPECIFIED , OSDP_CARD_FMT_RAW_WIEGAND , OSDP_CARD_FMT_ASCII , OSDP_CARD_FMT_SENTINEL }
```

相关声明：[osdp_event_cardread_format_e](#a976512dfb1a4dc3ea9326d72a0abb5e7)、[OSDP_CARD_FMT_RAW_UNSPECIFIED](#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471)、[OSDP_CARD_FMT_RAW_WIEGAND](#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e)、[OSDP_CARD_FMT_ASCII](#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059)、[OSDP_CARD_FMT_SENTINEL](#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1)。

PD 可支持的各种卡格式（Card formats）。

<a id="r_a81548fab575d89f66b45a5d4ac85984d"></a>

```c
enum osdp_event_type { OSDP_EVENT_CARDREAD , OSDP_EVENT_KEYPRESS , OSDP_EVENT_SENTINEL }
```

相关声明：[osdp_event_type](#a81548fab575d89f66b45a5d4ac85984d)、[OSDP_EVENT_CARDREAD](#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250)、[OSDP_EVENT_KEYPRESS](#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c)、[OSDP_EVENT_SENTINEL](#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47)。

OSDP 外设（PD）事件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.5\_函数（Functions）

<a id="func-members-0"></a>

### 外设模式 API（Peripheral Device mode APIs）

注意：仅在启用 `CONFIG_OSDP_MODE_PD` 时可用。

<a id="r_aa79d4fde3ae007e6c829d56daf8c3e49"></a>

```c
void osdp_pd_set_command_callback (pd_command_callback_t cb, void *arg)
```

相关声明：[osdp_pd_set_command_callback](#aa79d4fde3ae007e6c829d56daf8c3e49)、[pd_command_callback_t](#a6a71149ab51996f345c20ad34d725803)。

设置 PD 命令通知的回调方法。

<a id="r_ac097208c2b197ec4ebe567d59831a29f"></a>

```c
int osdp_pd_notify_event (const struct osdp_event *event)
```

相关声明：[osdp_pd_notify_event](#ac097208c2b197ec4ebe567d59831a29f)、[osdp_event](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md)。

向 CP 通知 PD 事件的 API。

<a id="func-members-1"></a>

### OSDP 安全通道 API（Secure Channel APIs）

注意：仅在启用 `CONFIG_OSDP_SC_ENABLED` 时可用。

<a id="r_ab1335ca06ebddff18873971e4dc03c40"></a>

```c
uint32_t osdp_get_sc_status_mask (void)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[osdp_get_sc_status_mask](#ab1335ca06ebddff18873971e4dc03c40)。

获取当前安全通道（Secure Channel，SC）状态掩码。

## 20.6\_详细说明（Detailed Documentation）

<a id="a04a0aa00cbe34e1723be1a4763f63e94"></a>

### `OSDP_CMD_KEYSET_KEY_MAX_LEN`

```c
#define OSDP_CMD_KEYSET_KEY_MAX_LEN 32
```

密钥设置（Keyset）命令中密钥数据的最大长度。

<a id="acfd9e52e3ca23e6ef3d1cb55a0fa5714"></a>

### `OSDP_CMD_TEXT_MAX_LEN`

```c
#define OSDP_CMD_TEXT_MAX_LEN 32
```

文本命令中文本的最大长度。

<a id="af531800483155468768b89d20c3377d6"></a>

### `OSDP_EVENT_MAX_DATALEN`

```c
#define OSDP_EVENT_MAX_DATALEN 64
```

事件数据的最大长度。

<a id="aa02ec1fa8d7da5d694d5c2ae163e03cd"></a>

### `cp_event_callback_t`

```c
typedef int(* cp_event_callback_t) (void *arg, int pd, struct osdp_event *ev)
```

控制面板（CP）事件通知的回调。

使用 `osdp_cp_set_event_callback` 注册后，当 CP 收到 PD 事件时调用此方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `arg` | 应用程序在注册回调时提供的不透明指针（Opaque pointer）。 |
| `pd` | 此 PD 在 Kconfig `OSDP_PD_ADDRESS_LIST` 中的偏移量，从 0 开始计数。 |
| `ev` | 指向 `osdp_event` 结构体的指针，由 libosdp 填充。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功处理事件时。 |
| `-ve` | 发生错误时。 |

<a id="a6a71149ab51996f345c20ad34d725803"></a>

### `pd_command_callback_t`

```c
typedef int(* pd_command_callback_t) (void *arg, struct osdp_cmd *cmd)
```

外设（PD）命令通知的回调。

使用 `osdp_pd_set_command_callback` 注册后，当 PD 收到 CP 命令时调用此方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `arg` | 此前传给 `osdp_pd_set_command_callback` 的 `arg` 参数的指针。 |
| `cmd` | 指向所接收命令的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | LibOSDP 必须发送 `osdp_ACK` 响应时。 |
| `-ve` | LibOSDP 必须发送 `osdp_NAK` 响应时。 |
| `+ve` | 若 LibOSDP 必须发送特定响应，还需修改传入的 `struct osdp_cmd *cmd`。这适用于发送制造商专用回复 `osdp_MFGREP`。 |

<a id="abd8555e895d9370da1400f76c931ba21"></a>

### `osdp_cmd_e`

```c
enum osdp_cmd_e
```

OSDP 向应用程序公开的命令。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OSDP_CMD_OUTPUT` | 输出控制命令（Output control command）。 |
| `OSDP_CMD_LED` | 读卡器 LED 控制命令。 |
| `OSDP_CMD_BUZZER` | 读卡器蜂鸣器控制命令。 |
| `OSDP_CMD_TEXT` | 读卡器文本输出命令。 |
| `OSDP_CMD_KEYSET` | 加密密钥设置命令（Encryption Key Set Command）。 |
| `OSDP_CMD_COMSET` | PD 通信配置命令（Communication Configuration Command）。 |
| `OSDP_CMD_SENTINEL` | 最大命令值。 |

<a id="a976512dfb1a4dc3ea9326d72a0abb5e7"></a>

### `osdp_event_cardread_format_e`

```c
enum osdp_event_cardread_format_e
```

PD 可支持的各种卡格式（Card formats）。

PD 需要报告一次读卡时，将此内容发送给 CP。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OSDP_CARD_FMT_RAW_UNSPECIFIED` | 未指定卡格式（Unspecified card format）。 |
| `OSDP_CARD_FMT_RAW_WIEGAND` | 韦根（Wiegand）卡格式。 |
| `OSDP_CARD_FMT_ASCII` | ASCII 卡格式。 |
| `OSDP_CARD_FMT_SENTINEL` | 最大卡格式值。 |

<a id="a81548fab575d89f66b45a5d4ac85984d"></a>

### `osdp_event_type`

```c
enum osdp_event_type
```

OSDP 外设（PD）事件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OSDP_EVENT_CARDREAD` | 读卡事件（Card read event）。 |
| `OSDP_EVENT_KEYPRESS` | 键盘按键事件（Keypad press event）。 |
| `OSDP_EVENT_SENTINEL` | 最大事件值。 |

<a id="a97ee0d8eb19e4e37ac89b2b6d338b84e"></a>

### `osdp_led_color_e`

```c
enum osdp_led_color_e
```

OSDP 为 `on_color`/`off_color` 参数规定的 LED 颜色。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OSDP_LED_COLOR_NONE` | 无颜色（No color）。 |
| `OSDP_LED_COLOR_RED` | 红色（Red）。 |
| `OSDP_LED_COLOR_GREEN` | 绿色（Green）。 |
| `OSDP_LED_COLOR_AMBER` | 琥珀色（Amber）。 |
| `OSDP_LED_COLOR_BLUE` | 蓝色（Blue）。 |
| `OSDP_LED_COLOR_SENTINEL` | 最大值。 |

<a id="ab1335ca06ebddff18873971e4dc03c40"></a>

### `osdp_get_sc_status_mask()`

```c
uint32_t osdp_get_sc_status_mask ( void )
```

获取当前安全通道（Secure Channel，SC）状态掩码。

**返回（Returns）**：返回值：安全通道（SC）状态掩码。

<a id="ac097208c2b197ec4ebe567d59831a29f"></a>

### `osdp_pd_notify_event()`

```c
int osdp_pd_notify_event ( const struct osdp_event * event)
```

向 CP 通知 PD 事件的 API。

这些事件作为 `POLL` 命令的替代响应发送给 CP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | 指向事件结构体的指针，必须由应用程序填充。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-1` | 失败。 |

<a id="aa79d4fde3ae007e6c829d56daf8c3e49"></a>

### `osdp_pd_set_command_callback()`

```c
void osdp_pd_set_command_callback ( pd_command_callback_t cb, void * arg )
```

设置 PD 命令通知的回调方法。

当 PD 收到 CP 命令时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调函数指针。 |
| `arg` | 将作为 `cb` 第一个参数传入的指针。 |


## 20.7\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [osdp_cmd_output](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md)
- [osdp_cmd_led_params](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md)
- [osdp_cmd_led](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md)
- [osdp_cmd_buzzer](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md)
- [osdp_cmd_text](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md)
- [osdp_cmd_comset](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md)
- [osdp_cmd_keyset](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md)
- [osdp_cmd](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md)
- [osdp_event_cardread](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md)
- [osdp_event_keypress](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md)
- [osdp_event](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [CONFIG_OSDP_MODE_PD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP_MODE_PD)
- [CONFIG_OSDP_SC_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP_SC_ENABLED)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b"></a>
<a id="abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42"></a>
<a id="abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03"></a>
<a id="abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01"></a>
<a id="abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f"></a>
<a id="abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289"></a>
<a id="abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea"></a>
<a id="a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471"></a>
<a id="a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e"></a>
<a id="a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059"></a>
<a id="a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1"></a>
<a id="a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250"></a>
<a id="a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c"></a>
<a id="a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66"></a>
<a id="a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_zephyr__drivers__mux.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__peci.h_头文件参考.md)
