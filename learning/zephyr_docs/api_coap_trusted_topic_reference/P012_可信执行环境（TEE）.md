---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-12
title: 可信执行环境（TEE）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_可信执行环境（TEE）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与可信执行环境（Trusted Execution Environment，TEE）交互的接口。

<a id="details"></a>

用于可信执行环境（Trusted Execution Environment，TEE）的接口。自 3.7 起提供（Since 3.7），版本（Version）0.1.0。这里提供与 TEE 交互的通用接口。TEE 是运行在安全空间（Secure Space）中的可信操作系统（Trusted OS），例如 ARM CPU 的 TrustZone；也可以采用独立安全协处理器（Secure Co-processor）的形式。它使系统能够实现与普通世界（Normal World）隔离的逻辑。TEE 系统调用（Syscalls）的用法如下：

- tee_get_version()：获取当前 TEE 能力（Capabilities）。
- tee_open_session()：打开到可信应用（Trusted Application，TA）的新会话（Session）。
- tee_close_session()：关闭到 TA 的会话。
- tee_cancel()：取消会话或函数调用。
- tee_invoke_func()：调用 TA 中的函数。
- tee_shm_register()：注册共享内存区域（Shared Memory Region）。
- tee_shm_unregister()：注销共享内存区域。
- tee_shm_alloc()：分配共享内存区域。
- tee_shm_free()：释放共享内存区域。

<a id="header-groups"></a>
<a id="groups"></a>

## 12.1\_主题（Topics）

<a id="r_tee_5Finterface_5Fbackend"></a>

相关声明：[TEE 驱动后端 API](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 12.2\_文件（Files）

<a id="r_tee_2Eh"></a>

```c
file tee.h
```

相关声明：[tee.h](../api_file_paging_wakeup_reference/P010_zephyr__drivers__tee.h_文件参考.md)。

可信执行环境（Trusted Execution Environment，TEE）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.4\_宏定义（Macros）

<a id="r_ga79ff2ca70757daf8e677b42002f4aeac"></a>

```c
#define TEE_UUID_LEN 16
```

相关声明：[TEE_UUID_LEN](#ga79ff2ca70757daf8e677b42002f4aeac)。

<a id="r_ga2eb5a95c2f50e08bbb6235fa47253f10"></a>

```c
#define TEE_GEN_CAP_GP BIT(0) /* GlobalPlatform compliant TEE */
```

相关声明：[TEE_GEN_CAP_GP](#ga2eb5a95c2f50e08bbb6235fa47253f10)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga15e96022b209b84d29c29f213aab0331"></a>

```c
#define TEE_GEN_CAP_PRIVILEGED BIT(1) /* Privileged device (for supplicant) */
```

相关声明：[TEE_GEN_CAP_PRIVILEGED](#ga15e96022b209b84d29c29f213aab0331)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gae661041c8b0f0638891a5a82b74aa928"></a>

```c
#define TEE_GEN_CAP_REG_MEM BIT(2) /* Supports registering shared memory */
```

相关声明：[TEE_GEN_CAP_REG_MEM](#gae661041c8b0f0638891a5a82b74aa928)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga4cd66a4425e312338823061e561638de"></a>

```c
#define TEE_GEN_CAP_MEMREF_NULL BIT(3) /* Support NULL MemRef */
```

相关声明：[TEE_GEN_CAP_MEMREF_NULL](#ga4cd66a4425e312338823061e561638de)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga2fac25b74105b1ddfb15db51598b89c8"></a>

```c
#define TEE_SHM_REGISTER BIT(0)
```

相关声明：[TEE_SHM_REGISTER](#ga2fac25b74105b1ddfb15db51598b89c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga85fd3e6e6b596da02c97661a35c9814c"></a>

```c
#define TEE_SHM_ALLOC BIT(1)
```

相关声明：[TEE_SHM_ALLOC](#ga85fd3e6e6b596da02c97661a35c9814c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gad3f8bf86812e0e5befa873389235ddd9"></a>

```c
#define TEE_PARAM_ATTR_TYPE_NONE 0 /* parameter not used */
```

相关声明：[TEE_PARAM_ATTR_TYPE_NONE](#gad3f8bf86812e0e5befa873389235ddd9)。

<a id="r_ga5304d0bdbfb80563bdf3bd801cc72613"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INPUT 1
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_INPUT](#ga5304d0bdbfb80563bdf3bd801cc72613)。

<a id="r_gaf66e35aefb70c34cba93eeb5f3cb0f8a"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT 2
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT](#gaf66e35aefb70c34cba93eeb5f3cb0f8a)。

<a id="r_ga925026258aed48470a015a655f25b270"></a>

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INOUT 3 /* input and output */
```

相关声明：[TEE_PARAM_ATTR_TYPE_VALUE_INOUT](#ga925026258aed48470a015a655f25b270)。

<a id="r_ga0c7f0c79fd599a2d5ec2759230bff6e7"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INPUT 5
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_INPUT](#ga0c7f0c79fd599a2d5ec2759230bff6e7)。

<a id="r_ga5305a53edb649a22c774731bf2f53987"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT 6
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT](#ga5305a53edb649a22c774731bf2f53987)。

<a id="r_ga43fcdc052991d21fc7fde3720256ef2c"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INOUT 7 /* input and output */
```

相关声明：[TEE_PARAM_ATTR_TYPE_MEMREF_INOUT](#ga43fcdc052991d21fc7fde3720256ef2c)。

<a id="r_ga8e2dca32129d730d9394f0798d578ce7"></a>

```c
#define TEE_PARAM_ATTR_TYPE_MASK 0xff
```

相关声明：[TEE_PARAM_ATTR_TYPE_MASK](#ga8e2dca32129d730d9394f0798d578ce7)。

<a id="r_ga42e96de713673837d60ac3b938373206"></a>

```c
#define TEE_PARAM_ATTR_META 0x100
```

相关声明：[TEE_PARAM_ATTR_META](#ga42e96de713673837d60ac3b938373206)。

<a id="r_ga15358e8f86ca9a2b6aca9899ee982542"></a>

```c
#define TEE_PARAM_ATTR_MASK (TEE_PARAM_ATTR_TYPE_MASK | TEE_PARAM_ATTR_META)
```

相关声明：[TEE_PARAM_ATTR_MASK](#ga15358e8f86ca9a2b6aca9899ee982542)、[TEE_PARAM_ATTR_TYPE_MASK](#ga8e2dca32129d730d9394f0798d578ce7)、[TEE_PARAM_ATTR_META](#ga42e96de713673837d60ac3b938373206)。

<a id="r_ga6040bf64a72a13c675681c99112f7f69"></a>

```c
#define TEEC_ORIGIN_API 0x00000001
```

相关声明：[TEEC_ORIGIN_API](#ga6040bf64a72a13c675681c99112f7f69)。

函数错误来源（Function Error Origins），类型为 `TEEC_ErrorOrigin`。

<a id="r_ga668c5799e8360e3e885a908784805578"></a>

```c
#define TEEC_ORIGIN_COMMS 0x00000002
```

相关声明：[TEEC_ORIGIN_COMMS](#ga668c5799e8360e3e885a908784805578)。

<a id="r_gabebf4008dbbf440ac352d510675c9433"></a>

```c
#define TEEC_ORIGIN_TEE 0x00000003
```

相关声明：[TEEC_ORIGIN_TEE](#gabebf4008dbbf440ac352d510675c9433)。

<a id="r_gaebb73e90a25eeecc5ac274c2c396f32f"></a>

```c
#define TEEC_ORIGIN_TRUSTED_APP 0x00000004
```

相关声明：[TEEC_ORIGIN_TRUSTED_APP](#gaebb73e90a25eeecc5ac274c2c396f32f)。

<a id="r_gae000299e1a48b8e9c807c8e1b7e62aed"></a>

```c
#define TEEC_SUCCESS 0x00000000
```

相关声明：[TEEC_SUCCESS](#gae000299e1a48b8e9c807c8e1b7e62aed)。

返回值（Return Values）。

<a id="r_gad9e7d08ba6637d86cf611952b9842568"></a>

```c
#define TEEC_ERROR_STORAGE_NOT_AVAILABLE 0xF0100003
```

相关声明：[TEEC_ERROR_STORAGE_NOT_AVAILABLE](#gad9e7d08ba6637d86cf611952b9842568)。

<a id="r_ga13c7ed6f37eba36870e4b138b661b61f"></a>

```c
#define TEEC_ERROR_GENERIC 0xFFFF0000
```

相关声明：[TEEC_ERROR_GENERIC](#ga13c7ed6f37eba36870e4b138b661b61f)。

<a id="r_gad7c7cd2ed537347d60276bd08375ca30"></a>

```c
#define TEEC_ERROR_ACCESS_DENIED 0xFFFF0001
```

相关声明：[TEEC_ERROR_ACCESS_DENIED](#gad7c7cd2ed537347d60276bd08375ca30)。

<a id="r_ga8cbe25a679add519a048c85c03be1ede"></a>

```c
#define TEEC_ERROR_CANCEL 0xFFFF0002
```

相关声明：[TEEC_ERROR_CANCEL](#ga8cbe25a679add519a048c85c03be1ede)。

<a id="r_ga65a8bd0582ef42f84e85704bab5a85fe"></a>

```c
#define TEEC_ERROR_ACCESS_CONFLICT 0xFFFF0003
```

相关声明：[TEEC_ERROR_ACCESS_CONFLICT](#ga65a8bd0582ef42f84e85704bab5a85fe)。

<a id="r_gad8825a36962871ac2006386d18a821e7"></a>

```c
#define TEEC_ERROR_EXCESS_DATA 0xFFFF0004
```

相关声明：[TEEC_ERROR_EXCESS_DATA](#gad8825a36962871ac2006386d18a821e7)。

<a id="r_ga0e08a22cf7abe05ae2d0cfd7fe92b0e7"></a>

```c
#define TEEC_ERROR_BAD_FORMAT 0xFFFF0005
```

相关声明：[TEEC_ERROR_BAD_FORMAT](#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)。

<a id="r_ga79b607eb603bef58b3065a3014ee7117"></a>

```c
#define TEEC_ERROR_BAD_PARAMETERS 0xFFFF0006
```

相关声明：[TEEC_ERROR_BAD_PARAMETERS](#ga79b607eb603bef58b3065a3014ee7117)。

<a id="r_ga19c6e3eb278dd58fa49b7de3dff8b7ac"></a>

```c
#define TEEC_ERROR_BAD_STATE 0xFFFF0007
```

相关声明：[TEEC_ERROR_BAD_STATE](#ga19c6e3eb278dd58fa49b7de3dff8b7ac)。

<a id="r_ga805299b26fda6bb38a97cf6a0825431d"></a>

```c
#define TEEC_ERROR_ITEM_NOT_FOUND 0xFFFF0008
```

相关声明：[TEEC_ERROR_ITEM_NOT_FOUND](#ga805299b26fda6bb38a97cf6a0825431d)。

<a id="r_gaa7ef60306699f14fa7f3bcd6ed744633"></a>

```c
#define TEEC_ERROR_NOT_IMPLEMENTED 0xFFFF0009
```

相关声明：[TEEC_ERROR_NOT_IMPLEMENTED](#gaa7ef60306699f14fa7f3bcd6ed744633)。

<a id="r_ga17041726bc43fb2a1aa3ddc927ac6cef"></a>

```c
#define TEEC_ERROR_NOT_SUPPORTED 0xFFFF000A
```

相关声明：[TEEC_ERROR_NOT_SUPPORTED](#ga17041726bc43fb2a1aa3ddc927ac6cef)。

<a id="r_gaf515dfd970be2caf575be186dd32afd7"></a>

```c
#define TEEC_ERROR_NO_DATA 0xFFFF000B
```

相关声明：[TEEC_ERROR_NO_DATA](#gaf515dfd970be2caf575be186dd32afd7)。

<a id="r_gac7aaf1249147ecd63d6fba179e26ad33"></a>

```c
#define TEEC_ERROR_OUT_OF_MEMORY 0xFFFF000C
```

相关声明：[TEEC_ERROR_OUT_OF_MEMORY](#gac7aaf1249147ecd63d6fba179e26ad33)。

<a id="r_ga28d244820db7caa7cb829ed3469f5961"></a>

```c
#define TEEC_ERROR_BUSY 0xFFFF000D
```

相关声明：[TEEC_ERROR_BUSY](#ga28d244820db7caa7cb829ed3469f5961)。

<a id="r_ga0a3047b67556c437e80c308853705de2"></a>

```c
#define TEEC_ERROR_COMMUNICATION 0xFFFF000E
```

相关声明：[TEEC_ERROR_COMMUNICATION](#ga0a3047b67556c437e80c308853705de2)。

<a id="r_gaae2b6bb8d476d422f782e7ac226de21b"></a>

```c
#define TEEC_ERROR_SECURITY 0xFFFF000F
```

相关声明：[TEEC_ERROR_SECURITY](#gaae2b6bb8d476d422f782e7ac226de21b)。

<a id="r_ga511a0747fab1c307a5263a07ce396962"></a>

```c
#define TEEC_ERROR_SHORT_BUFFER 0xFFFF0010
```

相关声明：[TEEC_ERROR_SHORT_BUFFER](#ga511a0747fab1c307a5263a07ce396962)。

<a id="r_ga10e9a718e8ce09e6fe117bc0b002a3d6"></a>

```c
#define TEEC_ERROR_EXTERNAL_CANCEL 0xFFFF0011
```

相关声明：[TEEC_ERROR_EXTERNAL_CANCEL](#ga10e9a718e8ce09e6fe117bc0b002a3d6)。

<a id="r_ga6aa8da2d81b77fb8d2ec16f4e3a27528"></a>

```c
#define TEEC_ERROR_TARGET_DEAD 0xFFFF3024
```

相关声明：[TEEC_ERROR_TARGET_DEAD](#ga6aa8da2d81b77fb8d2ec16f4e3a27528)。

<a id="r_ga6229f84eb575bf10c14b40f02495b46e"></a>

```c
#define TEEC_ERROR_STORAGE_NO_SPACE 0xFFFF3041
```

相关声明：[TEEC_ERROR_STORAGE_NO_SPACE](#ga6229f84eb575bf10c14b40f02495b46e)。

<a id="r_ga16baa8eb95393514c6035c957ad55a6b"></a>

```c
#define TEEC_LOGIN_PUBLIC 0x00000000
```

相关声明：[TEEC_LOGIN_PUBLIC](#ga16baa8eb95393514c6035c957ad55a6b)。

会话登录方法（Session Login Methods），用作 `tee_open_session()` 的 `connectionMethod` 参数。

<a id="r_gab6940dd1f636aa67e74a8615e8544f85"></a>

```c
#define TEEC_LOGIN_USER 0x00000001
```

相关声明：[TEEC_LOGIN_USER](#gab6940dd1f636aa67e74a8615e8544f85)。

<a id="r_ga8cdd4a2102e18a60d0624d610ef3619e"></a>

```c
#define TEEC_LOGIN_GROUP 0x00000002
```

相关声明：[TEEC_LOGIN_GROUP](#ga8cdd4a2102e18a60d0624d610ef3619e)。

<a id="r_gae803496f14c6cc84b7f56174006c16a6"></a>

```c
#define TEEC_LOGIN_APPLICATION 0x00000004
```

相关声明：[TEEC_LOGIN_APPLICATION](#gae803496f14c6cc84b7f56174006c16a6)。

<a id="r_ga37fbb624e8c289d400cd69948bf8b505"></a>

```c
#define TEEC_LOGIN_USER_APPLICATION 0x00000005
```

相关声明：[TEEC_LOGIN_USER_APPLICATION](#ga37fbb624e8c289d400cd69948bf8b505)。

<a id="r_gad1da184306fe0283fc1e618f829119e3"></a>

```c
#define TEEC_LOGIN_GROUP_APPLICATION 0x00000006
```

相关声明：[TEEC_LOGIN_GROUP_APPLICATION](#gad1da184306fe0283fc1e618f829119e3)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.5\_函数（Functions）

<a id="r_gadaaec6b6ea29d81f36943bbe5bcb305e"></a>

```c
int tee_get_version (const struct device *dev, struct tee_version_info *info)
```

相关声明：[tee_get_version](#gadaaec6b6ea29d81f36943bbe5bcb305e)、[device](../device_reference/P002_设备对象结构.md)、[tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)。

获取当前可信执行环境（TEE）版本信息（Version Info）。

<a id="r_gad7c66e32d5b02c42c698bd422cf43523"></a>

```c
int tee_open_session (const struct device *dev, struct tee_open_session_arg *arg, unsigned int num_param, struct tee_param *param, uint32_t *session_id)
```

相关声明：[tee_open_session](#gad7c66e32d5b02c42c698bd422cf43523)、[device](../device_reference/P002_设备对象结构.md)、[tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为可信环境（Trusted Environment）打开会话（Session）。

<a id="r_gacb1d58002378a11d92361a149d451241"></a>

```c
int tee_close_session (const struct device *dev, uint32_t session_id)
```

相关声明：[tee_close_session](#gacb1d58002378a11d92361a149d451241)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

关闭可信环境（Trusted Environment）会话（Session）。

<a id="r_ga34fbbfe48a07541041ffddb9e318332a"></a>

```c
int tee_cancel (const struct device *dev, uint32_t session_id, uint32_t cancel_id)
```

相关声明：[tee_cancel](#ga34fbbfe48a07541041ffddb9e318332a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

取消可信环境（Trusted Environment）的会话或函数调用（Session or Invoke Function）。

<a id="r_gae1337f293febcecc7dbc79ac064e7824"></a>

```c
int tee_invoke_func (const struct device *dev, struct tee_invoke_func_arg *arg, unsigned int num_param, struct tee_param *param)
```

相关声明：[tee_invoke_func](#gae1337f293febcecc7dbc79ac064e7824)、[device](../device_reference/P002_设备对象结构.md)、[tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

调用可信环境应用（Trusted Environment Application）的函数。

<a id="r_gade7fdbece8b0bd47f5d148572016c4ef"></a>

```c
int tee_add_shm (const struct device *dev, void *addr, size_t align, size_t size, uint32_t flags, struct tee_shm **shmp)
```

相关声明：[tee_add_shm](#gade7fdbece8b0bd47f5d148572016c4ef)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

分配并注册共享内存（Shared Memory）的辅助函数。

<a id="r_gaf53521a3e3a36a9827753716bef1434f"></a>

```c
int tee_rm_shm (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_rm_shm](#gaf53521a3e3a36a9827753716bef1434f)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

移除并注销共享内存（Shared Memory）的辅助函数。

<a id="r_ga1565c23104792203ede9d9cb388ff782"></a>

```c
int tee_shm_register (const struct device *dev, void *addr, size_t size, uint32_t flags, struct tee_shm **shm)
```

相关声明：[tee_shm_register](#ga1565c23104792203ede9d9cb388ff782)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

为可信环境（Trusted Environment）注册共享内存（Shared Memory）。

<a id="r_gade2c0e7d89e3594707637b62a1901bac"></a>

```c
int tee_shm_unregister (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_unregister](#gade2c0e7d89e3594707637b62a1901bac)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

注销可信环境（Trusted Environment）的共享内存（Shared Memory）。

<a id="r_ga47f7403e2b136f755432159c7bd679a5"></a>

```c
int tee_shm_alloc (const struct device *dev, size_t size, uint32_t flags, struct tee_shm **shm)
```

相关声明：[tee_shm_alloc](#ga47f7403e2b136f755432159c7bd679a5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

为可信环境（Trusted Environment）分配共享内存区域（Shared Memory Region）。

<a id="r_ga346d8d67a18542c097f1254c0ace8726"></a>

```c
int tee_shm_free (const struct device *dev, struct tee_shm *shm)
```

相关声明：[tee_shm_free](#ga346d8d67a18542c097f1254c0ace8726)、[device](../device_reference/P002_设备对象结构.md)、[tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)。

释放可信环境（Trusted Environment）的共享内存区域（Shared Memory Region）。

<a id="r_ga2213f63da1f080beaedc169e13531a37"></a>

```c
int tee_suppl_recv (const struct device *dev, uint32_t *func, unsigned int *num_params, struct tee_param *param)
```

相关声明：[tee_suppl_recv](#ga2213f63da1f080beaedc169e13531a37)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）接收请求。

<a id="r_ga93cccfa446983be704f364760bf7567b"></a>

```c
int tee_suppl_send (const struct device *dev, unsigned int ret, unsigned int num_params, struct tee_param *param)
```

相关声明：[tee_suppl_send](#ga93cccfa446983be704f364760bf7567b)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)。

为 TEE 辅助服务（Supplicant）函数发送请求。

## 12.6\_详细说明（Detailed Documentation）

<a id="ga2eb5a95c2f50e08bbb6235fa47253f10"></a>

### `TEE_GEN_CAP_GP`

```c
#define TEE_GEN_CAP_GP BIT(0) /* GlobalPlatform compliant TEE */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga4cd66a4425e312338823061e561638de"></a>

### `TEE_GEN_CAP_MEMREF_NULL`

```c
#define TEE_GEN_CAP_MEMREF_NULL BIT(3) /* Support NULL MemRef */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga15e96022b209b84d29c29f213aab0331"></a>

### `TEE_GEN_CAP_PRIVILEGED`

```c
#define TEE_GEN_CAP_PRIVILEGED BIT(1) /* Privileged device (for supplicant) */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gae661041c8b0f0638891a5a82b74aa928"></a>

### `TEE_GEN_CAP_REG_MEM`

```c
#define TEE_GEN_CAP_REG_MEM BIT(2) /* Supports registering shared memory */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga15358e8f86ca9a2b6aca9899ee982542"></a>

### `TEE_PARAM_ATTR_MASK`

```c
#define TEE_PARAM_ATTR_MASK (TEE_PARAM_ATTR_TYPE_MASK | TEE_PARAM_ATTR_META)
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga42e96de713673837d60ac3b938373206"></a>

### `TEE_PARAM_ATTR_META`

```c
#define TEE_PARAM_ATTR_META 0x100
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga8e2dca32129d730d9394f0798d578ce7"></a>

### `TEE_PARAM_ATTR_TYPE_MASK`

```c
#define TEE_PARAM_ATTR_TYPE_MASK 0xff
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga43fcdc052991d21fc7fde3720256ef2c"></a>

### `TEE_PARAM_ATTR_TYPE_MEMREF_INOUT`

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INOUT 7 /* input and output */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga0c7f0c79fd599a2d5ec2759230bff6e7"></a>

### `TEE_PARAM_ATTR_TYPE_MEMREF_INPUT`

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_INPUT 5
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga5305a53edb649a22c774731bf2f53987"></a>

### `TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT`

```c
#define TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT 6
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gad3f8bf86812e0e5befa873389235ddd9"></a>

### `TEE_PARAM_ATTR_TYPE_NONE`

```c
#define TEE_PARAM_ATTR_TYPE_NONE 0 /* parameter not used */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga925026258aed48470a015a655f25b270"></a>

### `TEE_PARAM_ATTR_TYPE_VALUE_INOUT`

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INOUT 3 /* input and output */
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga5304d0bdbfb80563bdf3bd801cc72613"></a>

### `TEE_PARAM_ATTR_TYPE_VALUE_INPUT`

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_INPUT 1
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gaf66e35aefb70c34cba93eeb5f3cb0f8a"></a>

### `TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT`

```c
#define TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT 2
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga85fd3e6e6b596da02c97661a35c9814c"></a>

### `TEE_SHM_ALLOC`

```c
#define TEE_SHM_ALLOC BIT(1)
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga2fac25b74105b1ddfb15db51598b89c8"></a>

### `TEE_SHM_REGISTER`

```c
#define TEE_SHM_REGISTER BIT(0)
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga79ff2ca70757daf8e677b42002f4aeac"></a>

### `TEE_UUID_LEN`

```c
#define TEE_UUID_LEN 16
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga65a8bd0582ef42f84e85704bab5a85fe"></a>

### `TEEC_ERROR_ACCESS_CONFLICT`

```c
#define TEEC_ERROR_ACCESS_CONFLICT 0xFFFF0003
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gad7c7cd2ed537347d60276bd08375ca30"></a>

### `TEEC_ERROR_ACCESS_DENIED`

```c
#define TEEC_ERROR_ACCESS_DENIED 0xFFFF0001
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga0e08a22cf7abe05ae2d0cfd7fe92b0e7"></a>

### `TEEC_ERROR_BAD_FORMAT`

```c
#define TEEC_ERROR_BAD_FORMAT 0xFFFF0005
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga79b607eb603bef58b3065a3014ee7117"></a>

### `TEEC_ERROR_BAD_PARAMETERS`

```c
#define TEEC_ERROR_BAD_PARAMETERS 0xFFFF0006
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga19c6e3eb278dd58fa49b7de3dff8b7ac"></a>

### `TEEC_ERROR_BAD_STATE`

```c
#define TEEC_ERROR_BAD_STATE 0xFFFF0007
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga28d244820db7caa7cb829ed3469f5961"></a>

### `TEEC_ERROR_BUSY`

```c
#define TEEC_ERROR_BUSY 0xFFFF000D
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga8cbe25a679add519a048c85c03be1ede"></a>

### `TEEC_ERROR_CANCEL`

```c
#define TEEC_ERROR_CANCEL 0xFFFF0002
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga0a3047b67556c437e80c308853705de2"></a>

### `TEEC_ERROR_COMMUNICATION`

```c
#define TEEC_ERROR_COMMUNICATION 0xFFFF000E
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gad8825a36962871ac2006386d18a821e7"></a>

### `TEEC_ERROR_EXCESS_DATA`

```c
#define TEEC_ERROR_EXCESS_DATA 0xFFFF0004
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga10e9a718e8ce09e6fe117bc0b002a3d6"></a>

### `TEEC_ERROR_EXTERNAL_CANCEL`

```c
#define TEEC_ERROR_EXTERNAL_CANCEL 0xFFFF0011
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga13c7ed6f37eba36870e4b138b661b61f"></a>

### `TEEC_ERROR_GENERIC`

```c
#define TEEC_ERROR_GENERIC 0xFFFF0000
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga805299b26fda6bb38a97cf6a0825431d"></a>

### `TEEC_ERROR_ITEM_NOT_FOUND`

```c
#define TEEC_ERROR_ITEM_NOT_FOUND 0xFFFF0008
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gaf515dfd970be2caf575be186dd32afd7"></a>

### `TEEC_ERROR_NO_DATA`

```c
#define TEEC_ERROR_NO_DATA 0xFFFF000B
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gaa7ef60306699f14fa7f3bcd6ed744633"></a>

### `TEEC_ERROR_NOT_IMPLEMENTED`

```c
#define TEEC_ERROR_NOT_IMPLEMENTED 0xFFFF0009
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga17041726bc43fb2a1aa3ddc927ac6cef"></a>

### `TEEC_ERROR_NOT_SUPPORTED`

```c
#define TEEC_ERROR_NOT_SUPPORTED 0xFFFF000A
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gac7aaf1249147ecd63d6fba179e26ad33"></a>

### `TEEC_ERROR_OUT_OF_MEMORY`

```c
#define TEEC_ERROR_OUT_OF_MEMORY 0xFFFF000C
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gaae2b6bb8d476d422f782e7ac226de21b"></a>

### `TEEC_ERROR_SECURITY`

```c
#define TEEC_ERROR_SECURITY 0xFFFF000F
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga511a0747fab1c307a5263a07ce396962"></a>

### `TEEC_ERROR_SHORT_BUFFER`

```c
#define TEEC_ERROR_SHORT_BUFFER 0xFFFF0010
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga6229f84eb575bf10c14b40f02495b46e"></a>

### `TEEC_ERROR_STORAGE_NO_SPACE`

```c
#define TEEC_ERROR_STORAGE_NO_SPACE 0xFFFF3041
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gad9e7d08ba6637d86cf611952b9842568"></a>

### `TEEC_ERROR_STORAGE_NOT_AVAILABLE`

```c
#define TEEC_ERROR_STORAGE_NOT_AVAILABLE 0xF0100003
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga6aa8da2d81b77fb8d2ec16f4e3a27528"></a>

### `TEEC_ERROR_TARGET_DEAD`

```c
#define TEEC_ERROR_TARGET_DEAD 0xFFFF3024
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gae803496f14c6cc84b7f56174006c16a6"></a>

### `TEEC_LOGIN_APPLICATION`

```c
#define TEEC_LOGIN_APPLICATION 0x00000004
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga8cdd4a2102e18a60d0624d610ef3619e"></a>

### `TEEC_LOGIN_GROUP`

```c
#define TEEC_LOGIN_GROUP 0x00000002
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gad1da184306fe0283fc1e618f829119e3"></a>

### `TEEC_LOGIN_GROUP_APPLICATION`

```c
#define TEEC_LOGIN_GROUP_APPLICATION 0x00000006
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga16baa8eb95393514c6035c957ad55a6b"></a>

### `TEEC_LOGIN_PUBLIC`

```c
#define TEEC_LOGIN_PUBLIC 0x00000000
```

```c
#include <zephyr/drivers/tee.h>
```

会话登录方法（Session Login Methods），用作 `tee_open_session()` 的 `connectionMethod` 参数。

类型为 uint32_t。

登录方式（Login Method）：

- TEEC_LOGIN_PUBLIC：不提供登录数据（Login Data）。
- TEEC_LOGIN_USER：提供有关运行客户端应用进程（Client Application Process）的用户的登录数据。
- TEEC_LOGIN_GROUP：提供有关运行客户端应用进程的用户组的登录数据。
- TEEC_LOGIN_APPLICATION：提供有关运行中的客户端应用自身的登录数据。
- TEEC_LOGIN_USER_APPLICATION：提供有关用户和运行中的客户端应用自身的登录数据。
- TEEC_LOGIN_GROUP_APPLICATION：提供有关用户组和运行中的客户端应用自身的登录数据。

<a id="gab6940dd1f636aa67e74a8615e8544f85"></a>

### `TEEC_LOGIN_USER`

```c
#define TEEC_LOGIN_USER 0x00000001
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga37fbb624e8c289d400cd69948bf8b505"></a>

### `TEEC_LOGIN_USER_APPLICATION`

```c
#define TEEC_LOGIN_USER_APPLICATION 0x00000005
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="ga6040bf64a72a13c675681c99112f7f69"></a>

### `TEEC_ORIGIN_API`

```c
#define TEEC_ORIGIN_API 0x00000001
```

```c
#include <zephyr/drivers/tee.h>
```

函数错误来源（Function Error Origins），类型为 `TEEC_ErrorOrigin`。

这些值表示某个返回值源自软件栈（Software Stack）的哪个位置。

错误来源（Error Origin）：

- TEEC_ORIGIN_API：错误源自 TEE 客户端 API（TEE Client API）的实现。
- TEEC_ORIGIN_COMMS：错误源自连接富操作系统（Rich OS）与 TEE 的底层通信栈（Communications Stack）。
- TEEC_ORIGIN_TEE：错误源自 TEE 公共代码。
- TEEC_ORIGIN_TRUSTED_APP：错误源自可信应用（Trusted Application）代码。

<a id="ga668c5799e8360e3e885a908784805578"></a>

### `TEEC_ORIGIN_COMMS`

```c
#define TEEC_ORIGIN_COMMS 0x00000002
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gabebf4008dbbf440ac352d510675c9433"></a>

### `TEEC_ORIGIN_TEE`

```c
#define TEEC_ORIGIN_TEE 0x00000003
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gaebb73e90a25eeecc5ac274c2c396f32f"></a>

### `TEEC_ORIGIN_TRUSTED_APP`

```c
#define TEEC_ORIGIN_TRUSTED_APP 0x00000004
```

```c
#include <zephyr/drivers/tee.h>
```

<a id="gae000299e1a48b8e9c807c8e1b7e62aed"></a>

### `TEEC_SUCCESS`

```c
#define TEEC_SUCCESS 0x00000000
```

```c
#include <zephyr/drivers/tee.h>
```

返回值（Return Values）。

类型为 TEEC_Result。

标准定义的错误码（Standard-defined Error Codes）：

- TEEC_SUCCESS：操作成功。
- TEEC_ERROR_GENERIC：未指定具体原因。
- TEEC_ERROR_ACCESS_DENIED：访问权限不足。
- TEEC_ERROR_CANCEL：操作已取消。
- TEEC_ERROR_ACCESS_CONFLICT：并发访问引发冲突。
- TEEC_ERROR_EXCESS_DATA：为所请求的操作传入了过多数据。
- TEEC_ERROR_BAD_FORMAT：输入数据格式无效。
- TEEC_ERROR_BAD_PARAMETERS：输入参数无效。
- TEEC_ERROR_BAD_STATE：操作在当前状态下无效。
- TEEC_ERROR_ITEM_NOT_FOUND：未找到所请求的数据项。
- TEEC_ERROR_NOT_IMPLEMENTED：所请求的操作应当存在，但尚未实现。
- TEEC_ERROR_NOT_SUPPORTED：所请求的操作有效，但此实现不支持。
- TEEC_ERROR_NO_DATA：缺少预期数据。
- TEEC_ERROR_OUT_OF_MEMORY：系统资源耗尽。
- TEEC_ERROR_BUSY：系统正忙于其他工作。
- TEEC_ERROR_COMMUNICATION：与远端通信失败。
- TEEC_ERROR_SECURITY：检测到安全故障。
- TEEC_ERROR_SHORT_BUFFER：提供的缓冲区太小，无法容纳生成的输出。
- TEEC_ERROR_TARGET_DEAD：可信应用在操作过程中发生恐慌（Panic）。

<a id="gade7fdbece8b0bd47f5d148572016c4ef"></a>

### `tee_add_shm()`

```c
int tee_add_shm ( const struct device * dev, void * addr, size_t align, size_t size, uint32_t flags, struct tee_shm ** shmp )
```

```c
#include <zephyr/drivers/tee.h>
```

分配并注册共享内存（Shared Memory）的辅助函数。

为 TEE 分配并注册共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `addr` | 共享内存地址（Shared Memory Address）。 |
| `align` | 区域对齐（Region Alignment）。 |
| `size` | 共享内存区域大小（Shared Memory Region Size）。 |
| `flags` | 用于设置注册参数（Registering Parameters）的标志。 |
| `shmp` | 返回共享内存结构体（Shared Memory Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga34fbbfe48a07541041ffddb9e318332a"></a>

### `tee_cancel()`

```c
int tee_cancel ( const struct device * dev, uint32_t session_id, uint32_t cancel_id )
```

```c
#include <zephyr/drivers/tee.h>
```

取消可信环境（Trusted Environment）的会话或函数调用（Session or Invoke Function）。

取消 TA 的会话（Session）或函数调用（Invoke Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `session_id` | 要关闭的会话（Session）。 |
| `cancel_id` | 取消原因（Cancel Reason）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gacb1d58002378a11d92361a149d451241"></a>

### `tee_close_session()`

```c
int tee_close_session ( const struct device * dev, uint32_t session_id )
```

```c
#include <zephyr/drivers/tee.h>
```

关闭可信环境（Trusted Environment）会话（Session）。

关闭到可信环境（Trusted Environment）的会话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `session_id` | 要关闭的会话（Session）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gadaaec6b6ea29d81f36943bbe5bcb305e"></a>

### `tee_get_version()`

```c
int tee_get_version ( const struct device * dev, struct tee_version_info * info )
```

```c
#include <zephyr/drivers/tee.h>
```

获取当前可信执行环境（TEE）版本信息（Version Info）。

以 TEE 版本信息（Version Info）的形式返回信息，其中包括能力描述（Capabilities Description）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `info` | 用于返回能力（Capabilities）的结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gae1337f293febcecc7dbc79ac064e7824"></a>

### `tee_invoke_func()`

```c
int tee_invoke_func ( const struct device * dev, struct tee_invoke_func_arg * arg, unsigned int num_param, struct tee_param * param )
```

```c
#include <zephyr/drivers/tee.h>
```

调用可信环境应用（Trusted Environment Application）的函数。

调用 TA 中的函数（Invoke Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `arg` | 包含函数调用参数（Invoke Function Arguments）的结构体。 |
| `num_param` | 要传递的附加参数数量（Number of Additional Parameters）。 |
| `param` | 传给 open_session 调用的参数列表（Parameter List）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gad7c66e32d5b02c42c698bd422cf43523"></a>

### `tee_open_session()`

```c
int tee_open_session ( const struct device * dev, struct tee_open_session_arg * arg, unsigned int num_param, struct tee_param * param, uint32_t * session_id )
```

```c
#include <zephyr/drivers/tee.h>
```

为可信环境（Trusted Environment）打开会话（Session）。

打开到可信环境（Trusted Environment）的新会话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `arg` | 包含会话参数（Session Arguments）的结构体。 |
| `num_param` | 要传递的附加参数数量（Number of Additional Parameters）。 |
| `param` | 传给 open_session 调用的参数列表（Parameter List）。 |
| `session_id` | 返回所创建会话的标识符（Session ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gaf53521a3e3a36a9827753716bef1434f"></a>

### `tee_rm_shm()`

```c
int tee_rm_shm ( const struct device * dev, struct tee_shm * shm )
```

```c
#include <zephyr/drivers/tee.h>
```

移除并注销共享内存（Shared Memory）的辅助函数。

移除并注销 TEE 的共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `shm` | 指向 tee_shm 结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga47f7403e2b136f755432159c7bd679a5"></a>

### `tee_shm_alloc()`

```c
int tee_shm_alloc ( const struct device * dev, size_t size, uint32_t flags, struct tee_shm ** shm )
```

```c
#include <zephyr/drivers/tee.h>
```

为可信环境（Trusted Environment）分配共享内存区域（Shared Memory Region）。

为 TEE 分配共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `size` | 区域大小。 |
| `flags` | 要分配的区域（Region）。 |
| `shm` | 返回共享内存结构体（Shared Memory Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga346d8d67a18542c097f1254c0ace8726"></a>

### `tee_shm_free()`

```c
int tee_shm_free ( const struct device * dev, struct tee_shm * shm )
```

```c
#include <zephyr/drivers/tee.h>
```

释放可信环境（Trusted Environment）的共享内存区域（Shared Memory Region）。

释放 TEE 的共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `shm` | 共享内存结构体（Shared Memory Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga1565c23104792203ede9d9cb388ff782"></a>

### `tee_shm_register()`

```c
int tee_shm_register ( const struct device * dev, void * addr, size_t size, uint32_t flags, struct tee_shm ** shm )
```

```c
#include <zephyr/drivers/tee.h>
```

为可信环境（Trusted Environment）注册共享内存（Shared Memory）。

为 TEE 注册共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `addr` | 共享内存地址（Shared Memory Address）。 |
| `size` | 共享内存区域大小（Shared Memory Region Size）。 |
| `flags` | 用于设置注册参数（Registering Parameters）的标志。 |
| `shm` | 返回共享内存结构体（Shared Memory Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="gade2c0e7d89e3594707637b62a1901bac"></a>

### `tee_shm_unregister()`

```c
int tee_shm_unregister ( const struct device * dev, struct tee_shm * shm )
```

```c
#include <zephyr/drivers/tee.h>
```

注销可信环境（Trusted Environment）的共享内存（Shared Memory）。

注销 TEE 的共享内存（Shared Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `shm` | 共享内存结构体（Shared Memory Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga2213f63da1f080beaedc169e13531a37"></a>

### `tee_suppl_recv()`

```c
int tee_suppl_recv ( const struct device * dev, uint32_t * func, unsigned int * num_params, struct tee_param * param )
```

```c
#include <zephyr/drivers/tee.h>
```

为 TEE 辅助服务（Supplicant）接收请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `func` | 辅助服务函数（Supplicant Function）。 |
| `num_params` | 要传递的参数数量（Number of Parameters）。 |
| `param` | 用于发送／接收的参数列表（Parameter List）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga93cccfa446983be704f364760bf7567b"></a>

### `tee_suppl_send()`

```c
int tee_suppl_send ( const struct device * dev, unsigned int ret, unsigned int num_params, struct tee_param * param )
```

```c
#include <zephyr/drivers/tee.h>
```

为 TEE 辅助服务（Supplicant）函数发送请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TEE 设备（Device）。 |
| `ret` | 辅助服务返回码（Supplicant Return Code）。 |
| `num_params` | 要传递的参数数量（Number of Parameters）。 |
| `param` | 用于发送／接收的参数列表（Parameter List）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现回调（Callback）时。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；出错时为负值（Negative）。 |

返回（Returns）：已发送请求的返回值（Return Value）。


## 12.7\_原页交叉引用（Cross References）

- [TEE 驱动后端 API](../api_power_policy_topic_reference/P011_TEE 驱动后端 API.md)
- [tee.h](../api_file_paging_wakeup_reference/P010_zephyr__drivers__tee.h_文件参考.md)
- [tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)
- [tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)
- [tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)
- [tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)
- [tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_值容器（Value Container）.md) · [返回大纲](大纲.md) · [下一章](P013_视频驱动（Video Drivers）.md)
