---
id: learning.zephyr-docs.api-file-reference.page-218
title: zephyr__bluetooth__mesh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第218章\_zephyr\_\_bluetooth\_\_mesh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh配置文件（Bluetooth Mesh Profile）的API。

<a id="details"></a>

```c
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
```

查看此文件的源码。

蓝牙Mesh配置文件（Bluetooth Mesh Profile）的API。


## 218.1\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [zephyr/bluetooth/mesh/keys.h](../api_source_reference/P073_keys.h_源码浏览.md)
- [zephyr/bluetooth/mesh/msg.h](../api_source_reference/P566_msg.h_源码浏览.md)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [zephyr/bluetooth/mesh/main.h](../api_source_supplement_reference/P102_main.h_源码浏览.md)
- [zephyr/bluetooth/mesh/cfg.h](../api_source_configuration_reference/P011_cfg.h_源码浏览.md)
- [zephyr/bluetooth/mesh/cfg_srv.h](../api_source_reference/P089_cfg_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/health_srv.h](../api_source_reference/P316_health_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_srv.h](../api_source_runtime_reference/P002_blob_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/cfg_cli.h](../api_source_reference/P088_cfg_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/health_cli.h](../api_source_reference/P314_health_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [zephyr/bluetooth/mesh/blob_io_flash.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h_source.html)
- [zephyr/bluetooth/mesh/priv_beacon_srv.h](../api_source_reference/P673_priv_beacon_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/priv_beacon_cli.h](../api_source_reference/P672_priv_beacon_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/dfu_srv.h](../api_source_configuration_reference/P016_dfu_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/dfd_srv.h](../api_source_reference/P125_dfd_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/dfu_cli.h](../api_source_supplement_reference/P039_dfu_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/dfu_metadata.h](../api_source_reference/P127_dfu_metadata.h_源码浏览.md)
- [zephyr/bluetooth/mesh/proxy.h](../api_source_reference/P676_proxy.h_源码浏览.md)
- [zephyr/bluetooth/mesh/heartbeat.h](../api_source_reference/P317_heartbeat.h_源码浏览.md)
- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)
- [zephyr/bluetooth/mesh/rpr_cli.h](../api_source_supplement_reference/P169_rpr_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/rpr_srv.h](../api_source_reference/P732_rpr_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/sar_cfg_srv.h](../api_source_reference/P746_sar_cfg_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/sar_cfg_cli.h](../api_source_supplement_reference/P175_sar_cfg_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/op_agg_srv.h](../api_source_reference/P634_op_agg_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/op_agg_cli.h](../api_source_reference/P633_op_agg_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/large_comp_data_srv.h](../api_source_reference/P436_large_comp_data_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/large_comp_data_cli.h](../api_source_reference/P435_large_comp_data_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/od_priv_proxy_srv.h](../api_source_reference/P632_od_priv_proxy_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/od_priv_proxy_cli.h](../api_source_reference/P631_od_priv_proxy_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/sol_pdu_rpl_srv.h](../api_source_reference/P806_sol_pdu_rpl_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h](../api_source_reference/P805_sol_pdu_rpl_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/brg_cfg_cli.h](../api_source_reference/P077_brg_cfg_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/brg_cfg_srv.h](../api_source_reference/P078_brg_cfg_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/statistic.h](../api_source_reference/P817_statistic.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P514_mesh.h_源码浏览.md)

<a id="header-details"></a>

---

[上一章](P217_zephyr__drivers__memc__memc_stm32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P219_zephyr__drivers__mfd__max31790.h_文件参考.md)
