---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-7
title: zephyr__drivers__ethernet__eth_adin2111.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_ethernet\_\_eth\_adin2111.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/eth__adin2111_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ADIN2111以太网控制器（Ethernet Controller）驱动API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
```

查看此文件的源码。

ADIN2111以太网控制器（Ethernet Controller）驱动API的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.1\_函数（Functions）

<a id="r_a54e88cd118466a1a44ef02197fe2b59d"></a>

```c
int eth_adin2111_lock (const struct device *dev, k_timeout_t timeout)
```

相关声明：[eth_adin2111_lock](#a54e88cd118466a1a44ef02197fe2b59d)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

锁定设备访问（Device Access）。

<a id="r_a72b5466138f087ac4e788bc878781c3e"></a>

```c
int eth_adin2111_unlock (const struct device *dev)
```

相关声明：[eth_adin2111_unlock](#a72b5466138f087ac4e788bc878781c3e)、[device](../device_reference/P002_设备对象结构.md)。

解锁设备访问（Device Access）。

<a id="r_a340b4d3786807c7feb423b36d6533a87"></a>

```c
int eth_adin2111_sw_reset (const struct device *dev, uint16_t delay)
```

相关声明：[eth_adin2111_sw_reset](#a340b4d3786807c7feb423b36d6533a87)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

同时复位介质访问控制器（MAC）和物理层（PHY）。

<a id="r_ad737f44a16702f4c8ce3f8a8ae994364"></a>

```c
int eth_adin2111_mac_reset (const struct device *dev)
```

相关声明：[eth_adin2111_mac_reset](#ad737f44a16702f4c8ce3f8a8ae994364)、[device](../device_reference/P002_设备对象结构.md)。

复位介质访问控制器（MAC）设备。

<a id="r_a9752b1a6a75880af069af1b00ce43928"></a>

```c
int eth_adin2111_broadcast_filter (const struct device *dev, bool enable)
```

相关声明：[eth_adin2111_broadcast_filter](#a9752b1a6a75880af069af1b00ce43928)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使能／禁用向主机转发广播帧（Broadcast Frames）。

<a id="r_a86de61f524a1837ff8f701c5af969d1b"></a>

```c
struct net_if * eth_adin2111_get_iface (const struct device *dev, const uint16_t port_idx)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[eth_adin2111_get_iface](#a86de61f524a1837ff8f701c5af969d1b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取与端口相关的 `net_if` 网络接口引用。

## 7.2\_详细说明（Detailed Documentation）

<a id="a9752b1a6a75880af069af1b00ce43928"></a>

### `eth_adin2111_broadcast_filter()`

```c
int eth_adin2111_broadcast_filter ( const struct device * dev, bool enable )
```

使能／禁用向主机转发广播帧（Broadcast Frames）。

目的地址（DA）不匹配的帧将被丢弃。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |
| ` enable` | 设为 0 以禁用，设为非零值以使能。 |

**说明（Note）**：注意：调用方负责锁定设备。不得从中断服务例程（ISR）调用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a86de61f524a1837ff8f701c5af969d1b"></a>

### `eth_adin2111_get_iface()`

```c
struct net_if * eth_adin2111_get_iface ( const struct device * dev, const uint16_t port_idx )
```

获取与端口相关的 `net_if` 网络接口引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |
| ` port_idx` | 端口索引。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | `struct net_if` 指针；出错时为 `NULL`。 |

<a id="a54e88cd118466a1a44ef02197fe2b59d"></a>

### `eth_adin2111_lock()`

```c
int eth_adin2111_lock ( const struct device * dev, k_timeout_t timeout )
```

锁定设备访问（Device Access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |
| ` timeout` | 等待取得设备锁（Device Lock）的时长，或特殊值 `K_NO_WAIT`、`K_FOREVER` 之一。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 设备已锁定（Locked）。 |
| `-EBUSY` | 未等待便返回。 |
| `-EAGAIN` | 等待时间已到，发生超时。 |

<a id="ad737f44a16702f4c8ce3f8a8ae994364"></a>

### `eth_adin2111_mac_reset()`

```c
int eth_adin2111_mac_reset ( const struct device * dev)
```

复位介质访问控制器（MAC）设备。

注意：PHY 1 必须退出软件掉电状态（Software Power-down），MAC 子系统复位才会生效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |

**说明（Note）**：注意：调用方负责锁定设备。不得从中断服务例程（ISR）调用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a340b4d3786807c7feb423b36d6533a87"></a>

### `eth_adin2111_sw_reset()`

```c
int eth_adin2111_sw_reset ( const struct device * dev, uint16_t delay )
```

同时复位介质访问控制器（MAC）和物理层（PHY）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |
| ` delay` | 延迟时间（Delay），单位为毫秒。 |

**说明（Note）**：注意：调用方负责锁定设备。不得从中断服务例程（ISR）调用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a72b5466138f087ac4e788bc878781c3e"></a>

### `eth_adin2111_unlock()`

```c
int eth_adin2111_unlock ( const struct device * dev)
```

解锁设备访问（Device Access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | ADIN2111 设备（Device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 设备已解锁（Unlocked）。 |
| `-EPERM` | 当前线程不持有设备锁（Device Lock）。 |
| `-EINVAL` | 设备未锁定（Locked）。 |


## 7.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P244_eth_adin2111.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_zephyr__drivers__i3c__error_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__interrupt_controller__gic.h_文件参考.md)
