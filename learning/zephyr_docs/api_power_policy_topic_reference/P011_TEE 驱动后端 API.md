---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-11
title: TEE 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_TEE 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现可信执行环境（TEE）驱动所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_tee_5Fdriver_5Fapi"></a>

```c
struct tee_driver_api
```

相关声明：[tee_driver_api](../platform_security_model_reference/P058_tee_driver_api_结构体.md)。

驱动操作（Driver Operations）：可信执行环境（TEE）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_gac533d9e85d65857c0d984506024a55b4"></a>

```c
typedef int(* tee_get_version_t) (const struct device *dev, struct tee_version_info *info)
```

相关声明：[tee_get_version_t](#gac533d9e85d65857c0d984506024a55b4)、[device](../device_reference/P002_设备对象结构.md)、[tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)。

获取当前可信执行环境（TEE）版本的回调 API。

<a id="r_gaf972199fcdbd892688dc141ddba6e6aa"></a>

```c
typedef int(* tee_open_session_t) (const struct device *dev, struct tee_open_session_arg *arg, unsigned int num_param, struct tee_param *param, uint32_t *session_id)
```

相关声明：[tee_open_session_t](#gaf972199fcdbd892688dc141ddba6e6aa)、[device](../device_reference/P002_设备对象结构.md)、[tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

打开到可信应用（Trusted Application，TA）的会话（Session）的回调 API。

<a id="r_gac412f57a3da187e6e272857d5bdaaaeb"></a>

```c
typedef int(* tee_close_session_t) (const struct device *dev, uint32_t session_id)
```

相关声明：[tee_close_session_t](#gac412f57a3da187e6e272857d5bdaaaeb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

关闭到可信应用（TA）的会话（Session）的回调 API。

<a id="r_gad4cd5b65cac3eb7b4338fd99eeb13a93"></a>

```c
typedef int(* tee_cancel_t) (const struct device *dev, uint32_t session_id, uint32_t cancel_id)
```

相关声明：[tee_cancel_t](#gad4cd5b65cac3eb7b4338fd99eeb13a93)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

取消面向可信应用（TA）的会话打开或函数调用（Open Session or Invoke Function）的回调 API。原文的 `open session of invoke function` 按上下文理解为两类可取消操作。

<a id="r_gac3695e51dc8b08bb5e5c5d984c402b0e"></a>

```c
typedef int(* tee_invoke_func_t) (const struct device *dev, struct tee_invoke_func_arg *arg, unsigned int num_param, struct tee_param *param)
```

相关声明：[tee_invoke_func_t](#gac3695e51dc8b08bb5e5c5d984c402b0e)、[device](../device_reference/P002_设备对象结构.md)、[tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

调用可信应用（TA）中函数（Function）的回调 API。

<a id="r_ga9e2807d34d580c012129a2fc1f5a425a"></a>

```c
typedef int(* tee_shm_register_t) (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_register_t](#ga9e2807d34d580c012129a2fc1f5a425a)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注册共享内存（Shared Memory）的回调 API。

<a id="r_ga2ea18e713a101a6ca715baa04c2f4185"></a>

```c
typedef int(* tee_shm_unregister_t) (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_unregister_t](#ga2ea18e713a101a6ca715baa04c2f4185)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注销共享内存（Shared Memory）的回调 API。

<a id="r_gaae68677cbff1e831fadc3d188c8588ff"></a>

```c
typedef int(* tee_suppl_recv_t) (const struct device *dev, uint32_t *func, unsigned int *num_params, struct tee_param *param)
```

相关声明：[tee_suppl_recv_t](#gaae68677cbff1e831fadc3d188c8588ff)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）接收请求（Request）的回调 API。

<a id="r_ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20"></a>

```c
typedef int(* tee_suppl_send_t) (const struct device *dev, unsigned int ret, unsigned int num_params, struct tee_param *param)
```

相关声明：[tee_suppl_send_t](#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）发送请求（Request）的回调 API。

## 11.3\_详细说明（Detailed Documentation）

<a id="gad4cd5b65cac3eb7b4338fd99eeb13a93"></a>

### `tee_cancel_t`

```c
typedef int(* tee_cancel_t) (const struct device *dev, uint32_t session_id, uint32_t cancel_id)
```

```c
#include <zephyr/drivers/tee.h>
```

取消面向可信应用（TA）的会话打开或函数调用（Open Session or Invoke Function）的回调 API。原文的 `open session of invoke function` 按上下文理解为两类可取消操作。

参数定义（Argument Definitions）参见 `tee_cancel()`。

<a id="gac412f57a3da187e6e272857d5bdaaaeb"></a>

### `tee_close_session_t`

```c
typedef int(* tee_close_session_t) (const struct device *dev, uint32_t session_id)
```

```c
#include <zephyr/drivers/tee.h>
```

关闭到可信应用（TA）的会话（Session）的回调 API。

参数定义（Argument Definitions）参见 `tee_close_session()`。

<a id="gac533d9e85d65857c0d984506024a55b4"></a>

### `tee_get_version_t`

```c
typedef int(* tee_get_version_t) (const struct device *dev, struct tee_version_info *info)
```

```c
#include <zephyr/drivers/tee.h>
```

获取当前可信执行环境（TEE）版本的回调 API。

参数定义（Argument Definitions）参见 `tee_get_version()`。

<a id="gac3695e51dc8b08bb5e5c5d984c402b0e"></a>

### `tee_invoke_func_t`

```c
typedef int(* tee_invoke_func_t) (const struct device *dev, struct tee_invoke_func_arg *arg, unsigned int num_param, struct tee_param *param)
```

```c
#include <zephyr/drivers/tee.h>
```

调用可信应用（TA）中函数（Function）的回调 API。

参数定义（Argument Definitions）参见 `tee_invoke_func()`。

<a id="gaf972199fcdbd892688dc141ddba6e6aa"></a>

### `tee_open_session_t`

```c
typedef int(* tee_open_session_t) (const struct device *dev, struct tee_open_session_arg *arg, unsigned int num_param, struct tee_param *param, uint32_t *session_id)
```

```c
#include <zephyr/drivers/tee.h>
```

打开到可信应用（Trusted Application，TA）的会话（Session）的回调 API。

参数定义（Argument Definitions）参见 `tee_open_session()`。

<a id="ga9e2807d34d580c012129a2fc1f5a425a"></a>

### `tee_shm_register_t`

```c
typedef int(* tee_shm_register_t) (const struct device *dev, struct tee_shm *shm)
```

```c
#include <zephyr/drivers/tee.h>
```

注册共享内存（Shared Memory）的回调 API。

参数定义（Argument Definitions）参见 `tee_shm_register()`。

<a id="ga2ea18e713a101a6ca715baa04c2f4185"></a>

### `tee_shm_unregister_t`

```c
typedef int(* tee_shm_unregister_t) (const struct device *dev, struct tee_shm *shm)
```

```c
#include <zephyr/drivers/tee.h>
```

注销共享内存（Shared Memory）的回调 API。

参数定义（Argument Definitions）参见 `tee_shm_unregister()`。

<a id="gaae68677cbff1e831fadc3d188c8588ff"></a>

### `tee_suppl_recv_t`

```c
typedef int(* tee_suppl_recv_t) (const struct device *dev, uint32_t *func, unsigned int *num_params, struct tee_param *param)
```

```c
#include <zephyr/drivers/tee.h>
```

为 TEE 辅助服务（Supplicant）接收请求（Request）的回调 API。

参数定义（Argument Definitions）参见 `tee_suppl_recv()`。

<a id="ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20"></a>

### `tee_suppl_send_t`

```c
typedef int(* tee_suppl_send_t) (const struct device *dev, unsigned int ret, unsigned int num_params, struct tee_param *param)
```

```c
#include <zephyr/drivers/tee.h>
```

为 TEE 辅助服务（Supplicant）发送请求（Request）的回调 API。

参数定义（Argument Definitions）参见 `tee_suppl_send()`。


## 11.4\_原页交叉引用（Cross References）

- [tee_driver_api](../platform_security_model_reference/P058_tee_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)
- [tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)
- [tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)
- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h.html)
- [tee_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga34fbbfe48a07541041ffddb9e318332a)
- [tee_close_session()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gacb1d58002378a11d92361a149d451241)
- [tee_get_version()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gadaaec6b6ea29d81f36943bbe5bcb305e)
- [tee_invoke_func()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae1337f293febcecc7dbc79ac064e7824)
- [tee_open_session()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c66e32d5b02c42c698bd422cf43523)
- [tee_shm_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga1565c23104792203ede9d9cb388ff782)
- [tee_shm_unregister()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade2c0e7d89e3594707637b62a1901bac)
- [tee_suppl_recv()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2213f63da1f080beaedc169e13531a37)
- [tee_suppl_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga93cccfa446983be704f364760bf7567b)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P010_受电端回调（Sink Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P012_视频类型（Video Types）.md)
