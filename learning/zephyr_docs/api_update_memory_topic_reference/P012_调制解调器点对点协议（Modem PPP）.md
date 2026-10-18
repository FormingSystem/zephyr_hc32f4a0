---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-12
title: 调制解调器点对点协议（Modem PPP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_调制解调器点对点协议（Modem PPP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器点对点协议（Modem PPP）

<a id="details"></a>

调制解调器点对点协议（Modem PPP）。**引入版本（Since）：**3.5。**版本（Version）：**1.0.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_ga5b38e57b13e8a00217bc64bbe69a595e"></a>

```c
#define MODEM_DEV_PPP_DEFINE(_dev, _name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_DEV_PPP_DEFINE](#ga5b38e57b13e8a00217bc64bbe69a595e)。

定义调制解调器点对点协议（modem PPP）模块，并将其绑定到网络接口。

<a id="r_gaeec331b2d9bccf4f5729e987b4ecf87e"></a>

```c
#define MODEM_DT_INST_PPP_DEFINE(inst, _name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_DT_INST_PPP_DEFINE](#gaeec331b2d9bccf4f5729e987b4ecf87e)。

为蜂窝设备树实例定义调制解调器 PPP 模块。

<a id="r_ga4dbed2a468d0b2c436e2d39e621ec245"></a>

```c
#define MODEM_PPP_DEFINE(_name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_PPP_DEFINE](#ga4dbed2a468d0b2c436e2d39e621ec245)。

定义不带设备的调制解调器 PPP 模块，并将其绑定到网络接口。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.2\_类型定义（Typedefs）

<a id="r_gafdd04a06c32e9ab70755d4f2e68deaad"></a>

```c
typedef void(* modem_ppp_init_iface) (struct net_if *iface)
```

相关声明：[modem_ppp_init_iface](#gafdd04a06c32e9ab70755d4f2e68deaad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

第二层（L2）网络接口初始化回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_gad3ce02dd0a6cf7067c5ca0341f807f88"></a>

```c
int modem_ppp_attach (struct modem_ppp *ppp, struct modem_pipe *pipe)
```

相关声明：[modem_ppp_attach](#gad3ce02dd0a6cf7067c5ca0341f807f88)。

将管道（pipe）附接到实例并连接。

<a id="r_gaebb69341b2b88338b2cfccaa1c0cba0b"></a>

```c
struct net_if * modem_ppp_get_iface (struct modem_ppp *ppp)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[modem_ppp_get_iface](#gaebb69341b2b88338b2cfccaa1c0cba0b)。

获取调制解调器 PPP 实例绑定的网络接口。

<a id="r_gaf2177b83100647ed0894cac7fa435cb3"></a>

```c
void modem_ppp_release (struct modem_ppp *ppp)
```

相关声明：[modem_ppp_release](#gaf2177b83100647ed0894cac7fa435cb3)。

从实例释放管道。

## 12.4\_详细说明（Detailed Documentation）

<a id="ga5b38e57b13e8a00217bc64bbe69a595e"></a>

### `MODEM_DEV_PPP_DEFINE`

```c
#define MODEM_DEV_PPP_DEFINE ( _dev, _name, _init_iface, _mtu, _buf_size )
```

```c
#include <zephyr/modem/ppp.h>
```

展开值（Value）：

```c
extern const struct ppp_api modem_ppp_ppp_api;                                             \
                                                                                           \
static uint8_t _CONCAT(_name, _receive_buf)[_buf_size];                                    \
static uint8_t _CONCAT(_name, _transmit_buf)[_buf_size];                                   \
                                                                                           \
static struct modem_ppp _name = {                                                          \
        .init_iface = _init_iface,                                                         \
        .receive_buf = _CONCAT(_name, _receive_buf),                                       \
        .transmit_buf = _CONCAT(_name, _transmit_buf),                                     \
        .buf_size = _buf_size,                                                             \
};                                                                                         \
static const struct modem_ppp_config _CONCAT(_name, _config) = {                           \
        .dev = _dev,                                                                       \
};                                                                                         \
                                                                                           \
NET_DEVICE_INIT(_CONCAT(ppp_net_dev_, _name), "modem_ppp_" #_name,                         \
                modem_ppp_init_internal, NULL, &_name, &_CONCAT(_name, _config),           \
                CONFIG_KERNEL_INIT_PRIORITY_DEFAULT,                                       \
                &modem_ppp_ppp_api, PPP_L2, NET_L2_GET_CTX_TYPE(PPP_L2), _mtu)
```

定义调制解调器点对点协议（modem PPP）模块，并将其绑定到网络接口。

本宏定义 `modem_ppp` 实例，初始化 PPP 二层（L2）网络设备实例，并将 `modem_ppp` 实例绑定到该 PPP L2 实例。

若提供底层蜂窝设备（Cellular Device），PPP 接口将在启动和停止 PPP 时管理该蜂窝设备的电源状态（Power State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 用于电源管理（Power Management）的蜂窝设备实例；不使用时设为 `NULL`。 |
| `_name` | 静态定义的 `modem_ppp` 实例名称。 |
| `_init_iface` | PPP 二层（L2）网络接口初始化函数的钩子（Hook）。 |
| `_mtu` | PPP 二层（L2）网络接口收发的 `net_pkt` 数据最大大小。 |
| `_buf_size` | PPP 部分帧（Partial Frame）发送和接收缓冲区的大小。 |

<a id="gaeec331b2d9bccf4f5729e987b4ecf87e"></a>

### `MODEM_DT_INST_PPP_DEFINE`

```c
#define MODEM_DT_INST_PPP_DEFINE ( inst, _name, _init_iface, _mtu, _buf_size )
```

```c
#include <zephyr/modem/ppp.h>
```

展开值（Value）：

```c
MODEM_DEV_PPP_DEFINE(DEVICE_DT_INST_GET(inst), _name, _init_iface, _mtu, _buf_size)
```

为蜂窝设备树实例定义调制解调器 PPP 模块。

**参阅（See Also）**：**另请参见（See Also）：**`MODEM_DEV_PPP_DEFINE`。

<a id="ga4dbed2a468d0b2c436e2d39e621ec245"></a>

### `MODEM_PPP_DEFINE`

```c
#define MODEM_PPP_DEFINE ( _name, _init_iface, _mtu, _buf_size )
```

```c
#include <zephyr/modem/ppp.h>
```

展开值（Value）：

```c
MODEM_DEV_PPP_DEFINE(NULL, _name, _init_iface, _mtu, _buf_size)
```

定义不带设备的调制解调器 PPP 模块，并将其绑定到网络接口。

**参阅（See Also）**：**另请参见（See Also）：**`MODEM_DEV_PPP_DEFINE`。

<a id="gafdd04a06c32e9ab70755d4f2e68deaad"></a>

### `modem_ppp_init_iface`

```c
typedef void(* modem_ppp_init_iface) (struct net_if *iface)
```

```c
#include <zephyr/modem/ppp.h>
```

第二层（L2）网络接口初始化回调。

<a id="gad3ce02dd0a6cf7067c5ca0341f807f88"></a>

### `modem_ppp_attach()`

```c
int modem_ppp_attach ( struct modem_ppp * ppp, struct modem_pipe * pipe )
```

```c
#include <zephyr/modem/ppp.h>
```

将管道（pipe）附接到实例并连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `PPP L2/driver Support Functions` | 调制解调器 PPP 实例（Modem PPP Instance）。 |
| `pipe` | 要附接到调制解调器 PPP 实例的管道（Pipe）。 |

<a id="gaebb69341b2b88338b2cfccaa1c0cba0b"></a>

### `modem_ppp_get_iface()`

```c
struct net_if * modem_ppp_get_iface ( struct modem_ppp * ppp)
```

```c
#include <zephyr/modem/ppp.h>
```

获取调制解调器 PPP 实例绑定的网络接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `PPP L2/driver Support Functions` | 调制解调器 PPP 实例（Modem PPP Instance）。 |

**返回（Returns）**：**返回值（Returns）：**调制解调器 PPP 实例所绑定的网络接口指针。

<a id="gaf2177b83100647ed0894cac7fa435cb3"></a>

### `modem_ppp_release()`

```c
void modem_ppp_release ( struct modem_ppp * ppp)
```

```c
#include <zephyr/modem/ppp.h>
```

从实例释放管道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `PPP L2/driver Support Functions` | 调制解调器 PPP 实例（Modem PPP Instance）。 |


## 12.5\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/modem/ppp.h](../api_file_system_device_reference/P027_zephyr__modem__ppp.h_文件参考.md)
- [ppp_api](../network_service_model_reference/P042_ppp_api_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [DEVICE_DT_INST_GET](../device_reference/P001_设备模型公共接口.md#ga9165e550ae175ce305eafe33390af78b)
- [点对点协议二层/驱动支持函数（PPP L2/driver Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructppp__api_html"></a>
<a id="agroup__device__model_html_ga9165e550ae175ce305eafe33390af78b"></a>
<a id="agroup__modem__ppp_html_ga5b38e57b13e8a00217bc64bbe69a595e"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_内存组（Memory Banks）的驱动API。.md) · [返回大纲](大纲.md) · [下一章](P013_PAC194X API主题.md)
