---
id: learning.zephyr-docs.api-file-configuration-reference.page-69
title: zephyr__mgmt__ec_host_cmd__simulator.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_zephyr\_\_mgmt\_\_ec\_host\_cmd\_\_simulator.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于通过常规设备接口之外的方式与模拟器（Simulator）交互的命令头文件。

<a id="details"></a>

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

查看此文件的源码。

用于通过常规设备接口之外的方式与模拟器（Simulator）交互的命令头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 69.1\_函数（Functions）

<a id="r_ga4ed1a006639d068f95732a1d30ba001b"></a>

```c
void ec_host_cmd_backend_sim_install_send_cb (ec_host_cmd_backend_api_send cb, struct ec_host_cmd_tx_buf **tx_buf)
```

相关声明：[ec_host_cmd_backend_sim_install_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#ga4ed1a006639d068f95732a1d30ba001b)、[ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)、[ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)。

安装回调（Callback），在此设备向主机（Host）发送数据时调用。

<a id="r_gaecf09d7134542c3bec94c131136c1f40"></a>

```c
int ec_host_cmd_backend_sim_data_received (const uint8_t *buffer, size_t len)
```

相关声明：[ec_host_cmd_backend_sim_data_received](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#gaecf09d7134542c3bec94c131136c1f40)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

模拟接收来自主机（Host）的数据；数据由调用者传入本函数。


## 69.2\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/backend.h](../api_source_reference/P050_backend.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P179_simulator.h_源码浏览.md)
- [ec_host_cmd_backend_sim_install_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#ga4ed1a006639d068f95732a1d30ba001b)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [ec_host_cmd_backend_sim_data_received](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#gaecf09d7134542c3bec94c131136c1f40)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P068_zephyr__drivers__sensor__sgp40.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P070_zephyr__display__ssd16xx.h_文件参考.md)
