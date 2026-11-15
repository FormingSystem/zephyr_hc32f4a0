---
id: learning.zephyr-docs.api-source-reference.page-514
title: mesh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第514章\_mesh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)。

## 514.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob__cli_8h_html"></a>
<a id="ablob__io__flash_8h_html"></a>
<a id="ablob__srv_8h_html"></a>
<a id="abluetooth_2mesh_2keys_8h_html"></a>
<a id="abrg__cfg__cli_8h_html"></a>
<a id="abrg__cfg__srv_8h_html"></a>
<a id="acdb_8h_html"></a>
<a id="acfg_8h_html"></a>
<a id="acfg__cli_8h_html"></a>
<a id="acfg__srv_8h_html"></a>
<a id="adfd__srv_8h_html"></a>
<a id="adfu__cli_8h_html"></a>
<a id="adfu__metadata_8h_html"></a>
<a id="adfu__srv_8h_html"></a>
<a id="ahealth__cli_8h_html"></a>
<a id="ahealth__srv_8h_html"></a>
<a id="aheartbeat_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alarge__comp__data__cli_8h_html"></a>
<a id="alarge__comp__data__srv_8h_html"></a>
<a id="amain_8h_html"></a>
<a id="amsg_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aod__priv__proxy__cli_8h_html"></a>
<a id="aod__priv__proxy__srv_8h_html"></a>
<a id="aop__agg__cli_8h_html"></a>
<a id="aop__agg__srv_8h_html"></a>
<a id="apriv__beacon__cli_8h_html"></a>
<a id="apriv__beacon__srv_8h_html"></a>
<a id="aproxy_8h_html"></a>
<a id="arpr__cli_8h_html"></a>
<a id="arpr__srv_8h_html"></a>
<a id="asar__cfg__cli_8h_html"></a>
<a id="asar__cfg__srv_8h_html"></a>
<a id="asol__pdu__rpl__cli_8h_html"></a>
<a id="asol__pdu__rpl__srv_8h_html"></a>
<a id="astatistic_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_H_

#include <stddef.h>

#include <zephyr/types.h>
#include <zephyr/net_buf.h>

#include <zephyr/bluetooth/mesh/keys.h>
#include <zephyr/bluetooth/mesh/msg.h>
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/main.h>
#include <zephyr/bluetooth/mesh/cfg.h>
#include <zephyr/bluetooth/mesh/cfg_srv.h>
#include <zephyr/bluetooth/mesh/health_srv.h>
#include <zephyr/bluetooth/mesh/blob_srv.h>
#include <zephyr/bluetooth/mesh/cfg_cli.h>
#include <zephyr/bluetooth/mesh/health_cli.h>
#include <zephyr/bluetooth/mesh/blob_cli.h>
#include <zephyr/bluetooth/mesh/blob_io_flash.h>
#include <zephyr/bluetooth/mesh/priv_beacon_srv.h>
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
#include <zephyr/bluetooth/mesh/dfu_srv.h>
#include <zephyr/bluetooth/mesh/dfd_srv.h>
#include <zephyr/bluetooth/mesh/dfu_cli.h>
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
#include <zephyr/bluetooth/mesh/proxy.h>
#include <zephyr/bluetooth/mesh/heartbeat.h>
#include <zephyr/bluetooth/mesh/cdb.h>
#include <zephyr/bluetooth/mesh/rpr_cli.h>
#include <zephyr/bluetooth/mesh/rpr_srv.h>
#include <zephyr/bluetooth/mesh/sar_cfg_srv.h>
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
#include <zephyr/bluetooth/mesh/op_agg_srv.h>
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
#include <zephyr/bluetooth/mesh/large_comp_data_srv.h>
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
#include <zephyr/bluetooth/mesh/od_priv_proxy_srv.h>
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_srv.h>
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
#include <zephyr/bluetooth/mesh/brg_cfg_srv.h>
#include <zephyr/bluetooth/mesh/statistic.h>

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_H_ */
```

## 514.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_H_`。

## 514.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/bluetooth/mesh/keys.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h.html)
- [zephyr/bluetooth/mesh/msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)
- [zephyr/bluetooth/mesh/cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)
- [zephyr/bluetooth/mesh/cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__srv_8h.html)
- [zephyr/bluetooth/mesh/health_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html)
- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html)
- [zephyr/bluetooth/mesh/health_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html)
- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [zephyr/bluetooth/mesh/blob_io_flash.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h.html)
- [zephyr/bluetooth/mesh/priv_beacon_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__srv_8h.html)
- [zephyr/bluetooth/mesh/priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html)
- [zephyr/bluetooth/mesh/dfu_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html)
- [zephyr/bluetooth/mesh/dfd_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html)
- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)
- [zephyr/bluetooth/mesh/dfu_metadata.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html)
- [zephyr/bluetooth/mesh/proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html)
- [zephyr/bluetooth/mesh/heartbeat.h](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html)
- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html)
- [zephyr/bluetooth/mesh/rpr_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html)
- [zephyr/bluetooth/mesh/rpr_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__srv_8h.html)
- [zephyr/bluetooth/mesh/sar_cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__srv_8h.html)
- [zephyr/bluetooth/mesh/sar_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html)
- [zephyr/bluetooth/mesh/op_agg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__srv_8h.html)
- [zephyr/bluetooth/mesh/op_agg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html)
- [zephyr/bluetooth/mesh/large_comp_data_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__srv_8h.html)
- [zephyr/bluetooth/mesh/large_comp_data_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html)
- [zephyr/bluetooth/mesh/od_priv_proxy_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__srv_8h.html)
- [zephyr/bluetooth/mesh/od_priv_proxy_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html)
- [zephyr/bluetooth/mesh/sol_pdu_rpl_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__srv_8h.html)
- [zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html)
- [zephyr/bluetooth/mesh/brg_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html)
- [zephyr/bluetooth/mesh/brg_cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h.html)
- [zephyr/bluetooth/mesh/statistic.h](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [blob_io_flash.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h.html)
- [blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [keys.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h.html)
- [brg_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html)
- [brg_cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h.html)
- [cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html)
- [cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)
- [cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html)
- [cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__srv_8h.html)
- [dfd_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html)
- [dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)
- [dfu_metadata.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html)
- [dfu_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html)
- [health_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html)
- [health_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html)
- [heartbeat.h](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [large_comp_data_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html)
- [large_comp_data_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__srv_8h.html)
- [main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)
- [msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [od_priv_proxy_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html)
- [od_priv_proxy_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__srv_8h.html)
- [op_agg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html)
- [op_agg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__srv_8h.html)
- [priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html)
- [priv_beacon_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__srv_8h.html)
- [proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html)
- [rpr_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html)
- [rpr_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__srv_8h.html)
- [sar_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html)
- [sar_cfg_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__srv_8h.html)
- [sol_pdu_rpl_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html)
- [sol_pdu_rpl_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__srv_8h.html)
- [statistic.h](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html)

---

[上一章](P513_memory.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P515_bd8lb600fs.h_源码浏览.md)
