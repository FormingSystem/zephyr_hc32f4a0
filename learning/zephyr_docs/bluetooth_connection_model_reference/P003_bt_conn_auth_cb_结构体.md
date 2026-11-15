---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-3
title: bt_conn_auth_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_conn\_auth\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

认证配对（Authenticated Pairing）回调结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

带认证的配对回调结构（Authenticated pairing callback structure）。注意（Note）：回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a92391a172e158a42966f410d732424a7"></a>

```c
enum bt_security_err(* pairing_accept )(struct bt_conn *conn, const struct bt_conn_pairing_feat *const feat)
```

相关声明：[bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)、[pairing_accept](#a92391a172e158a42966f410d732424a7)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_pairing_feat](P038_bt_conn_pairing_feat_结构体.md)。

查询是否继续传入的配对过程（Incoming pairing）。

<a id="r_a14074ca97fad6af4c58c43a00c503104"></a>

```c
void(* passkey_display )(struct bt_conn *conn, unsigned int passkey)
```

相关声明：[passkey_display](#a14074ca97fad6af4c58c43a00c503104)、[bt_conn](P002_bt_conn_结构体.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

向用户显示配对密钥（Passkey）。

<a id="r_af736a8808504fce22b95131818bad450"></a>

```c
void(* passkey_display_keypress )(struct bt_conn *conn, enum bt_conn_auth_keypress type)
```

相关声明：[passkey_display_keypress](#af736a8808504fce22b95131818bad450)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)。

配对期间接收配对密钥按键通知（Passkey Keypress Notification）。

<a id="r_a10f9d22c89c95a6f3ffe0016f92445c0"></a>

```c
void(* passkey_entry )(struct bt_conn *conn)
```

相关声明：[passkey_entry](#a10f9d22c89c95a6f3ffe0016f92445c0)、[bt_conn](P002_bt_conn_结构体.md)。

请求用户输入配对密钥（Passkey）。

<a id="r_a2bb6c10666d111f675fd6de5ff51410a"></a>

```c
void(* passkey_confirm )(struct bt_conn *conn, unsigned int passkey)
```

相关声明：[passkey_confirm](#a2bb6c10666d111f675fd6de5ff51410a)、[bt_conn](P002_bt_conn_结构体.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

请求用户确认配对密钥（Passkey）。

<a id="r_aec9f6256607ea2cd1ce1b4cdb3052b42"></a>

```c
void(* oob_data_request )(struct bt_conn *conn, struct bt_conn_oob_info *info)
```

相关声明：[oob_data_request](#aec9f6256607ea2cd1ce1b4cdb3052b42)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_oob_info](P037_bt_conn_oob_info_结构体.md)。

请求用户提供带外数据（Out of Band，OOB data）。

<a id="r_af6eb01c252ba3e32ff8bf583aa6ca0a4"></a>

```c
void(* cancel )(struct bt_conn *conn)
```

相关声明：[cancel](#af6eb01c252ba3e32ff8bf583aa6ca0a4)、[bt_conn](P002_bt_conn_结构体.md)。

取消当前用户请求（Ongoing user request）。

<a id="r_af4f7d3ee570b3472ee79b014be01f76e"></a>

```c
void(* pairing_confirm )(struct bt_conn *conn)
```

相关声明：[pairing_confirm](#af4f7d3ee570b3472ee79b014be01f76e)、[bt_conn](P002_bt_conn_结构体.md)。

请求确认传入的配对（Incoming pairing）。

<a id="r_ab6df1b1505dc22dd8dae0e946546c8bb"></a>

```c
void(* pincode_entry )(struct bt_conn *conn, bool highsec)
```

相关声明：[pincode_entry](#ab6df1b1505dc22dd8dae0e946546c8bb)、[bt_conn](P002_bt_conn_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

请求用户输入配对密钥（Passkey）。

<a id="r_a1be006307d1c9b6b13b4d35024f130e5"></a>

```c
uint32_t(* app_passkey )(struct bt_conn *conn)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[app_passkey](#a1be006307d1c9b6b13b4d35024f130e5)、[bt_conn](P002_bt_conn_结构体.md)。

允许应用提供配对所用的配对密钥（Passkey）。

## 3.2\_详细说明（Detailed Documentation）

<a id="a1be006307d1c9b6b13b4d35024f130e5"></a>

### `app_passkey`

```c
uint32_t(* bt_conn_auth_cb::app_passkey) (struct bt_conn *conn)
```

允许应用提供配对所用的配对密钥（Passkey）。

实现此回调后，应用可以提供配对密钥（Passkey），有效范围为 `0`–`999999`。应用应返回配对所用的密钥，或返回 `BT_PASSKEY_RAND` 以生成随机密钥。此回调仅用于蓝牙核心规范（Core Specification）第 3 卷 H 部分定义的配对密钥输入方法（Passkey Entry）。配对中的哪台设备显示密钥取决于设备的输入／输出能力（IO capabilities）；详情参见蓝牙核心规范 V6.0 第 3 卷 H 部分表 2.8。按该表判定能力时，只要此回调非 `NULL`，设备就具备显示能力（Display），无论回调返回指定密钥还是 `BT_PASSKEY_RAND`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |

**说明（Note）**：注意（Note）：使用此回调时，应用负责保证所使用的密钥随机且唯一（Random and unique keys）。

**返回（Returns）**：返回值（Returns）：配对所用的配对密钥（Passkey）；或返回 `BT_PASSKEY_RAND`，让主机（Host）生成随机密钥。

<a id="af6eb01c252ba3e32ff8bf583aa6ca0a4"></a>

### `cancel`

```c
void(* bt_conn_auth_cb::cancel) (struct bt_conn *conn)
```

取消当前用户请求（Ongoing user request）。

此回调通知应用，应取消此前的所有用户请求，包括配对密钥显示、输入或确认（Passkey display, entry or confirmation）。

此项可以设为 `NULL`；但只要提供了 `passkey_display`、`passkey_entry`、`passkey_confirm` 或 `pairing_confirm` 回调，就必须同时提供此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |

<a id="aec9f6256607ea2cd1ce1b4cdb3052b42"></a>

### `oob_data_request`

```c
void(* bt_conn_auth_cb::oob_data_request) (struct bt_conn *conn, struct bt_conn_oob_info *info)
```

请求用户提供带外数据（Out of Band，OOB data）。

调用此回调时，用户应提供带外数据（OOB data）。信息结构（Information structure）会指明所需数据。

对于低功耗安全连接带外配对（LE Secure Connections OOB pairing），用户应根据可用情况提供本地带外数据、远端带外数据或两者。应通过 `bt_le_oob_set_sc_data()` API 将相应值传给协议栈。

要支持带外配对（OOB pairing），必须将此回调设置为非 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |
| `info` | 带外配对信息（OOB pairing information）。 |

<a id="a92391a172e158a42966f410d732424a7"></a>

### `pairing_accept`

```c
enum bt_security_err(* bt_conn_auth_cb::pairing_accept) (struct bt_conn *conn, const struct bt_conn_pairing_feat *const feat)
```

查询是否继续传入的配对过程（Incoming pairing）。

每次收到传入的配对请求／响应（Pairing request/response）时，都会调用此回调，让应用决定是否允许配对继续。

将对等设备（Peer）发来的配对信息（Pairing info）传入，以辅助作出决定。

此回调是同步的（Synchronous），应用应立即返回响应值，否则可能影响配对时序。因此，不应把此信息交给用户，等待用户采取操作。

这不会影响其他回调，但请注意，配对过程中仍可能调用其他回调。例如，注册了 `pairing_confirm` 时，直接配对（Just Works）会调用这两个回调。

可以注销此回调；此时配对将继续进行，其行为等同于未设置相应 Kconfig 标志。

对于基本速率／增强数据率安全简单配对（BR/EDR Secure Simple Pairing，SSP），收到 `BT_HCI_EVT_IO_CAPA_REQ` 主机控制器接口事件（HCI event）时会调用此回调。此时 `feat` 为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 发起配对（Pairing）的连接。 |
| `feat` | 配对请求／响应信息（Pairing request/response info）。在 BR/EDR 安全简单配对（SSP）中为 `NULL`。 |

<a id="af4f7d3ee570b3472ee79b014be01f76e"></a>

### `pairing_confirm`

```c
void(* bt_conn_auth_cb::pairing_confirm) (struct bt_conn *conn)
```

请求确认传入的配对（Incoming pairing）。

当其他用户回调均不适用时，调用此回调确认传入的配对请求（Pairing request）。

若用户接受配对，应调用 `bt_conn_auth_pairing_confirm()` API；若用户拒绝配对，应调用 `bt_conn_auth_cancel()` API。

此回调可以设为 `NULL`，表示本地设备不具备确认配对请求的能力。如果设为非 `NULL`，则还必须提供 `cancel` 回调，因为应用只有通过它才能得知应停止请求用户确认配对。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |

<a id="a2bb6c10666d111f675fd6de5ff51410a"></a>

### `passkey_confirm`

```c
void(* bt_conn_auth_cb::passkey_confirm) (struct bt_conn *conn, unsigned int passkey)
```

请求用户确认配对密钥（Passkey）。

调用此回调时，用户应确认给定配对密钥（Passkey）是否也显示在对等设备上。密钥范围为 `0`–`999999`，应补前导零，使其始终为六位数字，例如 `37` 应显示为 `000037`。

用户确认配对密钥（Passkey）匹配后，应调用 `bt_conn_auth_passkey_confirm()` API。用户认为密钥不匹配时，应调用 `bt_conn_auth_cancel()` API。

此回调可以设为 `NULL`，表示本地设备不具备确认配对密钥（Passkey）的能力。如果设为非 `NULL`，则还必须提供 `cancel` 回调，因为应用只有通过它才能得知应停止请求用户确认密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |
| `passkey` | 待确认的配对密钥（Passkey）。 |

<a id="a14074ca97fad6af4c58c43a00c503104"></a>

### `passkey_display`

```c
void(* bt_conn_auth_cb::passkey_display) (struct bt_conn *conn, unsigned int passkey)
```

向用户显示配对密钥（Passkey）。

调用此回调时，应用应向用户显示给定配对密钥（Passkey），以便用户随后在对等设备上输入。密钥范围为 `0`–`999999`，应补前导零以始终显示六位数字。例如，值 `37` 应显示为 `000037`。

此回调可以设为 `NULL`，表示本地设备不具备显示配对密钥（Passkey）的能力。如果设为非 `NULL`，则还必须提供 `cancel` 回调，因为应用只有通过它才能得知应停止显示密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |
| `passkey` | 要向用户显示的配对密钥（Passkey）。 |

<a id="af736a8808504fce22b95131818bad450"></a>

### `passkey_display_keypress`

```c
void(* bt_conn_auth_cb::passkey_display_keypress) (struct bt_conn *conn, enum bt_conn_auth_keypress type)
```

配对期间接收配对密钥按键通知（Passkey Keypress Notification）。

这允许远端设备利用本地设备，向用户反馈远端输入配对密钥（Passkey）的进度。当远端设备自身没有适合显示输入进度的显示器时，此功能很有用。

此回调的处理函数应跟踪已输入的数字位数，并向用户显示类似密码输入框（Password field）的反馈。

此回调仅在本地执行配对密钥显示（Passkey Display）时适用。

事件类型（Event type）已验证处于枚举范围内，除此之外未进行其他合法性处理（Sanitization）。远端可能以任意顺序发送大量任意类型的事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 相关连接（Related connection）。 |
| `type` | 事件类型（Event type），已验证在枚举范围内。 |

<a id="a10f9d22c89c95a6f3ffe0016f92445c0"></a>

### `passkey_entry`

```c
void(* bt_conn_auth_cb::passkey_entry) (struct bt_conn *conn)
```

请求用户输入配对密钥（Passkey）。

调用此回调时，用户应输入配对密钥（Passkey）。密钥必须处于 `0`–`999999` 范围内，并应预期其带有前导零，因为对等设备通常按此方式显示，例如将 `37` 显示为 `000037`。

用户输入配对密钥（Passkey）后，应使用 `bt_conn_auth_passkey_entry()` API 将其值传给协议栈。

此回调可以设为 `NULL`，表示本地设备不具备输入配对密钥（Passkey）的能力。如果设为非 `NULL`，则还必须提供 `cancel` 回调，因为应用只有通过它才能得知应停止请求用户输入密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |

<a id="ab6df1b1505dc22dd8dae0e946546c8bb"></a>

### `pincode_entry`

```c
void(* bt_conn_auth_cb::pincode_entry) (struct bt_conn *conn, bool highsec)
```

请求用户输入配对密钥（Passkey）。

此回调用于正在执行配对的基本速率／增强数据率连接（BR/EDR，即经典蓝牙）。调用后，用户应输入长度为 1–16 位的个人识别码（PIN）。若 `highsec` 参数设为 `true`，PIN 必须恰好为 16 位。

输入完成后，应通过 `bt_conn_auth_pincode_entry()` API 将个人识别码（PIN）传给协议栈。

此回调可以设为 `NULL`，但此时无法通过 BR/EDR 配对。提供此回调时，也必须提供 `cancel` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 当前正在进行配对（Pairing）的连接。 |
| `highsec` | 要求 16 位个人识别码（PIN）时为 `true`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)
- [bt_conn](P002_bt_conn_结构体.md)
- [bt_conn_pairing_feat](P038_bt_conn_pairing_feat_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)
- [bt_conn_oob_info](P037_bt_conn_oob_info_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [bt_le_oob_set_sc_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac365f9748ad0737f09142ee1de982503)
- [bt_conn_auth_pairing_confirm()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3e15b9deb6787d3e415bbea35c9aa91d)
- [bt_conn_auth_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga89e5fc4bcab3f5598d20a9cd8ace5f59)
- [bt_conn_auth_passkey_confirm()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8c3ecf2a3d68e54379917844a29d995)
- [bt_conn_auth_passkey_entry()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)
- [bt_conn_auth_pincode_entry()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4002a1b092832807218afa8ad279ab98)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_conn_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_conn_auth_info_cb_结构体.md)
