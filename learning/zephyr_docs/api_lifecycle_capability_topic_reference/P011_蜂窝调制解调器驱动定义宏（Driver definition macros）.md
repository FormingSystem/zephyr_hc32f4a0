---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-11
title: 蜂窝调制解调器驱动定义宏（Driver definition macros）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_蜂窝调制解调器驱动定义宏（Driver definition macros）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

定义使用蜂窝调制解调器驱动的设备实例。

<a id="details"></a>

定义使用蜂窝调制解调器驱动（Cellular Modem Driver）的设备实例。完整的树外驱动（Out-of-tree Driver）示例参见蜂窝调制解调器文档。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_modem_5Fcellular_5Fboard_5Finit"></a>

```c
struct modem_cellular_board_init
```

相关声明：[modem_cellular_board_init](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md)。

将开发板提供的初始化脚本（Init Script）绑定到调制解调器实例的描述符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ga5cf681cc8970ee193b960d5e964aee32"></a>

```c
#define MODEM_CELLULAR_INST_NAME(name, inst)
```

相关声明：[MODEM_CELLULAR_INST_NAME](#ga5cf681cc8970ee193b960d5e964aee32)。

为调制解调器实例对象（Modem Instance Object）生成唯一的 C 标识符。

<a id="r_gab6cc63dc914ee95542a0b5a4a2ebd7f9"></a>

```c
#define MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES(inst, ...)
```

相关声明：[MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES](#gab6cc63dc914ee95542a0b5a4a2ebd7f9)。

为调制解调器实例定义额外的 CMUX 用户管道（User Pipes）。

<a id="r_gac2990fadd342efc0394ec7dadb8e3c82"></a>

```c
#define MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE](#gac2990fadd342efc0394ec7dadb8e3c82)。

定义多重匹配对象（Multiple Match Object），预期先收到一个响应，再收到 `OK`。

<a id="r_gacc9e3af4dacf62f956f68839eefc6862"></a>

```c
#define MODEM_CELLULAR_COMMON_CHAT_MATCHES()
```

相关声明：[MODEM_CELLULAR_COMMON_CHAT_MATCHES](#gacc9e3af4dacf62f956f68839eefc6862)。

定义蜂窝调制解调器脚本使用的通用聊天匹配项（Chat Matches）。

<a id="r_ga4fd2f91635f03a6e1fa4a0bddc7c7cdf"></a>

```c
#define MODEM_CELLULAR_COMMON_UNSOL_MATCHES
```

相关声明：[MODEM_CELLULAR_COMMON_UNSOL_MATCHES](#ga4fd2f91635f03a6e1fa4a0bddc7c7cdf)。

展开为通用非请求响应匹配项（Unsolicited Response Matches）。

<a id="r_ga4b61e995f86377dfbab0ca81d1efe492"></a>

```c
#define MODEM_CELLULAR_DEFINE_INSTANCE(inst, vendor_config, _vendor_specific)
```

相关声明：[MODEM_CELLULAR_DEFINE_INSTANCE](#ga4b61e995f86377dfbab0ca81d1efe492)。

定义蜂窝调制解调器设备实例（Cellular Modem Device Instance）。

<a id="r_ga5b16137fbab1b7199075e88422a0b9b4"></a>

```c
#define MODEM_CELLULAR_BOARD_INIT_DEFINE(node_id, _script)
```

相关声明：[MODEM_CELLULAR_BOARD_INIT_DEFINE](#ga5b16137fbab1b7199075e88422a0b9b4)。

为调制解调器实例注册开发板专用初始化脚本（Board-specific Init Script）。

## 11.3\_详细说明（Detailed Documentation）

<a id="ga5b16137fbab1b7199075e88422a0b9b4"></a>

### `MODEM_CELLULAR_BOARD_INIT_DEFINE`

```c
#define MODEM_CELLULAR_BOARD_INIT_DEFINE ( node_id, _script )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

为调制解调器实例注册开发板专用初始化脚本（Board-specific Init Script）。

此脚本在 CMUX 建立后、APN 和网络配置之前，通过 AT 控制通道（Control Channel）运行。驱动提供用于推进连接序列（Connect Sequence）的完成回调，因此不使用脚本自身的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 调制解调器实例（Modem Instance）的设备树节点标识符（Devicetree Node Identifier）。 |
| `_script` | 指向由 `MODEM_CHAT_SCRIPT_DEFINE` 定义的 `modem_chat_script` 的指针。 |

<a id="gacc9e3af4dacf62f956f68839eefc6862"></a>

### `MODEM_CELLULAR_COMMON_CHAT_MATCHES`

```c
#define MODEM_CELLULAR_COMMON_CHAT_MATCHES ( )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
MODEM_CHAT_MATCH_DEFINE(ok_match, "OK", "", NULL);                                         \
MODEM_CHAT_MATCHES_DEFINE(__maybe_unused allow_match,                                      \
                          MODEM_CHAT_MATCH("OK", "", NULL),                                \
                          MODEM_CHAT_MATCH("ERROR", "", NULL));                            \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused imei_match,                             \
                        "", "", modem_cellular_chat_on_imei);                              \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgsn_sn_match,                          \
                        "", "", modem_cellular_chat_on_cgsn_sn);                           \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgsn_imei_match,                        \
                        "+CGSN: ", "", modem_cellular_chat_on_cgsn_imei);                  \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmm_match,                             \
                        "", "", modem_cellular_chat_on_cgmm);                              \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused csq_match,                              \
                        "+CSQ: ", ",", modem_cellular_chat_on_csq);                        \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cesq_match,                             \
                        "+CESQ: ", ",", modem_cellular_chat_on_cesq);                      \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused qccid_match,                            \
                        "+QCCID: ", "", modem_cellular_chat_on_iccid);                     \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused iccid_match,                            \
                        "+ICCID: ", "", modem_cellular_chat_on_iccid);                     \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused ccid_match,                             \
                        "+CCID: ", "", modem_cellular_chat_on_iccid);                      \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cimi_match,                             \
                        "", "", modem_cellular_chat_on_imsi);                              \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmi_match,                             \
                        "", "", modem_cellular_chat_on_cgmi);                              \
MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmr_match,                             \
                        "", "", modem_cellular_chat_on_cgmr);                              \
MODEM_CHAT_MATCH_DEFINE(connect_match __maybe_unused,                                      \
                        "CONNECT", "", NULL);                                              \
MODEM_CHAT_MATCHES_DEFINE(__maybe_unused abort_matches,                                    \
                          MODEM_CHAT_MATCH("ERROR", "", NULL));                            \
MODEM_CHAT_MATCHES_DEFINE(__maybe_unused dial_abort_matches,                               \
                          MODEM_CHAT_MATCH("ERROR", "", NULL),                             \
                          MODEM_CHAT_MATCH("BUSY", "", NULL),                              \
                          MODEM_CHAT_MATCH("NO ANSWER", "", NULL),                         \
                          MODEM_CHAT_MATCH("NO CARRIER", "", NULL),                        \
                          MODEM_CHAT_MATCH("NO DIALTONE", "", NULL))
```

定义蜂窝调制解调器脚本使用的通用聊天匹配项（Chat Matches）。

在文件作用域（File Scope）调用此宏一次。它为命令成功、常见命令失败、调制解调器身份和信号查询，以及 PPP 拨号响应定义匹配项（Matches）。生成的标识符供该调制解调器的 `modem_cellular_config_scripts` 使用。

<a id="ga4fd2f91635f03a6e1fa4a0bddc7c7cdf"></a>

### `MODEM_CELLULAR_COMMON_UNSOL_MATCHES`

```c
#define MODEM_CELLULAR_COMMON_UNSOL_MATCHES
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
MODEM_CHAT_MATCH("+CREG: ", ",", modem_cellular_chat_on_cxreg),                            \
MODEM_CHAT_MATCH("+CEREG: ", ",", modem_cellular_chat_on_cxreg),                           \
MODEM_CHAT_MATCH("+CGREG: ", ",", modem_cellular_chat_on_cxreg),                           \
MODEM_CHAT_MATCH("+CGEV: ", ",", modem_cellular_chat_on_cgev),                             \
MODEM_CHAT_MATCH("APP RDY", "", modem_cellular_chat_on_modem_ready),                       \
MODEM_CHAT_MATCH("Ready", "", modem_cellular_chat_on_modem_ready)
```

展开为通用非请求响应匹配项（Unsolicited Response Matches）。

在传递给 `MODEM_CHAT_MATCHES_DEFINE()` 的条目列表（Entry List）中使用此宏。厂商驱动可以在其展开内容之后追加条目。

<a id="gab6cc63dc914ee95542a0b5a4a2ebd7f9"></a>

### `MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES`

```c
#define MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES ( inst, ... )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
FOR_EACH_FIXED_ARG(MODEM_CELLULAR_DEFINE_USER_PIPE_DATA_HELPER,                            \
                   (;), inst, __VA_ARGS__);                                                \
MODEM_CELLULAR_DEFINE_USER_PIPES(                                                          \
        inst,                                                                              \
        FOR_EACH_FIXED_ARG(MODEM_CELLULAR_INIT_USER_PIPE_HELPER,                           \
                           (,), inst, __VA_ARGS__)                                         \
);
```

为调制解调器实例定义额外的 CMUX 用户管道（User Pipes）。

每个可变参数（Variadic Argument）都是带括号的 `(name, dlci_address)` 对。此宏定义 `MODEM_CELLULAR_DEFINE_INSTANCE` 使用的接收缓冲区、管道链接（Pipe Links）和用户管道数组（User-pipe Array）。应在调用 `MODEM_CELLULAR_DEFINE_INSTANCE` 之前，为每个调制解调器实例调用一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |
| `...` | 一个或多个 `(name, dlci_address)` 对。 |

<a id="ga4b61e995f86377dfbab0ca81d1efe492"></a>

### `MODEM_CELLULAR_DEFINE_INSTANCE`

```c
#define MODEM_CELLULAR_DEFINE_INSTANCE ( inst, vendor_config, _vendor_specific )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
BUILD_ASSERT(vendor_config != NULL, "vendor_config must be non-NULL");                     \
static const struct modem_cellular_config MODEM_CELLULAR_INST_NAME(config, inst) = {       \
        .uart = DEVICE_DT_GET(DT_INST_BUS(inst)),                                          \
        .vendor = vendor_config,                                                           \
        .vendor_specific = _vendor_specific,                                               \
        .ppp = &MODEM_CELLULAR_INST_NAME(ppp, inst),                                       \
        .power_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_power_gpios, {}),                 \
        .reset_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_reset_gpios, {}),                 \
        .wake_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_wake_gpios, {}),                   \
        .ring_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_ring_gpios, {}),                   \
        .dtr_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_dtr_gpios, {}),                     \
        .status_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_status_gpios, {}),               \
        .autostarts = DT_INST_PROP(inst, autostarts),                                      \
        .hold_reset_on_suspend =                                                           \
                DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior, hold_on_suspend),  \
        .reset_on_resume = DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior,         \
                                                    toggle_on_resume),                     \
        .reset_on_recovery = DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior,       \
                                                    toggle_on_recovery),                   \
        .cmux_enable_runtime_power_save =                                                  \
                DT_INST_PROP_OR(inst, cmux_enable_runtime_power_save, 0),                  \
        .cmux_close_pipe_on_power_save =                                                   \
                DT_INST_PROP_OR(inst, cmux_close_pipe_on_power_save, 0),                   \
        .cmux_no_powersave_handshake =                                                     \
                DT_INST_PROP_OR(inst, cmux_no_powersave_handshake, 0),                     \
        .use_default_pdp_context = DT_INST_PROP_OR(inst, zephyr_use_default_pdp_ctx, 0),   \
        .use_default_apn = DT_INST_PROP_OR(inst, zephyr_use_default_apn, 0),               \
        .cmux_idle_timeout = K_MSEC(DT_INST_PROP_OR(inst, cmux_idle_timeout_ms, 0)),       \
        .user_pipes = MODEM_CELLULAR_GET_USER_PIPES(inst),                                 \
        .user_pipes_size = ARRAY_SIZE(MODEM_CELLULAR_GET_USER_PIPES(inst)),                \
};                                                                                         \
                                                                                           \
PM_DEVICE_DT_INST_DEFINE(inst, modem_cellular_pm_action);                                  \
                                                                                           \
DEVICE_DT_INST_DEFINE(inst, modem_cellular_init, PM_DEVICE_DT_INST_GET(inst),              \
                      &MODEM_CELLULAR_INST_NAME(data, inst),                               \
                      &MODEM_CELLULAR_INST_NAME(config, inst), POST_KERNEL,                \
                      CONFIG_MODEM_CELLULAR_INIT_PRIORITY, &modem_cellular_api);
```

定义蜂窝调制解调器设备实例（Cellular Modem Device Instance）。

此宏为设备树实例（Devicetree Instance）创建不可变设备配置（Immutable Device Configuration）、电源管理对象（Power-management Object）和 Zephyr 设备。调用前，需要定义该实例的 PPP 对象、初始化 `modem_cellular_data` 对象，并调用 `MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |
| `vendor_config` | 指向常量 `modem_cellular_vendor_config` 对象的指针。不得为 `NULL`，且必须在设备整个生命周期（Lifetime）内保持有效。 |
| `_vendor_specific` | 指向任意厂商专用配置结构体（Vendor-specific Configuration Structure）的指针，可以为 `NULL`。 |

<a id="ga5cf681cc8970ee193b960d5e964aee32"></a>

### `MODEM_CELLULAR_INST_NAME`

```c
#define MODEM_CELLULAR_INST_NAME ( name, inst )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
CONCAT(name, _, DT_DRV_COMPAT, inst)
```

为调制解调器实例对象（Modem Instance Object）生成唯一的 C 标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 基础对象名称（Base Object Name）。 |
| `inst` | 设备树实例编号。 |

**返回（Returns）**：**返回值（Returns）：**生成的 C 标识符（Identifier）。

<a id="gac2990fadd342efc0394ec7dadb8e3c82"></a>

### `MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE`

```c
#define MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE ( _sym, _match, _separators, _callback )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

展开值（Value）：

```c
MODEM_CHAT_MATCHES_DEFINE(_sym,                                                            \
        MODEM_CHAT_MATCH_INITIALIZER(_match, _separators, _callback, false, true),         \
        MODEM_CHAT_MATCH("OK", "", NULL))
```

定义多重匹配对象（Multiple Match Object），预期先收到一个响应，再收到 `OK`。

替代先调用 `MODEM_CHAT_MATCH_DEFINE`、再调用 `MODEM_CHAT_SCRIPT_CMD_RESP("", ok_match)` 的写法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_sym` | 匹配数组对象（Matches Array Object）的名称。 |
| `_match` | 按 `MODEM_CHAT_MATCH_DEFINE` 规定使用的匹配字符串（Match String）。 |
| `_separators` | 按 `MODEM_CHAT_MATCH_DEFINE` 规定使用的分隔符字符串（Separators String）。 |
| `_callback` | 按 `MODEM_CHAT_MATCH_DEFINE` 规定在匹配时调用的回调（Callback on Match）。 |


## 11.4\_原页交叉引用（Cross References）

- [modem_cellular_board_init](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md)
- [zephyr/drivers/modem/modem_cellular.h](../api_file_network_device_reference/P024_zephyr__drivers__modem__modem_cellular.h_文件参考.md)
- [modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)
- [MODEM_CHAT_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga926b0d2993eb8158137e2caa7687abb8)
- [MODEM_CHAT_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga078fd13acc9abcc0e0aa0304e6a8537a)
- [modem_cellular_config_scripts](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md)
- [MODEM_CHAT_MATCHES_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga216094ddd94351fadf0e84bacbadc84e)
- [FOR_EACH_FIXED_ARG](../util_reference/P001_通用工具公共接口.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_INST_BUS](../dt_instance_reference/P001_设备树驱动实例宏.md#gacecb46743315738dcd9a0765ea78276a)
- [GPIO_DT_SPEC_INST_GET_OR](../hardware/P266_GPIO公共接口.md#gae6b4a354c3cf0e042a390aac4bc37c69)
- [DT_INST_PROP](../dt_instance_reference/P001_设备树驱动实例宏.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)
- [DT_INST_ENUM_HAS_VALUE](../dt_instance_reference/P001_设备树驱动实例宏.md#ga80b0321efd592a63e39400e5327bb601)
- [DT_INST_PROP_OR](../dt_instance_reference/P001_设备树驱动实例宏.md#gaa51bd8f5b016244e0256b3ed9aceee7f)
- [K_MSEC](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [PM_DEVICE_DT_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga52892f2c34f6ccc9598002625baf12ce)
- [modem_cellular_data](../modem_wireless_model_reference/P050_modem_cellular_data_结构体.md)
- [modem_cellular_vendor_config](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md)
- [CONCAT](../util_reference/P001_通用工具公共接口.md#ga770b921e59b3151931ee939a1ecf450e)
- [MODEM_CHAT_MATCH_INITIALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa62ca91615d0b93b0d2adbcf6c78e251)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__modem__chat_html_ga078fd13acc9abcc0e0aa0304e6a8537a"></a>
<a id="agroup__modem__chat_html_ga926b0d2993eb8158137e2caa7687abb8"></a>
<a id="agroup__sys-util_html_ga1a2b2aa21d7cc37f33e6a62abd2ae340"></a>
<a id="agroup__clock__apis_html_ga302af954e87b10a9b731f1ad07775e9f"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-inst_html_ga80b0321efd592a63e39400e5327bb601"></a>
<a id="agroup__devicetree-inst_html_ga9dce2e631b2a94804e8f2bcc76c6eff8"></a>
<a id="agroup__devicetree-inst_html_gaa51bd8f5b016244e0256b3ed9aceee7f"></a>
<a id="agroup__devicetree-inst_html_gacecb46743315738dcd9a0765ea78276a"></a>
<a id="agroup__gpio__interface_html_gae6b4a354c3cf0e042a390aac4bc37c69"></a>
<a id="agroup__modem__driver__macros_html_ga5cf681cc8970ee193b960d5e964aee32"></a>
<a id="agroup__subsys__pm__device_html_ga52892f2c34f6ccc9598002625baf12ce"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__sys-util_html_ga770b921e59b3151931ee939a1ecf450e"></a>
<a id="agroup__modem__chat_html_ga216094ddd94351fadf0e84bacbadc84e"></a>
<a id="agroup__modem__chat_html_gaa62ca91615d0b93b0d2adbcf6c78e251"></a>

---

[上一章](P010_页面淘汰算法 API（Eviction Algorithm APIs）.md) · [返回大纲](大纲.md) · [下一章](P012_播放器（Player）.md)
