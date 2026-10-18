---
id: learning.zephyr-docs.api-source-supplement-reference.page-179
title: simulator.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_simulator.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h.html)。

## 179.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="abackend_8h_html"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga1097b2148a5e7e6bf9f2a67e54dd5ba5"></a>
<a id="agroup__ec__host__cmd__simulator_html_ga4ed1a006639d068f95732a1d30ba001b"></a>
<a id="agroup__ec__host__cmd__simulator_html_gaecf09d7134542c3bec94c131136c1f40"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructec__host__cmd__tx__buf_html"></a>

```c
/*
 * Copyright (c) 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_SIMULATOR_H_
#define ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_SIMULATOR_H_


/* For ec_host_cmd_backend_api_send function pointer type */
#include <zephyr/mgmt/ec_host_cmd/backend.h>

void ec_host_cmd_backend_sim_install_send_cb(ec_host_cmd_backend_api_send cb,
                                             struct ec_host_cmd_tx_buf **tx_buf);

int ec_host_cmd_backend_sim_data_received(const uint8_t *buffer, size_t len);


#endif /* ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_SIMULATOR_H_ */
```

## 179.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

供 `ec_host_cmd_backend_api_send` 函数指针类型使用。

### 注释 3：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_SIMULATOR_H_`。

## 179.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/simulator_8h.html)
- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)
- [ec_host_cmd_backend_sim_install_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#ga4ed1a006639d068f95732a1d30ba001b)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [ec_host_cmd_backend_sim_data_received](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html#gaecf09d7134542c3bec94c131136c1f40)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)

---

[上一章](P178_silabs-pinctrl-dbus.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P180_siwx91x-pinctrl.h_源码浏览.md)
