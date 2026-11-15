---
id: learning.zephyr-docs.api-file-audio-test-reference.page-5
title: zephyr__bluetooth__classic__classic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_classic\_\_classic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙子系统（Bluetooth Subsystem）的经典蓝牙核心API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <string.h>
#include <zephyr/sys/util.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/hci_types.h>
```

查看此文件的源码。

蓝牙子系统（Bluetooth Subsystem）的经典蓝牙核心API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fbr_5Fdiscovery_5Fresult"></a>

```c
struct bt_br_discovery_result
```

相关声明：[bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)。

BR/EDR 发现结果结构体。

<a id="r_bt_5Fbr_5Fdiscovery_5Fparam"></a>

```c
struct bt_br_discovery_param
```

相关声明：[bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)。

BR/EDR 发现（Discovery）参数。

<a id="r_bt_5Fbr_5Fdiscovery_5Fcb"></a>

```c
struct bt_br_discovery_cb
```

相关声明：[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

<a id="r_bt_5Fbr_5Foob"></a>

```c
struct bt_br_oob
```

相关声明：[bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)。

<a id="r_bt_5Fbr_5Fpage_5Fscan_5Fparam"></a>

```c
struct bt_br_page_scan_param
```

相关声明：[bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)。

寻呼扫描（Page Scan）参数。

<a id="r_bt_5Fbr_5Finquiry_5Fscan_5Fparam"></a>

```c
struct bt_br_inquiry_scan_param
```

相关声明：[bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)。

BR/EDR 查询扫描（Inquiry Scan）参数。

<a id="r_bt_5Fbr_5Fbond_5Finfo"></a>

```c
struct bt_br_bond_info
```

相关声明：[bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)。

与远端设备的绑定（Bond）信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga925f510c862c9a36539f4df1db0009d6"></a>

```c
#define BT_BR_EIR_SIZE_MAX 240
```

相关声明：[BT_BR_EIR_SIZE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga925f510c862c9a36539f4df1db0009d6)。

扩展查询响应（Extended Inquiry Response）的最大大小。

<a id="r_gada5bcc61877ac75849dc3c2867ad2505"></a>

```c
#define BT_BR_SCAN_INTERVAL_MIN 0x0012
```

相关声明：[BT_BR_SCAN_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gada5bcc61877ac75849dc3c2867ad2505)。

BR/EDR 最小扫描间隔（Scan Interval）：0x0012，即 11.25 ms，单位为 0.625 ms。

<a id="r_ga03ede7b8791a42172f28882f9da8f52e"></a>

```c
#define BT_BR_SCAN_INTERVAL_MAX 0x1000
```

相关声明：[BT_BR_SCAN_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03ede7b8791a42172f28882f9da8f52e)。

BR/EDR 最大扫描间隔（Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_gac69aaf3d5de86a2ba1ab7a7194256c79"></a>

```c
#define BT_BR_SCAN_WINDOW_MIN 0x0011
```

相关声明：[BT_BR_SCAN_WINDOW_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac69aaf3d5de86a2ba1ab7a7194256c79)。

BR/EDR 最小扫描窗口（Scan Window）：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga1b29c1de2a023f5b892939cda856f491"></a>

```c
#define BT_BR_SCAN_WINDOW_MAX 0x1000
```

相关声明：[BT_BR_SCAN_WINDOW_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1b29c1de2a023f5b892939cda856f491)。

BR/EDR 最大扫描窗口（Scan Window）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_gaff027ae0fe3fbac63db9c87f8e480214"></a>

```c
#define BT_BR_SCAN_INIT(_interval, _window, _type)
```

相关声明：[BT_BR_SCAN_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaff027ae0fe3fbac63db9c87f8e480214)。

初始化基本速率扫描参数（BR Scan Parameters）。

<a id="r_ga4d053fafbc0faed58c3305efdd581838"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM(_interval, _window, _type)
```

相关声明：[BT_BR_PAGE_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4d053fafbc0faed58c3305efdd581838)。

用于内联声明 BR/EDR 寻呼扫描参数（Page Scan Parameters）的辅助宏。

<a id="r_ga8c22bfb02c45f522794e6e3f0054ffa0"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_R0
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8c22bfb02c45f522794e6e3f0054ffa0)。

R0 的默认寻呼扫描参数（Default Page Scan Parameters）。

<a id="r_ga9f20d66911eaedeb26c93281e21febb6"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_FAST_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9f20d66911eaedeb26c93281e21febb6)。

R1 的快速寻呼扫描参数（Fast Page Scan Parameters）。

<a id="r_ga6c58418072c3cb5cc35193414a20f98f"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6c58418072c3cb5cc35193414a20f98f)。

R1 的中速寻呼扫描参数（Medium Page Scan Parameters）。

<a id="r_gae2641df344fc7bd32ad0ed7c185538a7"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_SLOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae2641df344fc7bd32ad0ed7c185538a7)。

R1 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

<a id="r_gab0bcacaa4d7ddfe85918ed26b7525eb7"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R2
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_FAST_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab0bcacaa4d7ddfe85918ed26b7525eb7)。

R2 的快速寻呼扫描参数（Fast Page Scan Parameters）。

<a id="r_ga1558b2c9183c631cd8a7fa0988598184"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R2
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_SLOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1558b2c9183c631cd8a7fa0988598184)。

R2 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

<a id="r_ga7a9e4560e84fa43e7c1f3cad39bdf24e"></a>

```c
#define BT_BR_INQUIRY_SCAN_PARAM(_interval, _window, _type)
```

相关声明：[BT_BR_INQUIRY_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a9e4560e84fa43e7c1f3cad39bdf24e)。

用于内联声明 BR/EDR 查询扫描参数（Inquiry Scan Parameters）的辅助宏。

<a id="r_gabe6aa0d2210ab0507d3b06bfd7000aaa"></a>

```c
#define BT_BR_INQUIRY_SCAN_PARAM_DEFAULT
```

相关声明：[BT_BR_INQUIRY_SCAN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabe6aa0d2210ab0507d3b06bfd7000aaa)。

默认查询扫描参数（Default Inquiry Scan Parameters）。

<a id="define-members-0"></a>

### 预定义的 BR/EDR 寻呼扫描间隔与窗口（Defined BR/EDR Page Scan Intervals and Windows）

<a id="r_ga05ad85ffd00e23052ab5cbb6ff5ee709"></a>

```c
#define BT_BR_PAGE_SCAN_INTERVAL_R0 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_INTERVAL_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga05ad85ffd00e23052ab5cbb6ff5ee709)。

默认寻呼扫描间隔（Page Scan Interval），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga13e5b00e35b3c338c0326dbee03c9268"></a>

```c
#define BT_BR_PAGE_SCAN_WINDOW_R0 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_WINDOW_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga13e5b00e35b3c338c0326dbee03c9268)。

默认寻呼扫描窗口（Page Scan Window），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga17ea91d5b363d5dba321cc38e4283dbc"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R1 0x00a0
```

相关声明：[BT_BR_PAGE_SCAN_FAST_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga17ea91d5b363d5dba321cc38e4283dbc)。

快速寻呼扫描间隔（Page Scan Interval），R1：0x00a0，即 100.0 ms，单位为 0.625 ms。

<a id="r_gaf1bfd9a2c5a846a1232520de20a326eb"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_FAST_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf1bfd9a2c5a846a1232520de20a326eb)。

快速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga6c2a8ae86cb80756beee0bcbdb18c8b6"></a>

```c
#define BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6c2a8ae86cb80756beee0bcbdb18c8b6)。

中速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga61c49f57aea54f455ef89de40c354cc5"></a>

```c
#define BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga61c49f57aea54f455ef89de40c354cc5)。

中速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_gaf955175076f985e932c0ab0ed9e58743"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf955175076f985e932c0ab0ed9e58743)。

慢速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_gaf26216f17eb0142791decac9377538f4"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf26216f17eb0142791decac9377538f4)。

慢速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_gadd743fae64449eaf337566a19e06fc6d"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R2 0x1000
```

相关声明：[BT_BR_PAGE_SCAN_FAST_INTERVAL_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gadd743fae64449eaf337566a19e06fc6d)。

快速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga1bd5dcfa2c47bacca1bdaee493d261c4"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R2 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_FAST_WINDOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1bd5dcfa2c47bacca1bdaee493d261c4)。

快速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga365abe1219cb283880f93de9b7f2e3d3"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2 0x1000
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga365abe1219cb283880f93de9b7f2e3d3)。

慢速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga440177ed725266616455bd135f414ea8"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R2 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_WINDOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga440177ed725266616455bd135f414ea8)。

慢速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="define-members-1"></a>

### 预定义的 BR 查询扫描间隔与窗口（Defined BR Inquiry Scan Intervals and Windows）

<a id="r_ga1770fa93707cf5ea6b57498be1aa9b26"></a>

```c
#define BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT 0x1000
```

相关声明：[BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1770fa93707cf5ea6b57498be1aa9b26)。

默认查询扫描间隔（Inquiry Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga6bc842be90369deb05fb4720ced19395"></a>

```c
#define BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT 0x0012
```

相关声明：[BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bc842be90369deb05fb4720ced19395)。

默认查询扫描窗口（Inquiry Scan Window）：0x0012，即 11.25 ms，单位为 0.625 ms。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gab661e90ad27ce1a280cefc15c5ad040c"></a>

```c
typedef enum bt_br_conn_req_rsp(* bt_br_conn_req_func_t) (const bt_addr_t *addr, uint32_t cod)
```

相关声明：[bt_br_conn_req_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfc34fe6f398d6526acc7c5afde8a689)、[bt_br_conn_req_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab661e90ad27ce1a280cefc15c5ad040c)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

传入 BR/EDR 连接请求（Incoming Connection Requests）的回调类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_gabfc34fe6f398d6526acc7c5afde8a689"></a>

```c
enum bt_br_conn_req_rsp { BT_BR_CONN_REQ_ACCEPT_CENTRAL = BT_HCI_ROLE_CENTRAL , BT_BR_CONN_REQ_ACCEPT_PERIPHERAL = BT_HCI_ROLE_PERIPHERAL , BT_BR_CONN_REQ_REJECT_NO_RESOURCES = BT_HCI_ERR_INSUFFICIENT_RESOURCES , BT_BR_CONN_REQ_REJECT_SECURITY = BT_HCI_ERR_INSUFFICIENT_SECURITY , BT_BR_CONN_REQ_REJECT_ADDR = BT_HCI_ERR_BD_ADDR_UNACCEPTABLE }
```

相关声明：[bt_br_conn_req_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfc34fe6f398d6526acc7c5afde8a689)、[BT_BR_CONN_REQ_ACCEPT_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f)、[BT_BR_CONN_REQ_ACCEPT_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97)、[BT_BR_CONN_REQ_REJECT_NO_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a)、[BT_BR_CONN_REQ_REJECT_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35)、[BT_BR_CONN_REQ_REJECT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908)。

BR/EDR 连接请求响应码（Connection Request Response Codes）。

<a id="r_ga03757f934de6f13f95f02316b098875d"></a>

```c
enum bt_br_scan_type { BT_BR_SCAN_TYPE_STANDARD = 0 , BT_BR_SCAN_TYPE_INTERLACED = 1 }
```

相关声明：[bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)、[BT_BR_SCAN_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7)、[BT_BR_SCAN_TYPE_INTERLACED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d)。

寻呼扫描类型（Page Scan Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_ga9760190192dde5c498ec96628468be8d"></a>

```c
int bt_br_discovery_start (const struct bt_br_discovery_param *param, struct bt_br_discovery_result *results, size_t count)
```

相关声明：[bt_br_discovery_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9760190192dde5c498ec96628468be8d)、[bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)、[bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)。

开始 BR/EDR 发现（Discovery）。

<a id="r_ga567c71b49399fe7e1a5593edbf005e3a"></a>

```c
int bt_br_discovery_stop (void)
```

相关声明：[bt_br_discovery_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga567c71b49399fe7e1a5593edbf005e3a)。

停止 BR/EDR 发现（Discovery）。

<a id="r_ga430de0ad30da7322c5353941f1f6a133"></a>

```c
void bt_br_discovery_cb_register (struct bt_br_discovery_cb *cb)
```

相关声明：[bt_br_discovery_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga430de0ad30da7322c5353941f1f6a133)、[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

注册发现数据包回调（Discovery Packet Callbacks）。

<a id="r_ga25ab96ac005237aee739bf32fc1aac94"></a>

```c
void bt_br_discovery_cb_unregister (struct bt_br_discovery_cb *cb)
```

相关声明：[bt_br_discovery_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga25ab96ac005237aee739bf32fc1aac94)、[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

注销发现数据包回调（Discovery Packet Callbacks）。

<a id="r_ga2ec860d06c45098624b106b59fbab634"></a>

```c
int bt_br_oob_get_local (struct bt_br_oob *oob)
```

相关声明：[bt_br_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga2ec860d06c45098624b106b59fbab634)、[bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)。

获取 BR/EDR 本地带外信息（Out Of Band Information）。

<a id="r_gae3376fdd364e9b9d6e304ec589ba00f5"></a>

```c
int bt_br_set_discoverable (bool enable, bool limited)
```

相关声明：[bt_br_set_discoverable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae3376fdd364e9b9d6e304ec589ba00f5)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用控制器的可发现状态（Discoverable State）。

<a id="r_ga66c29ea0ccb8b8ff5610c1fc53fe1eb9"></a>

```c
int bt_br_set_connectable (bool enable, bt_br_conn_req_func_t func)
```

相关声明：[bt_br_set_connectable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga66c29ea0ccb8b8ff5610c1fc53fe1eb9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_br_conn_req_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab661e90ad27ce1a280cefc15c5ad040c)。

启用／禁用控制器的可连接状态（Connectable State）。

<a id="r_ga78c5fc5f71d08b0c800967ee7696fc83"></a>

```c
int bt_br_page_scan_update_param (const struct bt_br_page_scan_param *param)
```

相关声明：[bt_br_page_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga78c5fc5f71d08b0c800967ee7696fc83)、[bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)。

更新 BR/EDR 寻呼扫描参数（Page Scan Parameters）。

<a id="r_ga6ca71da8c9eed3d317200aa1f6babc7d"></a>

```c
int bt_br_inquiry_scan_update_param (const struct bt_br_inquiry_scan_param *param)
```

相关声明：[bt_br_inquiry_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6ca71da8c9eed3d317200aa1f6babc7d)、[bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)。

更新 BR/EDR 查询扫描参数（Inquiry Scan Parameters）。

<a id="r_ga201f64881ccc13169d072d9cc04948ba"></a>

```c
int bt_br_set_class_of_device (uint32_t cod)
```

相关声明：[bt_br_set_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga201f64881ccc13169d072d9cc04948ba)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置本地 BR/EDR 控制器的设备类别（Class of Device）。

<a id="r_gab49521adee2b653dbec04fbf833e22d9"></a>

```c
int bt_br_get_class_of_device (uint32_t *cod)
```

相关声明：[bt_br_get_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab49521adee2b653dbec04fbf833e22d9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取本地 BR/EDR 控制器的设备类别（Class of Device）。

<a id="r_gad88cf1dec20264f9bdde91571efe8dce"></a>

```c
bool bt_br_bond_exists (const bt_addr_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_br_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad88cf1dec20264f9bdde91571efe8dce)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

检查经典蓝牙设备地址（Bluetooth Classic Device Address）是否已绑定（Bonded）。

<a id="r_gaccab07100ab64fd805fe1d468bc889ac"></a>

```c
int bt_br_unpair (const bt_addr_t *addr)
```

相关声明：[bt_br_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

清除经典蓝牙配对信息（Classic Pairing Information）。

<a id="r_ga4c82193c50c616d9319c87ebcffabe66"></a>

```c
void bt_br_foreach_bond (void(*func)(const struct bt_br_bond_info *info, void *user_data), void *user_data)
```

相关声明：[bt_br_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4c82193c50c616d9319c87ebcffabe66)、[bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)。

遍历全部已有经典蓝牙绑定（Classic Bonds）。

<a id="r_gab28ba977a94f63476f360d358868f8f6"></a>

```c
int bt_br_write_eir (const struct bt_data *eir, size_t eir_count, bool fec_required)
```

相关声明：[bt_br_write_eir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab28ba977a94f63476f360d358868f8f6)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

写入扩展查询响应数据（Extended Inquiry Response Data）。


## 5.6\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P095_classic.h_源码浏览.md)
- [bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)
- [bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)
- [bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)
- [bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)
- [bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)
- [bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)
- [bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)
- [BT_BR_EIR_SIZE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga925f510c862c9a36539f4df1db0009d6)
- [BT_BR_SCAN_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gada5bcc61877ac75849dc3c2867ad2505)
- [BT_BR_SCAN_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03ede7b8791a42172f28882f9da8f52e)
- [BT_BR_SCAN_WINDOW_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac69aaf3d5de86a2ba1ab7a7194256c79)
- [BT_BR_SCAN_WINDOW_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1b29c1de2a023f5b892939cda856f491)
- [BT_BR_SCAN_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaff027ae0fe3fbac63db9c87f8e480214)
- [BT_BR_PAGE_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4d053fafbc0faed58c3305efdd581838)
- [BT_BR_PAGE_SCAN_PARAM_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8c22bfb02c45f522794e6e3f0054ffa0)
- [BT_BR_PAGE_SCAN_PARAM_FAST_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9f20d66911eaedeb26c93281e21febb6)
- [BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6c58418072c3cb5cc35193414a20f98f)
- [BT_BR_PAGE_SCAN_PARAM_SLOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae2641df344fc7bd32ad0ed7c185538a7)
- [BT_BR_PAGE_SCAN_PARAM_FAST_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab0bcacaa4d7ddfe85918ed26b7525eb7)
- [BT_BR_PAGE_SCAN_PARAM_SLOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1558b2c9183c631cd8a7fa0988598184)
- [BT_BR_INQUIRY_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a9e4560e84fa43e7c1f3cad39bdf24e)
- [BT_BR_INQUIRY_SCAN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabe6aa0d2210ab0507d3b06bfd7000aaa)
- [BT_BR_PAGE_SCAN_INTERVAL_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga05ad85ffd00e23052ab5cbb6ff5ee709)
- [BT_BR_PAGE_SCAN_WINDOW_R0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga13e5b00e35b3c338c0326dbee03c9268)
- [BT_BR_PAGE_SCAN_FAST_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga17ea91d5b363d5dba321cc38e4283dbc)
- [BT_BR_PAGE_SCAN_FAST_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf1bfd9a2c5a846a1232520de20a326eb)
- [BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6c2a8ae86cb80756beee0bcbdb18c8b6)
- [BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga61c49f57aea54f455ef89de40c354cc5)
- [BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf955175076f985e932c0ab0ed9e58743)
- [BT_BR_PAGE_SCAN_SLOW_WINDOW_R1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf26216f17eb0142791decac9377538f4)
- [BT_BR_PAGE_SCAN_FAST_INTERVAL_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gadd743fae64449eaf337566a19e06fc6d)
- [BT_BR_PAGE_SCAN_FAST_WINDOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1bd5dcfa2c47bacca1bdaee493d261c4)
- [BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga365abe1219cb283880f93de9b7f2e3d3)
- [BT_BR_PAGE_SCAN_SLOW_WINDOW_R2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga440177ed725266616455bd135f414ea8)
- [BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1770fa93707cf5ea6b57498be1aa9b26)
- [BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bc842be90369deb05fb4720ced19395)
- [bt_br_conn_req_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfc34fe6f398d6526acc7c5afde8a689)
- [bt_br_conn_req_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab661e90ad27ce1a280cefc15c5ad040c)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BT_BR_CONN_REQ_ACCEPT_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f)
- [BT_BR_CONN_REQ_ACCEPT_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97)
- [BT_BR_CONN_REQ_REJECT_NO_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a)
- [BT_BR_CONN_REQ_REJECT_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35)
- [BT_BR_CONN_REQ_REJECT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908)
- [bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)
- [BT_BR_SCAN_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7)
- [BT_BR_SCAN_TYPE_INTERLACED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d)
- [bt_br_discovery_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9760190192dde5c498ec96628468be8d)
- [bt_br_discovery_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga567c71b49399fe7e1a5593edbf005e3a)
- [bt_br_discovery_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga430de0ad30da7322c5353941f1f6a133)
- [bt_br_discovery_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga25ab96ac005237aee739bf32fc1aac94)
- [bt_br_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga2ec860d06c45098624b106b59fbab634)
- [bt_br_set_discoverable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae3376fdd364e9b9d6e304ec589ba00f5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_br_set_connectable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga66c29ea0ccb8b8ff5610c1fc53fe1eb9)
- [bt_br_page_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga78c5fc5f71d08b0c800967ee7696fc83)
- [bt_br_inquiry_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6ca71da8c9eed3d317200aa1f6babc7d)
- [bt_br_set_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga201f64881ccc13169d072d9cc04948ba)
- [bt_br_get_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab49521adee2b653dbec04fbf833e22d9)
- [bt_br_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad88cf1dec20264f9bdde91571efe8dce)
- [bt_br_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)
- [bt_br_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4c82193c50c616d9319c87ebcffabe66)
- [bt_br_write_eir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab28ba977a94f63476f360d358868f8f6)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)

<a id="header-details"></a>

---

[上一章](P004_zephyr__bluetooth__audio__cap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__clock__em32_clock.h_文件参考.md)
