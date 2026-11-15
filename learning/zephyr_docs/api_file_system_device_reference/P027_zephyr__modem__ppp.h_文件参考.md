---
id: learning.zephyr-docs.api-file-system-device-reference.page-27
title: zephyr__modem__ppp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_modem\_\_ppp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/ppp.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="r_ga5b38e57b13e8a00217bc64bbe69a595e"></a>

```c
#define MODEM_DEV_PPP_DEFINE(_dev, _name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_DEV_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#ga5b38e57b13e8a00217bc64bbe69a595e)。

定义调制解调器点对点协议（modem PPP）模块，并将其绑定到网络接口。

<a id="r_gaeec331b2d9bccf4f5729e987b4ecf87e"></a>

```c
#define MODEM_DT_INST_PPP_DEFINE(inst, _name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_DT_INST_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaeec331b2d9bccf4f5729e987b4ecf87e)。

为蜂窝设备树实例定义调制解调器 PPP 模块。

<a id="r_ga4dbed2a468d0b2c436e2d39e621ec245"></a>

```c
#define MODEM_PPP_DEFINE(_name, _init_iface, _mtu, _buf_size)
```

相关声明：[MODEM_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#ga4dbed2a468d0b2c436e2d39e621ec245)。

定义不带设备的调制解调器 PPP 模块，并将其绑定到网络接口。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.2\_类型定义（Typedefs）

<a id="r_gafdd04a06c32e9ab70755d4f2e68deaad"></a>

```c
typedef void(* modem_ppp_init_iface) (struct net_if *iface)
```

相关声明：[modem_ppp_init_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gafdd04a06c32e9ab70755d4f2e68deaad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

第二层（L2）网络接口初始化回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.3\_函数（Functions）

<a id="r_gad3ce02dd0a6cf7067c5ca0341f807f88"></a>

```c
int modem_ppp_attach (struct modem_ppp *ppp, struct modem_pipe *pipe)
```

相关声明：[modem_ppp_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gad3ce02dd0a6cf7067c5ca0341f807f88)。

将管道（pipe）附接到实例并连接。

<a id="r_gaebb69341b2b88338b2cfccaa1c0cba0b"></a>

```c
struct net_if * modem_ppp_get_iface (struct modem_ppp *ppp)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[modem_ppp_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaebb69341b2b88338b2cfccaa1c0cba0b)。

获取调制解调器 PPP 实例绑定的网络接口。

<a id="r_gaf2177b83100647ed0894cac7fa435cb3"></a>

```c
void modem_ppp_release (struct modem_ppp *ppp)
```

相关声明：[modem_ppp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaf2177b83100647ed0894cac7fa435cb3)。

从实例释放管道。


## 27.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [zephyr/net/ppp.h](../api_source_runtime_reference/P045_ppp.h_源码浏览.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/modem/stats.h](../api_source_reference/P539_stats.h_源码浏览.md)
- [查看此文件的源码。](../api_source_interrupt_modem_reference/P005_ppp.h_源码浏览.md)
- [MODEM_DEV_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#ga5b38e57b13e8a00217bc64bbe69a595e)
- [MODEM_DT_INST_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaeec331b2d9bccf4f5729e987b4ecf87e)
- [MODEM_PPP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#ga4dbed2a468d0b2c436e2d39e621ec245)
- [modem_ppp_init_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gafdd04a06c32e9ab70755d4f2e68deaad)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [modem_ppp_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gad3ce02dd0a6cf7067c5ca0341f807f88)
- [modem_ppp_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaebb69341b2b88338b2cfccaa1c0cba0b)
- [modem_ppp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaf2177b83100647ed0894cac7fa435cb3)

---

[上一章](P026_zephyr__xen__memory.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__mpipe__base__mpipe_app_src.h_文件参考.md)
