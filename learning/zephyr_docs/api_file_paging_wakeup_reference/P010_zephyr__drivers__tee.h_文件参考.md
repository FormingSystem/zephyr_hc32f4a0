---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-10
title: zephyr__drivers__tee.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tee_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_tee.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可信执行环境（Trusted Execution Environment，TEE）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
#include <zephyr/syscalls/tee.h>
```

查看此文件的源码。

可信执行环境（Trusted Execution Environment，TEE）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_tee_5Fversion_5Finfo"></a>

```c
struct tee_version_info
```

相关声明：[tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)。

可信执行环境（TEE）的版本。

<a id="r_tee_5Fopen_5Fsession_5Farg"></a>

```c
struct tee_open_session_arg
```

相关声明：[tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)。

打开会话（Open Session）的参数。

<a id="r_tee_5Fparam"></a>

```c
struct tee_param
```

相关声明：[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

可信执行环境（TEE）的参数。

<a id="r_tee_5Finvoke_5Ffunc_5Farg"></a>

```c
struct tee_invoke_func_arg
```

相关声明：[tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)。

调用可信应用（Trusted Application）中的函数。

<a id="r_tee_5Fshm"></a>

```c
struct tee_shm
```

相关声明：[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

可信执行环境（TEE）的共享内存结构。

<a id="r_tee_5Fdriver_5Fapi"></a>

```c
struct tee_driver_api
```

相关声明：[tee_driver_api](../platform_security_model_reference/P058_tee_driver_api_结构体.md)。

驱动操作（Driver Operations）：可信执行环境（TEE）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga79ff2ca70757daf8e677b42002f4aeac"></a>

```c
#define TEE_UUID_LEN 16
```

相关声明：[TEE_UUID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga79ff2ca70757daf8e677b42002f4aeac)。

<a id="r_ga2eb5a95c2f50e08bbb6235fa47253f10"></a>

```c
#define TEE_GEN_CAP_GP BIT(0) /* GlobalPlatform compliant TEE */
```

相关声明：[TEE_GEN_CAP_GP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2eb5a95c2f50e08bbb6235fa47253f10)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga15e96022b209b84d29c29f213aab0331"></a>

```c
#define TEE_GEN_CAP_PRIVILEGED BIT(1) /* Privileged device (for supplicant) */
```

相关声明：[TEE_GEN_CAP_PRIVILEGED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga15e96022b209b84d29c29f213aab0331)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gae661041c8b0f0638891a5a82b74aa928"></a>

```c
#define TEE_GEN_CAP_REG_MEM BIT(2) /* Supports registering shared memory */
```

相关声明：[TEE_GEN_CAP_REG_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae661041c8b0f0638891a5a82b74aa928)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga4cd66a4425e312338823061e561638de"></a>

```c
#define TEE_GEN_CAP_MEMREF_NULL BIT(3) /* Support NULL MemRef */
```

相关声明：[TEE_GEN_CAP_MEMREF_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga4cd66a4425e312338823061e561638de)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga2fac25b74105b1ddfb15db51598b89c8"></a>

```c
#define TEE_SHM_REGISTER BIT(0)
```

相关声明：[TEE_SHM_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2fac25b74105b1ddfb15db51598b89c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga85fd3e6e6b596da02c97661a35c9814c"></a>

```c
#define TEE_SHM_ALLOC BIT(1)
```

相关声明：[TEE_SHM_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga85fd3e6e6b596da02c97661a35c9814c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gad3f8bf86812e0e5befa873389235ddd9"></a>

```c
#define TEE_PARAM_ATTR_TYPE_NONE 0 /* parameter not used */
```

相关声明：[TEE_PARAM_ATTR_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad3f8bf86812e0e5befa873389235ddd9)。

<a id="r_ga5304d0bdbfb80563bdf3bd801cc72613"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INPUT 1
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga5304d0bdbfb80563bdf3bd801cc72613)。

<a id="r_gaf66e35aefb70c34cba93eeb5f3cb0f8a"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT 2
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf66e35aefb70c34cba93eeb5f3cb0f8a)。

<a id="r_ga925026258aed48470a015a655f25b270"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INOUT 3 /* input and output */
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_INOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga925026258aed48470a015a655f25b270)。

<a id="r_ga0c7f0c79fd599a2d5ec2759230bff6e7"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INPUT 5
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0c7f0c79fd599a2d5ec2759230bff6e7)。

<a id="r_ga5305a53edb649a22c774731bf2f53987"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT 6
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga5305a53edb649a22c774731bf2f53987)。

<a id="r_ga43fcdc052991d21fc7fde3720256ef2c"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INOUT 7 /* input and output */
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_INOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga43fcdc052991d21fc7fde3720256ef2c)。

<a id="r_ga8e2dca32129d730d9394f0798d578ce7"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MASK 0xff
```

相关声明：[TEE_PARAM_ATTR_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8e2dca32129d730d9394f0798d578ce7)。

<a id="r_ga42e96de713673837d60ac3b938373206"></a>

```c
#define TEE_PARAM_ATTR_META 0x100
```

相关声明：[TEE_PARAM_ATTR_META](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga42e96de713673837d60ac3b938373206)。

<a id="r_ga15358e8f86ca9a2b6aca9899ee982542"></a>

```c
#define TEE_PARAM_ATTR_MASK (TEE_PARAM_ATTR_TYPE_MASK | TEE_PARAM_ATTR_META)
```

相关声明：[TEE_PARAM_ATTR_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga15358e8f86ca9a2b6aca9899ee982542)、[TEE_PARAM_ATTR_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8e2dca32129d730d9394f0798d578ce7)、[TEE_PARAM_ATTR_META](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga42e96de713673837d60ac3b938373206)。

<a id="r_ga6040bf64a72a13c675681c99112f7f69"></a>

```c
#define TEEC_ORIGIN_API 0x00000001
```

相关声明：[TEEC_ORIGIN_API](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6040bf64a72a13c675681c99112f7f69)。

函数错误来源（Function Error Origins），类型为 `TEEC_ErrorOrigin`。

<a id="r_ga668c5799e8360e3e885a908784805578"></a>

```c
#define TEEC_ORIGIN_COMMS 0x00000002
```

相关声明：[TEEC_ORIGIN_COMMS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga668c5799e8360e3e885a908784805578)。

<a id="r_gabebf4008dbbf440ac352d510675c9433"></a>

```c
#define TEEC_ORIGIN_TEE 0x00000003
```

相关声明：[TEEC_ORIGIN_TEE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gabebf4008dbbf440ac352d510675c9433)。

<a id="r_gaebb73e90a25eeecc5ac274c2c396f32f"></a>

```c
#define TEEC_ORIGIN_TRUSTED_APP 0x00000004
```

相关声明：[TEEC_ORIGIN_TRUSTED_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaebb73e90a25eeecc5ac274c2c396f32f)。

<a id="r_gae000299e1a48b8e9c807c8e1b7e62aed"></a>

```c
#define TEEC_SUCCESS 0x00000000
```

相关声明：[TEEC_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae000299e1a48b8e9c807c8e1b7e62aed)。

返回值（Return Values）。

<a id="r_gad9e7d08ba6637d86cf611952b9842568"></a>

```c
#define TEEC_ERROR_STORAGE_NOT_AVAILABLE 0xF0100003
```

相关声明：[TEEC_ERROR_STORAGE_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad9e7d08ba6637d86cf611952b9842568)。

<a id="r_ga13c7ed6f37eba36870e4b138b661b61f"></a>

```c
#define TEEC_ERROR_GENERIC 0xFFFF0000
```

相关声明：[TEEC_ERROR_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga13c7ed6f37eba36870e4b138b661b61f)。

<a id="r_gad7c7cd2ed537347d60276bd08375ca30"></a>

```c
#define TEEC_ERROR_ACCESS_DENIED 0xFFFF0001
```

相关声明：[TEEC_ERROR_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c7cd2ed537347d60276bd08375ca30)。

<a id="r_ga8cbe25a679add519a048c85c03be1ede"></a>

```c
#define TEEC_ERROR_CANCEL 0xFFFF0002
```

相关声明：[TEEC_ERROR_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8cbe25a679add519a048c85c03be1ede)。

<a id="r_ga65a8bd0582ef42f84e85704bab5a85fe"></a>

```c
#define TEEC_ERROR_ACCESS_CONFLICT 0xFFFF0003
```

相关声明：[TEEC_ERROR_ACCESS_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga65a8bd0582ef42f84e85704bab5a85fe)。

<a id="r_gad8825a36962871ac2006386d18a821e7"></a>

```c
#define TEEC_ERROR_EXCESS_DATA 0xFFFF0004
```

相关声明：[TEEC_ERROR_EXCESS_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad8825a36962871ac2006386d18a821e7)。

<a id="r_ga0e08a22cf7abe05ae2d0cfd7fe92b0e7"></a>

```c
#define TEEC_ERROR_BAD_FORMAT 0xFFFF0005
```

相关声明：[TEEC_ERROR_BAD_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)。

<a id="r_ga79b607eb603bef58b3065a3014ee7117"></a>

```c
#define TEEC_ERROR_BAD_PARAMETERS 0xFFFF0006
```

相关声明：[TEEC_ERROR_BAD_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga79b607eb603bef58b3065a3014ee7117)。

<a id="r_ga19c6e3eb278dd58fa49b7de3dff8b7ac"></a>

```c
#define TEEC_ERROR_BAD_STATE 0xFFFF0007
```

相关声明：[TEEC_ERROR_BAD_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga19c6e3eb278dd58fa49b7de3dff8b7ac)。

<a id="r_ga805299b26fda6bb38a97cf6a0825431d"></a>

```c
#define TEEC_ERROR_ITEM_NOT_FOUND 0xFFFF0008
```

相关声明：[TEEC_ERROR_ITEM_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga805299b26fda6bb38a97cf6a0825431d)。

<a id="r_gaa7ef60306699f14fa7f3bcd6ed744633"></a>

```c
#define TEEC_ERROR_NOT_IMPLEMENTED 0xFFFF0009
```

相关声明：[TEEC_ERROR_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaa7ef60306699f14fa7f3bcd6ed744633)。

<a id="r_ga17041726bc43fb2a1aa3ddc927ac6cef"></a>

```c
#define TEEC_ERROR_NOT_SUPPORTED 0xFFFF000A
```

相关声明：[TEEC_ERROR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga17041726bc43fb2a1aa3ddc927ac6cef)。

<a id="r_gaf515dfd970be2caf575be186dd32afd7"></a>

```c
#define TEEC_ERROR_NO_DATA 0xFFFF000B
```

相关声明：[TEEC_ERROR_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf515dfd970be2caf575be186dd32afd7)。

<a id="r_gac7aaf1249147ecd63d6fba179e26ad33"></a>

```c
#define TEEC_ERROR_OUT_OF_MEMORY 0xFFFF000C
```

相关声明：[TEEC_ERROR_OUT_OF_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gac7aaf1249147ecd63d6fba179e26ad33)。

<a id="r_ga28d244820db7caa7cb829ed3469f5961"></a>

```c
#define TEEC_ERROR_BUSY 0xFFFF000D
```

相关声明：[TEEC_ERROR_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga28d244820db7caa7cb829ed3469f5961)。

<a id="r_ga0a3047b67556c437e80c308853705de2"></a>

```c
#define TEEC_ERROR_COMMUNICATION 0xFFFF000E
```

相关声明：[TEEC_ERROR_COMMUNICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0a3047b67556c437e80c308853705de2)。

<a id="r_gaae2b6bb8d476d422f782e7ac226de21b"></a>

```c
#define TEEC_ERROR_SECURITY 0xFFFF000F
```

相关声明：[TEEC_ERROR_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaae2b6bb8d476d422f782e7ac226de21b)。

<a id="r_ga511a0747fab1c307a5263a07ce396962"></a>

```c
#define TEEC_ERROR_SHORT_BUFFER 0xFFFF0010
```

相关声明：[TEEC_ERROR_SHORT_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga511a0747fab1c307a5263a07ce396962)。

<a id="r_ga10e9a718e8ce09e6fe117bc0b002a3d6"></a>

```c
#define TEEC_ERROR_EXTERNAL_CANCEL 0xFFFF0011
```

相关声明：[TEEC_ERROR_EXTERNAL_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga10e9a718e8ce09e6fe117bc0b002a3d6)。

<a id="r_ga6aa8da2d81b77fb8d2ec16f4e3a27528"></a>

```c
#define TEEC_ERROR_TARGET_DEAD 0xFFFF3024
```

相关声明：[TEEC_ERROR_TARGET_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6aa8da2d81b77fb8d2ec16f4e3a27528)。

<a id="r_ga6229f84eb575bf10c14b40f02495b46e"></a>

```c
#define TEEC_ERROR_STORAGE_NO_SPACE 0xFFFF3041
```

相关声明：[TEEC_ERROR_STORAGE_NO_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6229f84eb575bf10c14b40f02495b46e)。

<a id="r_ga16baa8eb95393514c6035c957ad55a6b"></a>

```c
#define TEEC_LOGIN_PUBLIC 0x00000000
```

相关声明：[TEEC_LOGIN_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga16baa8eb95393514c6035c957ad55a6b)。

会话登录方法（Session Login Methods），用作 `tee_open_session()` 的 `connectionMethod` 参数。

<a id="r_gab6940dd1f636aa67e74a8615e8544f85"></a>

```c
#define TEEC_LOGIN_USER 0x00000001
```

相关声明：[TEEC_LOGIN_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gab6940dd1f636aa67e74a8615e8544f85)。

<a id="r_ga8cdd4a2102e18a60d0624d610ef3619e"></a>

```c
#define TEEC_LOGIN_GROUP 0x00000002
```

相关声明：[TEEC_LOGIN_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8cdd4a2102e18a60d0624d610ef3619e)。

<a id="r_gae803496f14c6cc84b7f56174006c16a6"></a>

```c
#define TEEC_LOGIN_APPLICATION 0x00000004
```

相关声明：[TEEC_LOGIN_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae803496f14c6cc84b7f56174006c16a6)。

<a id="r_ga37fbb624e8c289d400cd69948bf8b505"></a>

```c
#define TEEC_LOGIN_USER_APPLICATION 0x00000005
```

相关声明：[TEEC_LOGIN_USER_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga37fbb624e8c289d400cd69948bf8b505)。

<a id="r_gad1da184306fe0283fc1e618f829119e3"></a>

```c
#define TEEC_LOGIN_GROUP_APPLICATION 0x00000006
```

相关声明：[TEEC_LOGIN_GROUP_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad1da184306fe0283fc1e618f829119e3)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.3\_类型定义（Typedefs）

<a id="r_gac533d9e85d65857c0d984506024a55b4"></a>

```c
typedef int(* tee_get_version_t) (const struct device *dev, struct tee_version_info *info)
```

相关声明：[tee_get_version_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac533d9e85d65857c0d984506024a55b4)、[device](../device_reference/P002_设备对象结构.md)、[tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)。

获取当前可信执行环境（TEE）版本的回调 API。

<a id="r_gaf972199fcdbd892688dc141ddba6e6aa"></a>

```c
typedef int(* tee_open_session_t) (const struct device *dev, struct tee_open_session_arg *arg, unsigned int num_param, struct tee_param *param, uint32_t *session_id)
```

相关声明：[tee_open_session_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gaf972199fcdbd892688dc141ddba6e6aa)、[device](../device_reference/P002_设备对象结构.md)、[tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

打开到可信应用（Trusted Application，TA）的会话（Session）的回调 API。

<a id="r_gac412f57a3da187e6e272857d5bdaaaeb"></a>

```c
typedef int(* tee_close_session_t) (const struct device *dev, uint32_t session_id)
```

相关声明：[tee_close_session_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac412f57a3da187e6e272857d5bdaaaeb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

关闭到可信应用（TA）的会话（Session）的回调 API。

<a id="r_gad4cd5b65cac3eb7b4338fd99eeb13a93"></a>

```c
typedef int(* tee_cancel_t) (const struct device *dev, uint32_t session_id, uint32_t cancel_id)
```

相关声明：[tee_cancel_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gad4cd5b65cac3eb7b4338fd99eeb13a93)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

取消面向可信应用（TA）的会话打开或函数调用（Open Session or Invoke Function）的回调 API。原文的 `open session of invoke function` 按上下文理解为两类可取消操作。

<a id="r_gac3695e51dc8b08bb5e5c5d984c402b0e"></a>

```c
typedef int(* tee_invoke_func_t) (const struct device *dev, struct tee_invoke_func_arg *arg, unsigned int num_param, struct tee_param *param)
```

相关声明：[tee_invoke_func_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac3695e51dc8b08bb5e5c5d984c402b0e)、[device](../device_reference/P002_设备对象结构.md)、[tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

调用可信应用（TA）中函数（Function）的回调 API。

<a id="r_ga9e2807d34d580c012129a2fc1f5a425a"></a>

```c
typedef int(* tee_shm_register_t) (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_register_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga9e2807d34d580c012129a2fc1f5a425a)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注册共享内存（Shared Memory）的回调 API。

<a id="r_ga2ea18e713a101a6ca715baa04c2f4185"></a>

```c
typedef int(* tee_shm_unregister_t) (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_unregister_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga2ea18e713a101a6ca715baa04c2f4185)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注销共享内存（Shared Memory）的回调 API。

<a id="r_gaae68677cbff1e831fadc3d188c8588ff"></a>

```c
typedef int(* tee_suppl_recv_t) (const struct device *dev, uint32_t *func, unsigned int *num_params, struct tee_param *param)
```

相关声明：[tee_suppl_recv_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gaae68677cbff1e831fadc3d188c8588ff)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）接收请求（Request）的回调 API。

<a id="r_ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20"></a>

```c
typedef int(* tee_suppl_send_t) (const struct device *dev, unsigned int ret, unsigned int num_params, struct tee_param *param)
```

相关声明：[tee_suppl_send_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）发送请求（Request）的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_gadaaec6b6ea29d81f36943bbe5bcb305e"></a>

```c
int tee_get_version (const struct device *dev, struct tee_version_info *info)
```

相关声明：[tee_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gadaaec6b6ea29d81f36943bbe5bcb305e)、[device](../device_reference/P002_设备对象结构.md)、[tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)。

获取当前可信执行环境（TEE）版本信息（Version Info）。

<a id="r_gad7c66e32d5b02c42c698bd422cf43523"></a>

```c
int tee_open_session (const struct device *dev, struct tee_open_session_arg *arg, unsigned int num_param, struct tee_param *param, uint32_t *session_id)
```

相关声明：[tee_open_session](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c66e32d5b02c42c698bd422cf43523)、[device](../device_reference/P002_设备对象结构.md)、[tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为可信环境（Trusted Environment）打开会话（Session）。

<a id="r_gacb1d58002378a11d92361a149d451241"></a>

```c
int tee_close_session (const struct device *dev, uint32_t session_id)
```

相关声明：[tee_close_session](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gacb1d58002378a11d92361a149d451241)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

关闭可信环境（Trusted Environment）会话（Session）。

<a id="r_ga34fbbfe48a07541041ffddb9e318332a"></a>

```c
int tee_cancel (const struct device *dev, uint32_t session_id, uint32_t cancel_id)
```

相关声明：[tee_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga34fbbfe48a07541041ffddb9e318332a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

取消可信环境（Trusted Environment）的会话或函数调用（Session or Invoke Function）。

<a id="r_gae1337f293febcecc7dbc79ac064e7824"></a>

```c
int tee_invoke_func (const struct device *dev, struct tee_invoke_func_arg *arg, unsigned int num_param, struct tee_param *param)
```

相关声明：[tee_invoke_func](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae1337f293febcecc7dbc79ac064e7824)、[device](../device_reference/P002_设备对象结构.md)、[tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

调用可信环境应用（Trusted Environment Application）的函数。

<a id="r_gade7fdbece8b0bd47f5d148572016c4ef"></a>

```c
int tee_add_shm (const struct device *dev, void *addr, size_t align, size_t size, uint32_t flags, struct tee_shm **shmp)
```

相关声明：[tee_add_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade7fdbece8b0bd47f5d148572016c4ef)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

分配并注册共享内存（Shared Memory）的辅助函数。

<a id="r_gaf53521a3e3a36a9827753716bef1434f"></a>

```c
int tee_rm_shm (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_rm_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf53521a3e3a36a9827753716bef1434f)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

移除并注销共享内存（Shared Memory）的辅助函数。

<a id="r_ga1565c23104792203ede9d9cb388ff782"></a>

```c
int tee_shm_register (const struct device *dev, void *addr, size_t size, uint32_t flags, struct tee_shm **shm)
```

相关声明：[tee_shm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga1565c23104792203ede9d9cb388ff782)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

为可信环境（Trusted Environment）注册共享内存（Shared Memory）。

<a id="r_gade2c0e7d89e3594707637b62a1901bac"></a>

```c
int tee_shm_unregister (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade2c0e7d89e3594707637b62a1901bac)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注销可信环境（Trusted Environment）的共享内存（Shared Memory）。

<a id="r_ga47f7403e2b136f755432159c7bd679a5"></a>

```c
int tee_shm_alloc (const struct device *dev, size_t size, uint32_t flags, struct tee_shm **shm)
```

相关声明：[tee_shm_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga47f7403e2b136f755432159c7bd679a5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

为可信环境（Trusted Environment）分配共享内存区域（Shared Memory Region）。

<a id="r_ga346d8d67a18542c097f1254c0ace8726"></a>

```c
int tee_shm_free (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_free](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga346d8d67a18542c097f1254c0ace8726)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

释放可信环境（Trusted Environment）的共享内存区域（Shared Memory Region）。

<a id="r_ga2213f63da1f080beaedc169e13531a37"></a>

```c
int tee_suppl_recv (const struct device *dev, uint32_t *func, unsigned int *num_params, struct tee_param *param)
```

相关声明：[tee_suppl_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2213f63da1f080beaedc169e13531a37)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）接收请求。

<a id="r_ga93cccfa446983be704f364760bf7567b"></a>

```c
int tee_suppl_send (const struct device *dev, unsigned int ret, unsigned int num_params, struct tee_param *param)
```

相关声明：[tee_suppl_send](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga93cccfa446983be704f364760bf7567b)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）函数发送请求。


## 10.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_network_reference/P021_tee.h_源码浏览.md)
- [tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)
- [tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)
- [tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)
- [tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)
- [tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)
- [tee_driver_api](../platform_security_model_reference/P058_tee_driver_api_结构体.md)
- [TEE_UUID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga79ff2ca70757daf8e677b42002f4aeac)
- [TEE_GEN_CAP_GP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2eb5a95c2f50e08bbb6235fa47253f10)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [TEE_GEN_CAP_PRIVILEGED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga15e96022b209b84d29c29f213aab0331)
- [device](../device_reference/P002_设备对象结构.md)
- [TEE_GEN_CAP_REG_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae661041c8b0f0638891a5a82b74aa928)
- [TEE_GEN_CAP_MEMREF_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga4cd66a4425e312338823061e561638de)
- [TEE_SHM_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2fac25b74105b1ddfb15db51598b89c8)
- [TEE_SHM_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga85fd3e6e6b596da02c97661a35c9814c)
- [TEE_PARAM_ATTR_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad3f8bf86812e0e5befa873389235ddd9)
- [TEE_PARAM_ATTR_TYPE_VALUE_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga5304d0bdbfb80563bdf3bd801cc72613)
- [TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf66e35aefb70c34cba93eeb5f3cb0f8a)
- [TEE_PARAM_ATTR_TYPE_VALUE_INOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga925026258aed48470a015a655f25b270)
- [TEE_PARAM_ATTR_TYPE_MEMREF_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0c7f0c79fd599a2d5ec2759230bff6e7)
- [TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga5305a53edb649a22c774731bf2f53987)
- [TEE_PARAM_ATTR_TYPE_MEMREF_INOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga43fcdc052991d21fc7fde3720256ef2c)
- [TEE_PARAM_ATTR_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8e2dca32129d730d9394f0798d578ce7)
- [TEE_PARAM_ATTR_META](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga42e96de713673837d60ac3b938373206)
- [TEE_PARAM_ATTR_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga15358e8f86ca9a2b6aca9899ee982542)
- [TEEC_ORIGIN_API](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6040bf64a72a13c675681c99112f7f69)
- [TEEC_ORIGIN_COMMS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga668c5799e8360e3e885a908784805578)
- [TEEC_ORIGIN_TEE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gabebf4008dbbf440ac352d510675c9433)
- [TEEC_ORIGIN_TRUSTED_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaebb73e90a25eeecc5ac274c2c396f32f)
- [TEEC_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae000299e1a48b8e9c807c8e1b7e62aed)
- [TEEC_ERROR_STORAGE_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad9e7d08ba6637d86cf611952b9842568)
- [TEEC_ERROR_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga13c7ed6f37eba36870e4b138b661b61f)
- [TEEC_ERROR_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c7cd2ed537347d60276bd08375ca30)
- [TEEC_ERROR_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8cbe25a679add519a048c85c03be1ede)
- [TEEC_ERROR_ACCESS_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga65a8bd0582ef42f84e85704bab5a85fe)
- [TEEC_ERROR_EXCESS_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad8825a36962871ac2006386d18a821e7)
- [TEEC_ERROR_BAD_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)
- [TEEC_ERROR_BAD_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga79b607eb603bef58b3065a3014ee7117)
- [TEEC_ERROR_BAD_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga19c6e3eb278dd58fa49b7de3dff8b7ac)
- [TEEC_ERROR_ITEM_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga805299b26fda6bb38a97cf6a0825431d)
- [TEEC_ERROR_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaa7ef60306699f14fa7f3bcd6ed744633)
- [TEEC_ERROR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga17041726bc43fb2a1aa3ddc927ac6cef)
- [TEEC_ERROR_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf515dfd970be2caf575be186dd32afd7)
- [TEEC_ERROR_OUT_OF_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gac7aaf1249147ecd63d6fba179e26ad33)
- [TEEC_ERROR_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga28d244820db7caa7cb829ed3469f5961)
- [TEEC_ERROR_COMMUNICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga0a3047b67556c437e80c308853705de2)
- [TEEC_ERROR_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaae2b6bb8d476d422f782e7ac226de21b)
- [TEEC_ERROR_SHORT_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga511a0747fab1c307a5263a07ce396962)
- [TEEC_ERROR_EXTERNAL_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga10e9a718e8ce09e6fe117bc0b002a3d6)
- [TEEC_ERROR_TARGET_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6aa8da2d81b77fb8d2ec16f4e3a27528)
- [TEEC_ERROR_STORAGE_NO_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga6229f84eb575bf10c14b40f02495b46e)
- [TEEC_LOGIN_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga16baa8eb95393514c6035c957ad55a6b)
- [tee_open_session()](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c66e32d5b02c42c698bd422cf43523)
- [TEEC_LOGIN_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gab6940dd1f636aa67e74a8615e8544f85)
- [TEEC_LOGIN_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga8cdd4a2102e18a60d0624d610ef3619e)
- [TEEC_LOGIN_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae803496f14c6cc84b7f56174006c16a6)
- [TEEC_LOGIN_USER_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga37fbb624e8c289d400cd69948bf8b505)
- [TEEC_LOGIN_GROUP_APPLICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad1da184306fe0283fc1e618f829119e3)
- [tee_get_version_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac533d9e85d65857c0d984506024a55b4)
- [tee_open_session_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gaf972199fcdbd892688dc141ddba6e6aa)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tee_close_session_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac412f57a3da187e6e272857d5bdaaaeb)
- [tee_cancel_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gad4cd5b65cac3eb7b4338fd99eeb13a93)
- [tee_invoke_func_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gac3695e51dc8b08bb5e5c5d984c402b0e)
- [tee_shm_register_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga9e2807d34d580c012129a2fc1f5a425a)
- [tee_shm_unregister_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga2ea18e713a101a6ca715baa04c2f4185)
- [tee_suppl_recv_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#gaae68677cbff1e831fadc3d188c8588ff)
- [tee_suppl_send_t](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)
- [tee_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gadaaec6b6ea29d81f36943bbe5bcb305e)
- [tee_close_session](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gacb1d58002378a11d92361a149d451241)
- [tee_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga34fbbfe48a07541041ffddb9e318332a)
- [tee_invoke_func](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae1337f293febcecc7dbc79ac064e7824)
- [tee_add_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade7fdbece8b0bd47f5d148572016c4ef)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [tee_rm_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf53521a3e3a36a9827753716bef1434f)
- [tee_shm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga1565c23104792203ede9d9cb388ff782)
- [tee_shm_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade2c0e7d89e3594707637b62a1901bac)
- [tee_shm_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga47f7403e2b136f755432159c7bd679a5)
- [tee_shm_free](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga346d8d67a18542c097f1254c0ace8726)
- [tee_suppl_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2213f63da1f080beaedc169e13531a37)
- [tee_suppl_send](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga93cccfa446983be704f364760bf7567b)

<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__gpio__stmod-plus-connector.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__dt-bindings__timer__ti-dmtimer.h_文件参考.md)
