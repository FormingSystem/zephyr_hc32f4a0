---
id: learning.zephyr-docs.api-file-usb-network-reference.page-14
title: zephyr__drivers__sip_svc__sip_svc_driver.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_sip\_svc\_\_sip\_svc\_driver.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>
#include <zephyr/sip_svc/sip_svc_controller.h>
#include <zephyr/syscalls/sip_svc_driver.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_svc_5Fdriver_5Fapi"></a>

```c
struct svc_driver_api
```

相关声明：[svc_driver_api](../device_power_control_model_reference/P092_svc_driver_api_结构体.md)。

sip_svc驱动的API结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_a780bbf4be68a9ac867243823c0eb790e"></a>

```c
#define SVC_CONDUIT_NAME_LENGTH (4)
```

相关声明：[SVC_CONDUIT_NAME_LENGTH](#a780bbf4be68a9ac867243823c0eb790e)。

SVC 调用通道名称（Conduit Name）的长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.3\_类型定义（Typedefs）

<a id="r_a15714e3852882693de6c9c7f2229bcd1"></a>

```c
typedef void(* sip_supervisory_call_t) (const struct device *dev, unsigned long function_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm_smccc_res *res)
```

相关声明：[sip_supervisory_call_t](#a15714e3852882693de6c9c7f2229bcd1)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

执行监管调用（Supervisory Call）的回调 API。参数说明参见 `sip_supervisory_call()`。

<a id="r_ac5921c9cdc00604651696e1580f30797"></a>

```c
typedef bool(* sip_svc_plat_func_id_valid_t) (const struct device *dev, uint32_t command, uint32_t func_id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sip_svc_plat_func_id_valid_t](#ac5921c9cdc00604651696e1580f30797)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

验证监管调用（Supervisory Call）函数标识符（Function ID）的回调 API。

<a id="r_a3cf78c760c6eae2091e92329e54b1a31"></a>

```c
typedef uint32_t(* sip_svc_plat_format_trans_id_t) (const struct device *dev, uint32_t client_idx, uint32_t trans_idx)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_format_trans_id_t](#a3cf78c760c6eae2091e92329e54b1a31)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

根据客户端标识符（Client ID）生成事务标识符（Transaction ID）的回调 API。

<a id="r_a35145ddf422e8782b4ec37270b04d98c"></a>

```c
typedef uint32_t(* sip_svc_plat_get_trans_idx_t) (const struct device *dev, uint32_t trans_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_get_trans_idx_t](#a35145ddf422e8782b4ec37270b04d98c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从事务标识符（Transaction ID）提取客户端事务标识符（Client Transaction ID）的回调 API。参数说明参见 `sip_svc_plat_get_trans_idx()`。

<a id="r_a9d61db0484e2aacce4515290ffb4450c"></a>

```c
typedef void(* sip_svc_plat_update_trans_id_t) (const struct device *dev, struct sip_svc_request *request, uint32_t trans_id)
```

相关声明：[sip_svc_plat_update_trans_id_t](#a9d61db0484e2aacce4515290ffb4450c)、[device](../device_reference/P002_设备对象结构.md)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为发往下层的请求包（Request Packet）更新事务标识符（Transaction ID）的回调 API。参数说明参见 `sip_svc_plat_update_trans_id()`。

<a id="r_ab32e31bdba00ff66303fab1b04cd0ebe"></a>

```c
typedef void(* sip_svc_plat_free_async_memory_t) (const struct device *dev, struct sip_svc_request *request)
```

相关声明：[sip_svc_plat_free_async_memory_t](#ab32e31bdba00ff66303fab1b04cd0ebe)、[device](../device_reference/P002_设备对象结构.md)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)。

释放异步（ASYNC）数据包中命令缓冲区（Command Buffer）的回调 API。参数说明参见 `sip_svc_plat_free_async_memory()`。

<a id="r_aa49a26b4b503e58d23fb5087ed701a0a"></a>

```c
typedef int(* sip_svc_plat_async_res_req_t) (const struct device *dev, unsigned long *a0, unsigned long *a1, unsigned long *a2, unsigned long *a3, unsigned long *a4, unsigned long *a5, unsigned long *a6, unsigned long *a7, char *buf, size_t size)
```

相关声明：[sip_svc_plat_async_res_req_t](#aa49a26b4b503e58d23fb5087ed701a0a)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

为异步事务（ASYNC Transaction）构造轮询数据包（Polling Packet）的回调 API。

<a id="r_a54293f84f9bc86661f8a4bf717ad4754"></a>

```c
typedef int(* sip_svc_plat_async_res_res_t) (const struct device *dev, struct arm_smccc_res *res, char *buf, size_t *size, uint32_t *trans_id)
```

相关声明：[sip_svc_plat_async_res_res_t](#a54293f84f9bc86661f8a4bf717ad4754)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查轮询请求响应（Polling Request Response）的回调 API。参数说明参见 `sip_svc_plat_async_res_res()`。

<a id="r_a926eeecea766b2131c03c57111a186f8"></a>

```c
typedef uint32_t(* sip_svc_plat_get_error_code_t) (const struct device *dev, struct arm_smccc_res *res)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_get_error_code_t](#a926eeecea766b2131c03c57111a186f8)、[device](../device_reference/P002_设备对象结构.md)。

从监管调用响应（Supervisory Call Response）提取错误码（Error Code）的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_a881e3794f9e29e12c925cb5dbd443420"></a>

```c
void sip_supervisory_call (const struct device *dev, unsigned long function_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm_smccc_res *res)
```

相关声明：[sip_supervisory_call](#a881e3794f9e29e12c925cb5dbd443420)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

执行 `smc`／`hvc` 调用的监管调用函数（Supervisory Call Function）。

<a id="r_a8df36a218cce4c0904c147d498c1322d"></a>

```c
bool sip_svc_plat_func_id_valid (const struct device *dev, uint32_t command, uint32_t func_id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sip_svc_plat_func_id_valid](#a8df36a218cce4c0904c147d498c1322d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

验证监管调用（Supervisory Call）的函数标识符（Function ID）。

<a id="r_ae52dee0bbba688a73a9726dd4aa482d2"></a>

```c
uint32_t sip_svc_plat_format_trans_id (const struct device *dev, uint32_t client_idx, uint32_t trans_idx)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_format_trans_id](#ae52dee0bbba688a73a9726dd4aa482d2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

根据客户端标识符（Client ID），格式化并生成事务标识符（Transaction ID）。

<a id="r_ad0e52f49e7db8cf51ff8cf95e1283994"></a>

```c
uint32_t sip_svc_plat_get_trans_idx (const struct device *dev, uint32_t trans_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_get_trans_idx](#ad0e52f49e7db8cf51ff8cf95e1283994)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从数据包事务标识符（Packet Transaction ID）提取客户端事务标识符（Client Transaction ID）。

<a id="r_a095123f7aec80a3e51d75ef248990124"></a>

```c
void sip_svc_plat_update_trans_id (const struct device *dev, struct sip_svc_request *request, uint32_t trans_id)
```

相关声明：[sip_svc_plat_update_trans_id](#a095123f7aec80a3e51d75ef248990124)、[device](../device_reference/P002_设备对象结构.md)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为发往下层的 `sip_svc_request` 更新事务标识符（Transaction ID）。

<a id="r_a3510743d8cf114376b740f3d297c583f"></a>

```c
uint32_t sip_svc_plat_get_error_code (const struct device *dev, struct arm_smccc_res *res)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_plat_get_error_code](#a3510743d8cf114376b740f3d297c583f)、[device](../device_reference/P002_设备对象结构.md)。

从 `arm_smccc_res` 响应中提取错误码（Error Code）。

<a id="r_abb9ff6ec7dea6fc4e104db8cc5e7168b"></a>

```c
int sip_svc_plat_async_res_req (const struct device *dev, unsigned long *a0, unsigned long *a1, unsigned long *a2, unsigned long *a3, unsigned long *a4, unsigned long *a5, unsigned long *a6, unsigned long *a7, char *buf, size_t size)
```

相关声明：[sip_svc_plat_async_res_req](#abb9ff6ec7dea6fc4e104db8cc5e7168b)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置轮询监管调用（Polling Supervisory Call）的参数。

<a id="r_a0a0577249c2a9f470cd6ec0a60b455c8"></a>

```c
int sip_svc_plat_async_res_res (const struct device *dev, struct arm_smccc_res *res, char *buf, size_t *size, uint32_t *trans_id)
```

相关声明：[sip_svc_plat_async_res_res](#a0a0577249c2a9f470cd6ec0a60b455c8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查轮询监管调用（Polling Supervisory Call）的响应，并获取响应大小（Response Size）和事务标识符（Transaction ID）。

<a id="r_aa4e44eb2af080207821a60f8b3442886"></a>

```c
void sip_svc_plat_free_async_memory (const struct device *dev, struct sip_svc_request *request)
```

相关声明：[sip_svc_plat_free_async_memory](#aa4e44eb2af080207821a60f8b3442886)、[device](../device_reference/P002_设备对象结构.md)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)。

将异步（ASYNC）数据包发送到下层后，释放其使用的命令缓冲区（Command Buffer）。

## 14.5\_详细说明（Detailed Documentation）

<a id="a780bbf4be68a9ac867243823c0eb790e"></a>

### `SVC_CONDUIT_NAME_LENGTH`

```c
#define SVC_CONDUIT_NAME_LENGTH (4)
```

SVC 调用通道名称（Conduit Name）的长度。

<a id="a15714e3852882693de6c9c7f2229bcd1"></a>

### `sip_supervisory_call_t`

```c
typedef void(* sip_supervisory_call_t) (const struct device *dev, unsigned long function_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm_smccc_res *res)
```

执行监管调用（Supervisory Call）的回调 API。参数说明参见 `sip_supervisory_call()`。

<a id="aa49a26b4b503e58d23fb5087ed701a0a"></a>

### `sip_svc_plat_async_res_req_t`

```c
typedef int(* sip_svc_plat_async_res_req_t) (const struct device *dev, unsigned long *a0, unsigned long *a1, unsigned long *a2, unsigned long *a3, unsigned long *a4, unsigned long *a5, unsigned long *a6, unsigned long *a7, char *buf, size_t size)
```

为异步事务（ASYNC Transaction）构造轮询数据包（Polling Packet）的回调 API。

参数说明参见 `sip_svc_plat_async_res_req()`。

<a id="a54293f84f9bc86661f8a4bf717ad4754"></a>

### `sip_svc_plat_async_res_res_t`

```c
typedef int(* sip_svc_plat_async_res_res_t) (const struct device *dev, struct arm_smccc_res *res, char *buf, size_t *size, uint32_t *trans_id)
```

检查轮询请求响应（Polling Request Response）的回调 API。参数说明参见 `sip_svc_plat_async_res_res()`。

<a id="a3cf78c760c6eae2091e92329e54b1a31"></a>

### `sip_svc_plat_format_trans_id_t`

```c
typedef uint32_t(* sip_svc_plat_format_trans_id_t) (const struct device *dev, uint32_t client_idx, uint32_t trans_idx)
```

根据客户端标识符（Client ID）生成事务标识符（Transaction ID）的回调 API。

参数说明参见 `sip_svc_plat_format_trans_id()`。

<a id="ab32e31bdba00ff66303fab1b04cd0ebe"></a>

### `sip_svc_plat_free_async_memory_t`

```c
typedef void(* sip_svc_plat_free_async_memory_t) (const struct device *dev, struct sip_svc_request *request)
```

释放异步（ASYNC）数据包中命令缓冲区（Command Buffer）的回调 API。参数说明参见 `sip_svc_plat_free_async_memory()`。

<a id="ac5921c9cdc00604651696e1580f30797"></a>

### `sip_svc_plat_func_id_valid_t`

```c
typedef bool(* sip_svc_plat_func_id_valid_t) (const struct device *dev, uint32_t command, uint32_t func_id)
```

验证监管调用（Supervisory Call）函数标识符（Function ID）的回调 API。

参数说明参见 `sip_svc_plat_func_id_valid()`。

<a id="a926eeecea766b2131c03c57111a186f8"></a>

### `sip_svc_plat_get_error_code_t`

```c
typedef uint32_t(* sip_svc_plat_get_error_code_t) (const struct device *dev, struct arm_smccc_res *res)
```

从监管调用响应（Supervisory Call Response）提取错误码（Error Code）的回调 API。

参数说明参见 `sip_svc_plat_get_error_code()`。

<a id="a35145ddf422e8782b4ec37270b04d98c"></a>

### `sip_svc_plat_get_trans_idx_t`

```c
typedef uint32_t(* sip_svc_plat_get_trans_idx_t) (const struct device *dev, uint32_t trans_id)
```

从事务标识符（Transaction ID）提取客户端事务标识符（Client Transaction ID）的回调 API。参数说明参见 `sip_svc_plat_get_trans_idx()`。

<a id="a9d61db0484e2aacce4515290ffb4450c"></a>

### `sip_svc_plat_update_trans_id_t`

```c
typedef void(* sip_svc_plat_update_trans_id_t) (const struct device *dev, struct sip_svc_request *request, uint32_t trans_id)
```

为发往下层的请求包（Request Packet）更新事务标识符（Transaction ID）的回调 API。参数说明参见 `sip_svc_plat_update_trans_id()`。

<a id="a881e3794f9e29e12c925cb5dbd443420"></a>

### `sip_supervisory_call()`

```c
void sip_supervisory_call ( const struct device * dev, unsigned long function_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm_smccc_res * res )
```

执行 `smc`／`hvc` 调用的监管调用函数（Supervisory Call Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `function_id` | 监管调用（Supervisory Call）的函数标识符（Function Identifier）。 |
| `arg0` | 监管调用（Supervisory Call）的参数 0。 |
| `arg1` | 监管调用（Supervisory Call）的参数 1。 |
| `arg2` | 监管调用（Supervisory Call）的参数 2。 |
| `arg3` | 监管调用（Supervisory Call）的参数 3。 |
| `arg4` | 监管调用（Supervisory Call）的参数 4。 |
| `arg5` | 监管调用（Supervisory Call）的参数 5。 |
| `arg6` | 监管调用（Supervisory Call）的参数 6。 |
| `res` | 指向监管调用响应缓冲区（Response Buffer）的指针。 |

<a id="abb9ff6ec7dea6fc4e104db8cc5e7168b"></a>

### `sip_svc_plat_async_res_req()`

```c
int sip_svc_plat_async_res_req ( const struct device * dev, unsigned long * a0, unsigned long * a1, unsigned long * a2, unsigned long * a3, unsigned long * a4, unsigned long * a5, unsigned long * a6, unsigned long * a7, char * buf, size_t size )
```

设置轮询监管调用（Polling Supervisory Call）的参数。

用于异步响应轮询（ASYNC Polling of Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `a0` | 监管调用（Supervisory Call）的参数 0。 |
| `a1` | 监管调用（Supervisory Call）的参数 1。 |
| `a2` | 监管调用（Supervisory Call）的参数 2。 |
| `a3` | 监管调用（Supervisory Call）的参数 3。 |
| `a4` | 监管调用（Supervisory Call）的参数 4。 |
| `a5` | 监管调用（Supervisory Call）的参数 5。 |
| `a6` | 监管调用（Supervisory Call）的参数 6。 |
| `a7` | 监管调用（Supervisory Call）的参数 7。 |
| `buf` | 响应缓冲区（Response Buffer）指针。 |
| `size` | 响应缓冲区大小（Response Buffer Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="a0a0577249c2a9f470cd6ec0a60b455c8"></a>

### `sip_svc_plat_async_res_res()`

```c
int sip_svc_plat_async_res_res ( const struct device * dev, struct arm_smccc_res * res, char * buf, size_t * size, uint32_t * trans_id )
```

检查轮询监管调用（Polling Supervisory Call）的响应，并获取响应大小（Response Size）和事务标识符（Transaction ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `res` | 指向 `struct arm_smccc_res` 响应的指针。 |
| `buf` | 指向响应缓冲区（Response Buffer）的指针。 |
| `size` | 响应缓冲区（Response Buffer）中响应的大小。 |
| `trans_id` | 响应的事务标识符（Transaction ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 从监管调用（Supervisory Call）获取到有效轮询响应（Polling Response）时。 |
| `-EINPROGRESS` | 未从监管调用（Supervisory Call）获取到有效轮询响应（Polling Response）时。 |

<a id="ae52dee0bbba688a73a9726dd4aa482d2"></a>

### `sip_svc_plat_format_trans_id()`

```c
uint32_t sip_svc_plat_format_trans_id ( const struct device * dev, uint32_t client_idx, uint32_t trans_idx )
```

根据客户端标识符（Client ID），格式化并生成事务标识符（Transaction ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `client_idx` | 客户端索引（Client Index）。 |
| `trans_idx` | 事务索引（Transaction Index）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `transaction` | 用于跟踪每个事务（Transaction）的标识符（ID）。 |

<a id="aa4e44eb2af080207821a60f8b3442886"></a>

### `sip_svc_plat_free_async_memory()`

```c
void sip_svc_plat_free_async_memory ( const struct device * dev, struct sip_svc_request * request )
```

将异步（ASYNC）数据包发送到下层后，释放其使用的命令缓冲区（Command Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `request` | 指向 `sip_svc_request` 数据包的指针。 |

<a id="a8df36a218cce4c0904c147d498c1322d"></a>

### `sip_svc_plat_func_id_valid()`

```c
bool sip_svc_plat_func_id_valid ( const struct device * dev, uint32_t command, uint32_t func_id )
```

验证监管调用（Supervisory Call）的函数标识符（Function ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `command` | 指定调用为同步（SYNC）还是异步（ASYNC）的命令（Command）。 |
| `func_id` | 函数标识符（Function Identifier）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 命令标识符（Command Identifier）和函数标识符（Function Identifier）均有效时。 |
| `false` | 命令标识符（Command Identifier）和函数标识符（Function Identifier）无效时。 |

<a id="a3510743d8cf114376b740f3d297c583f"></a>

### `sip_svc_plat_get_error_code()`

```c
uint32_t sip_svc_plat_get_error_code ( const struct device * dev, struct arm_smccc_res * res )
```

从 `arm_smccc_res` 响应中提取错误码（Error Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `res` | 指向 `struct arm_smccc_res` 响应的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `SIP_SVC_ID_INVALID` | 失败。 |

<a id="ad0e52f49e7db8cf51ff8cf95e1283994"></a>

### `sip_svc_plat_get_trans_idx()`

```c
uint32_t sip_svc_plat_get_trans_idx ( const struct device * dev, uint32_t trans_id )
```

从数据包事务标识符（Packet Transaction ID）提取客户端事务标识符（Client Transaction ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `trans_id` | 针对事务（Transaction）的事务标识符（Transaction Identifier）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 从事务标识符（Transaction ID）中提取事务 ID。 |

<a id="a095123f7aec80a3e51d75ef248990124"></a>

### `sip_svc_plat_update_trans_id()`

```c
void sip_svc_plat_update_trans_id ( const struct device * dev, struct sip_svc_request * request, uint32_t trans_id )
```

为发往下层的 `sip_svc_request` 更新事务标识符（Transaction ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `request` | 指向 `sip_svc_request` 结构体的指针。 |
| `trans_id` | 事务标识符（Transaction ID）。 |


## 14.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/drivers/sip_svc/sip_svc_proto.h](../api_source_reference/P790_sip_svc_proto.h_源码浏览.md)
- [zephyr/sip_svc/sip_svc_controller.h](../api_source_pcie_hid_reference/P008_sip_svc_controller.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P789_sip_svc_driver.h_源码浏览.md)
- [svc_driver_api](../device_power_control_model_reference/P092_svc_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [SIP_SVC_ID_INVALID](../api_file_battery_interrupt_reference/P011_zephyr__drivers__sip_svc__sip_svc_proto.h_文件参考.md#ad1cb9509a40e51809b13f1fccf0f35ba)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_zephyr__sip_svc__sip_svc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__usb__udc.h_文件参考.md)
