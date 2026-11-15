---
id: learning.zephyr-docs.api-file-usb-network-reference.page-13
title: zephyr__sip_svc__sip_svc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_sip\_svc\_\_sip\_svc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ARM SiP服务（SiP Services）的公共API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>
```

查看此文件的源码。

ARM SiP 服务的公共 API（Public API for ARM SiP Services）。ARM SiP 服务允许从运行于 EL1 的内核发出 SMC/HVC 调用，将调用送往运行于 EL2/EL3 的虚拟机监控器／安全监控固件（Hypervisor/Secure Monitor Firmware）。每个系统仅允许一个 SMC 和一个 HVC。该服务支持多个客户端（Client）。客户端必须在发送任何请求之前打开通道（Channel），并在完成后立即关闭通道。同一时刻仅允许打开一个通道。服务通过回调函数（Callback Function）将 SMC/HVC 返回值传给客户端。

客户端状态机（Client State Machine）：

- `INVALID`：注册前的无效状态（Invalid State）。
- `IDLE`：初始状态（Initial State）。
- `OPEN`：成功打开通道后，客户端从 `IDLE` 转为 `OPEN`；成功关闭通道后，则从 `OPEN` 转为 `IDLE`。
- `ABORT`：客户端已关闭通道，但仍留有尚未完成的事务（Transaction）。只有在全部事务完成后，服务才会将客户端转回 `IDLE`。处于 `ABORT` 状态时，客户端不得重新打开通道。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_ab90395e8383b1665ef5d6d88114432d8"></a>

```c
#define SIP_SVC_CLIENT_ST_INVALID 0
```

相关声明：[SIP_SVC_CLIENT_ST_INVALID](#ab90395e8383b1665ef5d6d88114432d8)。

<a id="r_a65723ac5b896f336035fc28e42ba973b"></a>

```c
#define SIP_SVC_CLIENT_ST_IDLE 1
```

相关声明：[SIP_SVC_CLIENT_ST_IDLE](#a65723ac5b896f336035fc28e42ba973b)。

<a id="r_a2d2ad62c149785afe1d60bd4c36e0008"></a>

```c
#define SIP_SVC_CLIENT_ST_OPEN 2
```

相关声明：[SIP_SVC_CLIENT_ST_OPEN](#a2d2ad62c149785afe1d60bd4c36e0008)。

<a id="r_ae200454b4fde621b96b2a17b8f1885a2"></a>

```c
#define SIP_SVC_CLIENT_ST_ABORT 3
```

相关声明：[SIP_SVC_CLIENT_ST_ABORT](#ae200454b4fde621b96b2a17b8f1885a2)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.2\_类型定义（Typedefs）

<a id="r_a73d836f58dd466241f5ba50955468b4c"></a>

```c
typedef void(* sip_svc_cb_fn) (uint32_t c_token, struct sip_svc_response *res)
```

相关声明：[sip_svc_cb_fn](#a73d836f58dd466241f5ba50955468b4c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)。

ARM SiP 服务完成后用于响应的回调函数原型（Callback Function Prototype）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.3\_函数（Functions）

<a id="r_a7f5a7116667f4904d128935e3a0fcc58"></a>

```c
uint32_t sip_svc_register (void *ctrl, void *priv_data)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_register](#a7f5a7116667f4904d128935e3a0fcc58)。

在 ARM SiP 服务中注册客户端（Client）。

<a id="r_aaafe385fe1dd0b13fe6dbffd2f01bd16"></a>

```c
int sip_svc_unregister (void *ctrl, uint32_t c_token)
```

相关声明：[sip_svc_unregister](#aaafe385fe1dd0b13fe6dbffd2f01bd16)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 ARM SiP 服务注销客户端（Client）。

<a id="r_ac1991768d256e5260542c544859c5bca"></a>

```c
int sip_svc_open (void *ctrl, uint32_t c_token, k_timeout_t k_timeout)
```

相关声明：[sip_svc_open](#ac1991768d256e5260542c544859c5bca)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

客户端请求在 ARM SiP 服务上打开通道（Channel）。

<a id="r_ab3774b372ddba3d3c4dd6e0a80082b9e"></a>

```c
int sip_svc_close (void *ctrl, uint32_t c_token, struct sip_svc_request *pre_close_req)
```

相关声明：[sip_svc_close](#ab3774b372ddba3d3c4dd6e0a80082b9e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)。

客户端请求关闭 ARM SiP 服务上的通道（Channel）。

<a id="r_afd71f6da58b4e8df3fbcf3b985226e74"></a>

```c
int sip_svc_send (void *ctrl, uint32_t c_token, struct sip_svc_request *req, sip_svc_cb_fn cb)
```

相关声明：[sip_svc_send](#afd71f6da58b4e8df3fbcf3b985226e74)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)、[sip_svc_cb_fn](#a73d836f58dd466241f5ba50955468b4c)。

客户端请求向 EL3/EL2 发送 SMC/HVC 调用。

<a id="r_a754649a7ad55281bc0059036b0e5c7e9"></a>

```c
void * sip_svc_get_priv_data (void *ctrl, uint32_t c_token)
```

相关声明：[sip_svc_get_priv_data](#a754649a7ad55281bc0059036b0e5c7e9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取指向客户端私有数据（Client Private Data）的地址指针。

<a id="r_a217c518c046cd1d716d803175b4cd99e"></a>

```c
void * sip_svc_get_controller (char *method)
```

相关声明：[sip_svc_get_controller](#a217c518c046cd1d716d803175b4cd99e)。

获取 ARM SiP 服务句柄（Service Handle）。

## 13.4\_详细说明（Detailed Documentation）

<a id="ae200454b4fde621b96b2a17b8f1885a2"></a>

### `SIP_SVC_CLIENT_ST_ABORT`

```c
#define SIP_SVC_CLIENT_ST_ABORT 3
```

<a id="a65723ac5b896f336035fc28e42ba973b"></a>

### `SIP_SVC_CLIENT_ST_IDLE`

```c
#define SIP_SVC_CLIENT_ST_IDLE 1
```

<a id="ab90395e8383b1665ef5d6d88114432d8"></a>

### `SIP_SVC_CLIENT_ST_INVALID`

```c
#define SIP_SVC_CLIENT_ST_INVALID 0
```

<a id="a2d2ad62c149785afe1d60bd4c36e0008"></a>

### `SIP_SVC_CLIENT_ST_OPEN`

```c
#define SIP_SVC_CLIENT_ST_OPEN 2
```

<a id="a73d836f58dd466241f5ba50955468b4c"></a>

### `sip_svc_cb_fn`

```c
typedef void(* sip_svc_cb_fn) (uint32_t c_token, struct sip_svc_response *res)
```

ARM SiP 服务完成后用于响应的回调函数原型（Callback Function Prototype）。

成功时，通过回调（Callback）向用户返回响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c_token` | 客户端令牌（Client Token）。 |
| `res` | 指向 `struct sip_svc_response` 的指针。 |

<a id="ab3774b372ddba3d3c4dd6e0a80082b9e"></a>

### `sip_svc_close()`

```c
int sip_svc_close ( void * ctrl, uint32_t c_token, struct sip_svc_request * pre_close_req )
```

客户端请求关闭 ARM SiP 服务上的通道（Channel）。

客户端必须在完成后立即关闭通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |
| `c_token` | 客户端令牌（Client Token）。 |
| `pre_close_req` | 关闭通道（Channel）时向下层发送的预关闭请求（Pre-close Request）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOTSUP` | 发送 `pre_close_request` 时出错。 |
| `-EPROTO` | 客户端不处于 `OPEN` 状态。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a217c518c046cd1d716d803175b4cd99e"></a>

### `sip_svc_get_controller()`

```c
void * sip_svc_get_controller ( char * method)
```

获取 ARM SiP 服务句柄（Service Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `method` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 参数无效（Invalid Arguments），或提供了不受支持的方法名称（Method Name）。 |

**返回（Returns）**：返回值（Returns）：有效指针（Valid Pointer）。

<a id="a754649a7ad55281bc0059036b0e5c7e9"></a>

### `sip_svc_get_priv_data()`

```c
void * sip_svc_get_priv_data ( void * ctrl, uint32_t c_token )
```

获取指向客户端私有数据（Client Private Data）的地址指针。

该指针（Pointer）由客户端在注册时提供。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |
| `c_token` | 客户端令牌（Client Token）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 参数无效（Invalid Arguments），或获取锁（Lock）失败。 |

**返回（Returns）**：返回值（Returns）：指向客户端私有数据（Client Private Data）的地址指针。

<a id="ac1991768d256e5260542c544859c5bca"></a>

### `sip_svc_open()`

```c
int sip_svc_open ( void * ctrl, uint32_t c_token, k_timeout_t k_timeout )
```

客户端请求在 ARM SiP 服务上打开通道（Channel）。

客户端必须先打开通道（Channel），才能通过 SMC/HVC 向运行于 EL2/EL3 的虚拟机监控器／安全监控固件（Hypervisor/Secure Monitor Firmware）发送任何请求。

同一时刻，服务仅允许打开一个通道（Channel），并使用互斥量（Mutex）进行保护。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |
| `c_token` | 客户端令牌（Client Token）。 |
| `k_timeout` | 互斥量（Mutex）已被锁定时的等待时间：若取值为 `K_NO_WAIT`，立即返回非零错误码；若取值为 `K_FOREVER`，则无限等待；否则等待给定的时间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ETIMEDOUT` | 超时期限已到（Timeout Expiry）。 |
| `-EALREADY` | 客户端已处于打开状态（Open State）。 |

<a id="a7f5a7116667f4904d128935e3a0fcc58"></a>

### `sip_svc_register()`

```c
uint32_t sip_svc_register ( void * ctrl, void * priv_data )
```

在 ARM SiP 服务中注册客户端（Client）。

成功时，客户端在服务中处于 `IDLE` 状态，且服务向客户端返回一个令牌（Token）。随后客户端可使用该令牌打开服务上的通道（Channel），与运行于 EL2/EL3 的虚拟机监控器／安全监控固件（Hypervisor/Secure Monitor Firmware）通信。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向控制器实例（Controller Instance）的指针，其服务提供 ARM SMC/HVC SiP 服务。 |
| `priv_data` | 指向客户端私有数据（Client Private Data）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `token_id` | 成功时返回。 |
| `SIP_SVC_ID_INVALID` | 参数无效（Invalid Arguments）、分配客户端标识符（Client ID）失败，或获取锁（Lock）失败。 |

<a id="afd71f6da58b4e8df3fbcf3b985226e74"></a>

### `sip_svc_send()`

```c
int sip_svc_send ( void * ctrl, uint32_t c_token, struct sip_svc_request * req, sip_svc_cb_fn cb )
```

客户端请求向 EL3/EL2 发送 SMC/HVC 调用。

客户端必须先在设备上打开通道（Channel），才能使用本函数。本函数为非阻塞函数（Non-blocking Function），可从任何上下文调用。如果请求被接受，服务会向客户端返回事务标识符（Transaction ID）。事务完成时调用客户端回调（Client Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |
| `c_token` | 客户端令牌（Client Token）。 |
| `req` | 采用 `struct sip_svc_request` 格式的用户输入的地址。 |
| `cb` | 回调（Callback）。SMC/SVC 返回值将通过回调中的上下文（Context）传给客户端，格式为 `struct sip_svc_response`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-EOPNOTSUPP` | 命令标识符（Command ID）或函数标识符（Function ID）无效。 |
| `-ESRCH` | 客户端状态（Client State）无效。 |
| `-ENOMEM` | 分配内存（Memory Allocation）失败。 |
| `-ENOMSG` | 插入数据库（Database）失败。 |
| `-ENOBUF` | 插入消息队列（`msgq`）失败。 |
| `-ENOLCK` | 获取锁（Lock）失败。 |
| `-EHOSTDOWN` | 不存在 `sip_svc` 线程（Thread）。 |
| `-ENOTSUP` | 检查不受支持的条件（Unsupported Condition）。 |

**返回（Returns）**：返回值（Returns）：成功时返回事务标识符（Transaction ID）。

<a id="aaafe385fe1dd0b13fe6dbffd2f01bd16"></a>

### `sip_svc_unregister()`

```c
int sip_svc_unregister ( void * ctrl, uint32_t c_token )
```

从 ARM SiP 服务注销客户端（Client）。

成功时，将客户端从服务分离（Detach）。只有在该客户端所属的全部事务（Transaction）均已关闭时，才允许注销（Unregistration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 指向提供 ARM SiP 服务的控制器实例（Controller Instance）的指针。 |
| `c_token` | 客户端令牌（Client Token）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVALinvalid` | 参数（Arguments）。 |
| `-ENODATA` | 客户端未正确注册（Registered）时。 |
| `-EBUSY` | 客户端具有待处理事务（Pending Transaction）时。 |
| `-ECANCELED` | 客户端不处于 `IDLE` 状态时。 |
| `-ENOLCK` | 获取互斥量（Mutex）失败时。 |


## 13.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/drivers/sip_svc/sip_svc_proto.h](../api_source_reference/P790_sip_svc_proto.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P787_sip_svc.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [SIP_SVC_ID_INVALID](../api_file_battery_interrupt_reference/P011_zephyr__drivers__sip_svc__sip_svc_proto.h_文件参考.md#ad1cb9509a40e51809b13f1fccf0f35ba)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_zephyr__sd__sdio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__sip_svc__sip_svc_driver.h_文件参考.md)
