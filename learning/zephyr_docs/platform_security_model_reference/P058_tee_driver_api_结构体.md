---
id: learning.zephyr-docs.platform-security-model-reference.page-58
title: tee_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_tee\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：可信执行环境（TEE）驱动操作。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：可信执行环境（Trusted Execution Environment，TEE）驱动操作。这是每个 TEE 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_ac99f066bd644741df90d418ab9fe4198"></a>

```c
tee_get_version_t get_version
```

相关声明：[tee_get_version_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac533d9e85d65857c0d984506024a55b4)、[get_version](#ac99f066bd644741df90d418ab9fe4198)。

`OPT`：获取当前 TEE 版本信息。

<a id="r_acf8076d0cf2bb496d9c6143d6e5d2253"></a>

```c
tee_open_session_t open_session
```

相关声明：[tee_open_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaf972199fcdbd892688dc141ddba6e6aa)、[open_session](#acf8076d0cf2bb496d9c6143d6e5d2253)。

`OPT`：为可信执行环境打开会话（Session）。

<a id="r_a380a12c033c1c659d7169d0d16593f94"></a>

```c
tee_close_session_t close_session
```

相关声明：[tee_close_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac412f57a3da187e6e272857d5bdaaaeb)、[close_session](#a380a12c033c1c659d7169d0d16593f94)。

`OPT`：关闭可信执行环境的会话。

<a id="r_a04db5713f645416fa9cc015433941a94"></a>

```c
tee_cancel_t cancel
```

相关声明：[tee_cancel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gad4cd5b65cac3eb7b4338fd99eeb13a93)、[cancel](#a04db5713f645416fa9cc015433941a94)。

`OPT`：取消可信执行环境的会话或函数调用。

<a id="r_a5d2a33d8156fd56176f69e903da9204e"></a>

```c
tee_invoke_func_t invoke_func
```

相关声明：[tee_invoke_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac3695e51dc8b08bb5e5c5d984c402b0e)、[invoke_func](#a5d2a33d8156fd56176f69e903da9204e)。

`OPT`：调用可信执行环境应用程序的函数。

<a id="r_a1db852ebd953c0c4ba5f88fcab9fdce9"></a>

```c
tee_shm_register_t shm_register
```

相关声明：[tee_shm_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga9e2807d34d580c012129a2fc1f5a425a)、[shm_register](#a1db852ebd953c0c4ba5f88fcab9fdce9)。

`OPT`：为可信执行环境注册共享内存（Shared memory）。

<a id="r_ac24f7f4d3f63145e8f687a37cad780ca"></a>

```c
tee_shm_unregister_t shm_unregister
```

相关声明：[tee_shm_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga2ea18e713a101a6ca715baa04c2f4185)、[shm_unregister](#ac24f7f4d3f63145e8f687a37cad780ca)。

`OPT`：注销可信执行环境的共享内存。

<a id="r_a35c770c1dfb807bb461640a519fdabe5"></a>

```c
tee_suppl_recv_t suppl_recv
```

相关声明：[tee_suppl_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaae68677cbff1e831fadc3d188c8588ff)、[suppl_recv](#a35c770c1dfb807bb461640a519fdabe5)。

`OPT`：接收供 TEE 辅助进程（TEE Supplicant）处理的请求。

<a id="r_abd28ba23f09ce245a6346f7a241eb9cc"></a>

```c
tee_suppl_send_t suppl_send
```

相关声明：[tee_suppl_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)、[suppl_send](#abd28ba23f09ce245a6346f7a241eb9cc)。

`OPT`：发送 TEE 辅助进程功能的请求。

## 58.2\_详细说明（Detailed Documentation）

<a id="a04db5713f645416fa9cc015433941a94"></a>

### `cancel`

```c
tee_cancel_t tee_driver_api::cancel
```

`OPT`：取消可信执行环境的会话或函数调用。

<a id="a380a12c033c1c659d7169d0d16593f94"></a>

### `close_session`

```c
tee_close_session_t tee_driver_api::close_session
```

`OPT`：关闭可信执行环境的会话。

<a id="ac99f066bd644741df90d418ab9fe4198"></a>

### `get_version`

```c
tee_get_version_t tee_driver_api::get_version
```

`OPT`：获取当前 TEE 版本信息。

<a id="a5d2a33d8156fd56176f69e903da9204e"></a>

### `invoke_func`

```c
tee_invoke_func_t tee_driver_api::invoke_func
```

`OPT`：调用可信执行环境应用程序的函数。

<a id="acf8076d0cf2bb496d9c6143d6e5d2253"></a>

### `open_session`

```c
tee_open_session_t tee_driver_api::open_session
```

`OPT`：为可信执行环境打开会话（Session）。

<a id="a1db852ebd953c0c4ba5f88fcab9fdce9"></a>

### `shm_register`

```c
tee_shm_register_t tee_driver_api::shm_register
```

`OPT`：为可信执行环境注册共享内存（Shared memory）。

<a id="ac24f7f4d3f63145e8f687a37cad780ca"></a>

### `shm_unregister`

```c
tee_shm_unregister_t tee_driver_api::shm_unregister
```

`OPT`：注销可信执行环境的共享内存。

<a id="a35c770c1dfb807bb461640a519fdabe5"></a>

### `suppl_recv`

```c
tee_suppl_recv_t tee_driver_api::suppl_recv
```

`OPT`：接收供 TEE 辅助进程（TEE Supplicant）处理的请求。

<a id="abd28ba23f09ce245a6346f7a241eb9cc"></a>

### `suppl_send`

```c
tee_suppl_send_t tee_driver_api::suppl_send
```

`OPT`：发送 TEE 辅助进程功能的请求。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [tee_get_version_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac533d9e85d65857c0d984506024a55b4)
- [tee_open_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaf972199fcdbd892688dc141ddba6e6aa)
- [tee_close_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac412f57a3da187e6e272857d5bdaaaeb)
- [tee_cancel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gad4cd5b65cac3eb7b4338fd99eeb13a93)
- [tee_invoke_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac3695e51dc8b08bb5e5c5d984c402b0e)
- [tee_shm_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga9e2807d34d580c012129a2fc1f5a425a)
- [tee_shm_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga2ea18e713a101a6ca715baa04c2f4185)
- [tee_suppl_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaae68677cbff1e831fadc3d188c8588ff)
- [tee_suppl_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_sip_svc_response_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_tee_invoke_func_arg_结构体.md)
