---
id: learning.zephyr-docs.api-file-display-chat-reference.page-20
title: ____w__zephyr__zephyr__modules__openthread__include__openthread.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_modules\_\_openthread\_\_include\_\_openthread.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <openthread/instance.h>
#include <openthread/message.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_openthread_5Fstate_5Fchanged_5Fcallback"></a>

```c
struct openthread_state_changed_callback
```

相关声明：[openthread_state_changed_callback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md)。

OpenThread状态变化（State Change）的回调。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 20.2\_类型定义（Typedefs）

<a id="r_a8f95392e11afa85e9bd80569c1793e76"></a>

```c
typedef void(* openthread_receive_cb) (struct otMessage *message, void *context)
```

相关声明：[openthread_receive_cb](#a8f95392e11afa85e9bd80569c1793e76)。

接收 IPv4（经 NAT64 转换）与 IPv6 数据报（Datagrams）的公共回调类型（Common Callback Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.3\_函数（Functions）

<a id="r_a4178b72288585869e2c941acdc21db57"></a>

```c
int openthread_state_changed_callback_register (struct openthread_state_changed_callback *cb)
```

相关声明：[openthread_state_changed_callback_register](#a4178b72288585869e2c941acdc21db57)、[openthread_state_changed_callback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md)。

注册在 OpenThread 内部发生特定配置或状态变化时调用的回调（Callbacks）。

<a id="r_ae4ad25613f8eada1a0a29426a2f4a518"></a>

```c
int openthread_state_changed_callback_unregister (struct openthread_state_changed_callback *cb)
```

相关声明：[openthread_state_changed_callback_unregister](#ae4ad25613f8eada1a0a29426a2f4a518)、[openthread_state_changed_callback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md)。

注销 OpenThread 配置或状态变化回调（Configuration or State Changed Callbacks）。

<a id="r_a9499c4c69a0094f0b7ef803ac05fb19a"></a>

```c
k_tid_t openthread_thread_id_get (void)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[openthread_thread_id_get](#a9499c4c69a0094f0b7ef803ac05fb19a)。

获取 OpenThread 线程标识（Thread Identification）。

<a id="r_a1d81606d48cfb714ba59b94400bbce23"></a>

```c
struct k_work_q * openthread_work_q_get (void)
```

相关声明：[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[openthread_work_q_get](#a1d81606d48cfb714ba59b94400bbce23)。

获取 OpenThread 工作队列（Work Queue）。

<a id="r_a517a538fa32afac8ca8968ada2cea89d"></a>

```c
struct otInstance * openthread_get_default_instance (void)
```

相关声明：[openthread_get_default_instance](#a517a538fa32afac8ca8968ada2cea89d)。

获取默认 OpenThread 实例（Default Instance）的指针。

<a id="r_a4d213cad99e6eeb747bd0057248251e5"></a>

```c
int openthread_init (void)
```

相关声明：[openthread_init](#a4d213cad99e6eeb747bd0057248251e5)。

初始化 OpenThread 模块（Module）。

<a id="r_a558165d2e49e9335649c94ac0be53392"></a>

```c
int openthread_run (void)
```

相关声明：[openthread_run](#a558165d2e49e9335649c94ac0be53392)。

运行 OpenThread 网络（Network）。

<a id="r_af52cc96d5d4be673f16eb4856de6cc58"></a>

```c
int openthread_stop (void)
```

相关声明：[openthread_stop](#af52cc96d5d4be673f16eb4856de6cc58)。

禁用 OpenThread 网络（Network）。

<a id="r_a14ea88a5f4e4a9e014f2381cd853e8de"></a>

```c
void openthread_set_receive_cb (openthread_receive_cb cb, void *context)
```

相关声明：[openthread_set_receive_cb](#a14ea88a5f4e4a9e014f2381cd853e8de)、[openthread_receive_cb](#a8f95392e11afa85e9bd80569c1793e76)。

设置接收数据包的附加回调（Additional Callback）。

<a id="r_a76aff0a483b1462707f80de5185b17e4"></a>

```c
void openthread_set_nat64_receive_cb (openthread_receive_cb cb, void *context)
```

相关声明：[openthread_set_nat64_receive_cb](#a76aff0a483b1462707f80de5185b17e4)、[openthread_receive_cb](#a8f95392e11afa85e9bd80569c1793e76)。

设置接收经 NAT64 转换的数据包的附加回调（Additional Callback）。

<a id="r_ae3945bc3549118dc5420f9859588282d"></a>

```c
void openthread_mutex_lock (void)
```

相关声明：[openthread_mutex_lock](#ae3945bc3549118dc5420f9859588282d)。

在访问 OpenThread API 前锁定内部互斥量（Internal Mutex）。

<a id="r_ab5669622dfd83d3a5175fa47325dade3"></a>

```c
int openthread_mutex_try_lock (void)
```

相关声明：[openthread_mutex_try_lock](#ab5669622dfd83d3a5175fa47325dade3)。

在访问 OpenThread API 前尝试锁定内部互斥量（Internal Mutex）。

<a id="r_a420c3321272141f63ea86166b84ec845"></a>

```c
void openthread_mutex_unlock (void)
```

相关声明：[openthread_mutex_unlock](#a420c3321272141f63ea86166b84ec845)。

在访问 OpenThread API 后解锁内部互斥量（Internal Mutex）。

## 20.4\_详细说明（Detailed Documentation）

<a id="a8f95392e11afa85e9bd80569c1793e76"></a>

### `openthread_receive_cb`

```c
typedef void(* openthread_receive_cb) (struct otMessage *message, void *context)
```

接收 IPv4（经 NAT64 转换）与 IPv6 数据报（Datagrams）的公共回调类型（Common Callback Type）。

接收到数据报（Datagram）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `message` | 要接收的消息（Message）。 |
| `context` | 传递给回调的上下文（Context）。 |

<a id="a517a538fa32afac8ca8968ada2cea89d"></a>

### `openthread_get_default_instance()`

```c
struct otInstance * openthread_get_default_instance ( void )
```

获取默认 OpenThread 实例（Default Instance）的指针。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `!NULL` | 成功时返回。 |
| `NULL` | 失败。 |

<a id="a4d213cad99e6eeb747bd0057248251e5"></a>

### `openthread_init()`

```c
int openthread_init ( void )
```

初始化 OpenThread 模块（Module）。

此函数执行以下操作：

- 初始化 OpenThread 模块（Module）。
- 创建 OpenThread 单一实例（Single Instance）。
- 启动命令行（Shell）。
- 为协处理器（Coprocessor）用途启用 UART 和 NCP HDLC。
- 初始化 NAT64 转换器（Translator）。
- 为 OpenThread 模块创建工作队列（Work Queue）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |

**说明（Note）**：注意（Note）：Zephyr 网络层（Networking Layer）会自动调用此函数。如果希望独立初始化 OpenThread，请在应用初始化代码中调用它。

<a id="ae3945bc3549118dc5420f9859588282d"></a>

### `openthread_mutex_lock()`

```c
void openthread_mutex_lock ( void )
```

在访问 OpenThread API 前锁定内部互斥量（Internal Mutex）。

OpenThread API 不是线程安全的（Thread-safe）。因此，在访问任何 API 函数前，都需要锁定内部互斥量（Internal Mutex），防止 OpenThread 线程抢占 API 调用。

<a id="ab5669622dfd83d3a5175fa47325dade3"></a>

### `openthread_mutex_try_lock()`

```c
int openthread_mutex_try_lock ( void )
```

在访问 OpenThread API 前尝试锁定内部互斥量（Internal Mutex）。

内部互斥量（Internal Mutex）未被锁定时，此函数的行为与 openthread_mutex_lock() 相同；否则立即返回负值，不进行等待。

<a id="a420c3321272141f63ea86166b84ec845"></a>

### `openthread_mutex_unlock()`

```c
void openthread_mutex_unlock ( void )
```

在访问 OpenThread API 后解锁内部互斥量（Internal Mutex）。

<a id="a558165d2e49e9335649c94ac0be53392"></a>

### `openthread_run()`

```c
int openthread_run ( void )
```

运行 OpenThread 网络（Network）。

准备并启用 OpenThread 网络。其行为取决于当前有效设置：使用已存储的网络配置（Stored Network Configuration）、启动加入过程（Joining Procedure），或使用默认网络配置（Default Network Configuration）。此外，设备为最小 Thread 设备（Minimal Thread Device，MTD）时，会设置休眠终端设备（Sleepy End Device，SED）模式，以正确附着到网络。

<a id="a76aff0a483b1462707f80de5185b17e4"></a>

### `openthread_set_nat64_receive_cb()`

```c
void openthread_set_nat64_receive_cb ( openthread_receive_cb cb, void * context )
```

设置接收经 NAT64 转换的数据包的附加回调（Additional Callback）。

收到来自 OpenThread NAT64 转换器（NAT64 Translator）的数据包时调用此回调，可用它向 Zephyr 网络协议栈（Networking Stack）注入数据包。设置此回调是可选的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要设置的回调（Callback）。 |
| `context` | 传递给回调的上下文（Context）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_OPENTHREAD_NAT64_TRANSLATOR 时可用。

<a id="a14ea88a5f4e4a9e014f2381cd853e8de"></a>

### `openthread_set_receive_cb()`

```c
void openthread_set_receive_cb ( openthread_receive_cb cb, void * context )
```

设置接收数据包的附加回调（Additional Callback）。

收到数据包时调用此回调，可用它向 Zephyr 网络协议栈（Networking Stack）注入数据包。设置此回调是可选的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要设置的回调（Callback）。 |
| `context` | 传递给回调的上下文（Context）。 |

<a id="a4178b72288585869e2c941acdc21db57"></a>

### `openthread_state_changed_callback_register()`

```c
int openthread_state_changed_callback_register ( struct openthread_state_changed_callback * cb)
```

注册在 OpenThread 内部发生特定配置或状态变化时调用的回调（Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要注册的回调结构体（Callback Struct）。 |

<a id="ae4ad25613f8eada1a0a29426a2f4a518"></a>

### `openthread_state_changed_callback_unregister()`

```c
int openthread_state_changed_callback_unregister ( struct openthread_state_changed_callback * cb)
```

注销 OpenThread 配置或状态变化回调（Configuration or State Changed Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要注销的回调结构体（Callback Struct）。 |

<a id="af52cc96d5d4be673f16eb4856de6cc58"></a>

### `openthread_stop()`

```c
int openthread_stop ( void )
```

禁用 OpenThread 网络（Network）。

<a id="a9499c4c69a0094f0b7ef803ac05fb19a"></a>

### `openthread_thread_id_get()`

```c
k_tid_t openthread_thread_id_get ( void )
```

获取 OpenThread 线程标识（Thread Identification）。

<a id="a1d81606d48cfb714ba59b94400bbce23"></a>

### `openthread_work_q_get()`

```c
struct k_work_q * openthread_work_q_get ( void )
```

获取 OpenThread 工作队列（Work Queue）。


## 20.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P541_openthread.h_源码浏览.md)
- [openthread_state_changed_callback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)
- [CONFIG_OPENTHREAD_NAT64_TRANSLATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_NAT64_TRANSLATOR)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_zephyr__drivers__clock_control__mchp_clock_pic32cm_sg_gc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__dt-bindings__reset__syna_sr100_reset.h_文件参考.md)
