---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-1
title: 蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）

<a id="details"></a>

蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.1\_基础模型（Foundation Models）

<a id="r_ga004d8d1be55b2aec56abbeeca1d118d8"></a>

```c
#define BT_MESH_MODEL_ID_CFG_SRV 0x0000
```

相关声明：[BT_MESH_MODEL_ID_CFG_SRV](#ga004d8d1be55b2aec56abbeeca1d118d8)。

配置服务器（Configuration Server）。

<a id="r_ga3f8442dcd1a110ea0d0023f50057139f"></a>

```c
#define BT_MESH_MODEL_ID_CFG_CLI 0x0001
```

相关声明：[BT_MESH_MODEL_ID_CFG_CLI](#ga3f8442dcd1a110ea0d0023f50057139f)。

配置客户端（Configuration Client）。

<a id="r_ga6416216348d7186f91175ca50bb8c903"></a>

```c
#define BT_MESH_MODEL_ID_HEALTH_SRV 0x0002
```

相关声明：[BT_MESH_MODEL_ID_HEALTH_SRV](#ga6416216348d7186f91175ca50bb8c903)。

健康服务器（Health Server）。

<a id="r_gab58b85b7a77feeb579973177c12bb446"></a>

```c
#define BT_MESH_MODEL_ID_HEALTH_CLI 0x0003
```

相关声明：[BT_MESH_MODEL_ID_HEALTH_CLI](#gab58b85b7a77feeb579973177c12bb446)。

健康客户端（Health Client）。

<a id="r_ga9c7d1c5dfb87a5ce50c08747af47414f"></a>

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_SRV 0x0004
```

相关声明：[BT_MESH_MODEL_ID_REMOTE_PROV_SRV](#ga9c7d1c5dfb87a5ce50c08747af47414f)。

远程配网服务器（Remote Provisioning Server）。

<a id="r_gaf373eb4d8af5d6bee76a821bd4d5e48c"></a>

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_CLI 0x0005
```

相关声明：[BT_MESH_MODEL_ID_REMOTE_PROV_CLI](#gaf373eb4d8af5d6bee76a821bd4d5e48c)。

远程配网客户端（Remote Provisioning Client）。

<a id="r_ga599d00e9d63ade6ed1a6803579c1e16e"></a>

```c
#define BT_MESH_MODEL_ID_BRG_CFG_SRV 0x0008
```

相关声明：[BT_MESH_MODEL_ID_BRG_CFG_SRV](#ga599d00e9d63ade6ed1a6803579c1e16e)。

桥接配置服务器（Bridge Configuration Sever），原文将 Server 写作 Sever。

<a id="r_ga9c776b4befd21c15f4867d906f631257"></a>

```c
#define BT_MESH_MODEL_ID_BRG_CFG_CLI 0x0009
```

相关声明：[BT_MESH_MODEL_ID_BRG_CFG_CLI](#ga9c776b4befd21c15f4867d906f631257)。

桥接配置客户端（Bridge Configuration Client）。

<a id="r_gacca0e355982935cfbde46a06b09a7bec"></a>

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_SRV 0x000a
```

相关声明：[BT_MESH_MODEL_ID_PRIV_BEACON_SRV](#gacca0e355982935cfbde46a06b09a7bec)。

私有信标服务器（Private Beacon Server）。

<a id="r_gab3b21cbee4e11319a6e0ba3b02b24a91"></a>

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_CLI 0x000b
```

相关声明：[BT_MESH_MODEL_ID_PRIV_BEACON_CLI](#gab3b21cbee4e11319a6e0ba3b02b24a91)。

私有信标客户端（Private Beacon Client）。

<a id="r_ga1e9d8be1d2e65d2977aea0306b015258"></a>

```c
#define BT_MESH_MODEL_ID_SAR_CFG_SRV 0x000e
```

相关声明：[BT_MESH_MODEL_ID_SAR_CFG_SRV](#ga1e9d8be1d2e65d2977aea0306b015258)。

分段与重组配置服务器（SAR Configuration Server）。

<a id="r_gaf214eb7eef3530919432b62ff9b353c3"></a>

```c
#define BT_MESH_MODEL_ID_SAR_CFG_CLI 0x000f
```

相关声明：[BT_MESH_MODEL_ID_SAR_CFG_CLI](#gaf214eb7eef3530919432b62ff9b353c3)。

分段与重组配置客户端（SAR Configuration Client）。

<a id="r_ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a"></a>

```c
#define BT_MESH_MODEL_ID_OP_AGG_SRV 0x0010
```

相关声明：[BT_MESH_MODEL_ID_OP_AGG_SRV](#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)。

操作码聚合器服务器（Opcodes Aggregator Server）。

<a id="r_gabac62a77e7d2d7677af21c33c8629187"></a>

```c
#define BT_MESH_MODEL_ID_OP_AGG_CLI 0x0011
```

相关声明：[BT_MESH_MODEL_ID_OP_AGG_CLI](#gabac62a77e7d2d7677af21c33c8629187)。

操作码聚合器客户端（Opcodes Aggregator Client）。

<a id="r_gaec3abd6a0bd7b07a71fe5ed6a7a6931a"></a>

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV 0x0012
```

相关声明：[BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV](#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)。

大型组成数据服务器（Large Composition Data Server）。

<a id="r_ga729d67e4183457932e4c837d65abd842"></a>

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI 0x0013
```

相关声明：[BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI](#ga729d67e4183457932e4c837d65abd842)。

大型组成数据客户端（Large Composition Data Client）。

<a id="r_ga165bc198dadaa0d534ec82eb8192ebc0"></a>

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV 0x0014
```

相关声明：[BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV](#ga165bc198dadaa0d534ec82eb8192ebc0)。

请求PDU重放保护列表配置服务器（Solicitation PDU RPL Configuration Server）。

<a id="r_ga6e747dd364bcfaa368e37c5f01afd530"></a>

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI 0x0015
```

相关声明：[BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI](#ga6e747dd364bcfaa368e37c5f01afd530)。

请求PDU重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）。

<a id="r_gaddc0bd645180a57cb9cd36745b84f7a1"></a>

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV 0x000c
```

相关声明：[BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV](#gaddc0bd645180a57cb9cd36745b84f7a1)。

私有代理服务器（Private Proxy Server）。

<a id="r_gadd36546fb2cb6d1c731f7ae7674af6a7"></a>

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI 0x000d
```

相关声明：[BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI](#gadd36546fb2cb6d1c731f7ae7674af6a7)。

私有代理客户端（Private Proxy Client）。

## 1.2\_Mesh模型规范中的模型（Models from the Mesh Model Specification）

<a id="r_ga83e1ed5398d513cfeb900e41655aa4d8"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_SRV 0x1000
```

相关声明：[BT_MESH_MODEL_ID_GEN_ONOFF_SRV](#ga83e1ed5398d513cfeb900e41655aa4d8)。

通用开关服务器（Generic OnOff Server）。

<a id="r_ga4f0eee2569b518a5e4250f5b7b294fed"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_CLI 0x1001
```

相关声明：[BT_MESH_MODEL_ID_GEN_ONOFF_CLI](#ga4f0eee2569b518a5e4250f5b7b294fed)。

通用开关客户端（Generic OnOff Client）。

<a id="r_ga7f10a8332b1406c3ad628b9679e1d7cb"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_SRV 0x1002
```

相关声明：[BT_MESH_MODEL_ID_GEN_LEVEL_SRV](#ga7f10a8332b1406c3ad628b9679e1d7cb)。

通用级别服务器（Generic Level Server）。

<a id="r_ga462c578845a17b20cdb3e008f74f93a6"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_CLI 0x1003
```

相关声明：[BT_MESH_MODEL_ID_GEN_LEVEL_CLI](#ga462c578845a17b20cdb3e008f74f93a6)。

通用级别客户端（Generic Level Client）。

<a id="r_ga004d5ec0870d47a8d37182e5b0c089a5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV 0x1004
```

相关声明：[BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV](#ga004d5ec0870d47a8d37182e5b0c089a5)。

通用默认过渡时间服务器（Generic Default Transition Time Server）。

<a id="r_gafa1c6a7d857fe13a139ce2242b4e62f5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI 0x1005
```

相关声明：[BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI](#gafa1c6a7d857fe13a139ce2242b4e62f5)。

通用默认过渡时间客户端（Generic Default Transition Time Client）。

<a id="r_ga09ac731fff09146ec68557f00e8294e0"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV 0x1006
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV](#ga09ac731fff09146ec68557f00e8294e0)。

通用电源开关服务器（Generic Power OnOff Server）。

<a id="r_ga2a6dad18792ba7f1d81d6c9a1c65f90a"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV 0x1007
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV](#ga2a6dad18792ba7f1d81d6c9a1c65f90a)。

通用电源开关设置服务器（Generic Power OnOff Setup Server）。

<a id="r_ga9f6544f7b87f39d0792ea2de13cd45f1"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI 0x1008
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI](#ga9f6544f7b87f39d0792ea2de13cd45f1)。

通用电源开关客户端（Generic Power OnOff Client）。

<a id="r_gadd30afe63f89e9c1778e56f722fd82f9"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV 0x1009
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV](#gadd30afe63f89e9c1778e56f722fd82f9)。

通用功率级别服务器（Generic Power Level Server）。

<a id="r_ga1ff6ec64ce3a86d1cfd00fc98e89c0a5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV 0x100a
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV](#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)。

通用功率级别设置服务器（Generic Power Level Setup Server）。

<a id="r_ga8420454c35afc12c62ede55942f3b6d3"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI 0x100b
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI](#ga8420454c35afc12c62ede55942f3b6d3)。

通用功率级别客户端（Generic Power Level Client）。

<a id="r_gacf891135f54fb1fbb62beb812235619e"></a>

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_SRV 0x100c
```

相关声明：[BT_MESH_MODEL_ID_GEN_BATTERY_SRV](#gacf891135f54fb1fbb62beb812235619e)。

通用电池服务器（Generic Battery Server）。

<a id="r_ga34bb3d4839e9685ec55f8285aac9a79f"></a>

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_CLI 0x100d
```

相关声明：[BT_MESH_MODEL_ID_GEN_BATTERY_CLI](#ga34bb3d4839e9685ec55f8285aac9a79f)。

通用电池客户端（Generic Battery Client）。

<a id="r_gad516f513c5c942fbfee65b85332b105e"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SRV 0x100e
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_SRV](#gad516f513c5c942fbfee65b85332b105e)。

通用位置服务器（Generic Location Server）。

<a id="r_ga240d1ed34b7341627773cce862f85620"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV 0x100f
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV](#ga240d1ed34b7341627773cce862f85620)。

通用位置设置服务器（Generic Location Setup Server）。

<a id="r_ga8fa01ddb1f4de4d61500bb650243390d"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_CLI 0x1010
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_CLI](#ga8fa01ddb1f4de4d61500bb650243390d)。

通用位置客户端（Generic Location Client）。

<a id="r_ga3cc6862e9c72f9282055c5cda2343c89"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV 0x1011
```

相关声明：[BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV](#ga3cc6862e9c72f9282055c5cda2343c89)。

通用管理员属性服务器（Generic Admin Property Server）。

<a id="r_ga32e09ddfebd2e8b22da9a3102e116aae"></a>

```c
#define BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV 0x1012
```

相关声明：[BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV](#ga32e09ddfebd2e8b22da9a3102e116aae)。

通用制造商属性服务器（Generic Manufacturer Property Server）。

<a id="r_ga4b7b6a4b47e87de94ccf11ef1abd64b9"></a>

```c
#define BT_MESH_MODEL_ID_GEN_USER_PROP_SRV 0x1013
```

相关声明：[BT_MESH_MODEL_ID_GEN_USER_PROP_SRV](#ga4b7b6a4b47e87de94ccf11ef1abd64b9)。

通用用户属性服务器（Generic User Property Server）。

<a id="r_ga20906658018ef26114d8a6656c258f62"></a>

```c
#define BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV 0x1014
```

相关声明：[BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV](#ga20906658018ef26114d8a6656c258f62)。

通用客户端属性服务器（Generic Client Property Server）。

<a id="r_ga69455e5b1e6def3d909c4bb6e0dee9ae"></a>

```c
#define BT_MESH_MODEL_ID_GEN_PROP_CLI 0x1015
```

相关声明：[BT_MESH_MODEL_ID_GEN_PROP_CLI](#ga69455e5b1e6def3d909c4bb6e0dee9ae)。

通用属性客户端（Generic Property Client）。

<a id="r_ga3e0dcb14f46f6076e5b1b114b977f630"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_SRV 0x1100
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_SRV](#ga3e0dcb14f46f6076e5b1b114b977f630)。

传感器服务器（Sensor Server）。

<a id="r_gad10780bfc1c16866fa28de750e56bec3"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_SETUP_SRV 0x1101
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_SETUP_SRV](#gad10780bfc1c16866fa28de750e56bec3)。

传感器设置服务器（Sensor Setup Server）。

<a id="r_ga8f1e4ff66d388627dbe91b2f8d4ed358"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_CLI 0x1102
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_CLI](#ga8f1e4ff66d388627dbe91b2f8d4ed358)。

传感器客户端（Sensor Client）。

<a id="r_ga93fbf1c661a75d70fdbd2a599353eb94"></a>

```c
#define BT_MESH_MODEL_ID_TIME_SRV 0x1200
```

相关声明：[BT_MESH_MODEL_ID_TIME_SRV](#ga93fbf1c661a75d70fdbd2a599353eb94)。

时间服务器（Time Server）。

<a id="r_ga2725121dc8c2c21c0ee469fe4348f45f"></a>

```c
#define BT_MESH_MODEL_ID_TIME_SETUP_SRV 0x1201
```

相关声明：[BT_MESH_MODEL_ID_TIME_SETUP_SRV](#ga2725121dc8c2c21c0ee469fe4348f45f)。

时间设置服务器（Time Setup Server）。

<a id="r_ga500df90af7989794c5d72e760e5e65c6"></a>

```c
#define BT_MESH_MODEL_ID_TIME_CLI 0x1202
```

相关声明：[BT_MESH_MODEL_ID_TIME_CLI](#ga500df90af7989794c5d72e760e5e65c6)。

时间客户端（Time Client）。

<a id="r_gaaa5554e3d48ae101596476e6bd6caf67"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_SRV 0x1203
```

相关声明：[BT_MESH_MODEL_ID_SCENE_SRV](#gaaa5554e3d48ae101596476e6bd6caf67)。

场景服务器（Scene Server）。

<a id="r_gaa3b08fc8788684abb960fa3516726264"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_SETUP_SRV 0x1204
```

相关声明：[BT_MESH_MODEL_ID_SCENE_SETUP_SRV](#gaa3b08fc8788684abb960fa3516726264)。

场景设置服务器（Scene Setup Server）。

<a id="r_gad60472aa004a8a913aeb63ef62c45857"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_CLI 0x1205
```

相关声明：[BT_MESH_MODEL_ID_SCENE_CLI](#gad60472aa004a8a913aeb63ef62c45857)。

场景客户端（Scene Client）。

<a id="r_ga82b723752e240f22b9bcc8dc3dd10eb9"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SRV 0x1206
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_SRV](#ga82b723752e240f22b9bcc8dc3dd10eb9)。

调度器服务器（Scheduler Server）。

<a id="r_ga3dbec5a3b82cb25a142c4bc851e3fe0e"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV 0x1207
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV](#ga3dbec5a3b82cb25a142c4bc851e3fe0e)。

调度器设置服务器（Scheduler Setup Server）。

<a id="r_gac743b26cf7e746b16302c25e8cd56221"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_CLI 0x1208
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_CLI](#gac743b26cf7e746b16302c25e8cd56221)。

调度器客户端（Scheduler Client）。

<a id="r_ga16df49e84e84d0ae4a6ab5d5f3f1b2b6"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV 0x1300
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV](#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)。

灯光亮度服务器（Light Lightness Server）。

<a id="r_gadb93b2ed2256a5c9c3f66237841b1bf5"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV 0x1301
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV](#gadb93b2ed2256a5c9c3f66237841b1bf5)。

灯光亮度设置服务器（Light Lightness Setup Server）。

<a id="r_ga960055723dec7b3b366efa7c49cafc2e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI 0x1302
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI](#ga960055723dec7b3b366efa7c49cafc2e)。

灯光亮度客户端（Light Lightness Client）。

<a id="r_gaa9a211341c5b3283b9b0e0842adef053"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SRV 0x1303
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_SRV](#gaa9a211341c5b3283b9b0e0842adef053)。

灯光色温与亮度服务器（Light CTL Server）。

<a id="r_ga28ac69b2dbeec70bae4bd3c0381e9e93"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV 0x1304
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV](#ga28ac69b2dbeec70bae4bd3c0381e9e93)。

灯光色温与亮度设置服务器（Light CTL Setup Server）。

<a id="r_ga58fc8d99b746b0061177ac5d95341da1"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_CLI 0x1305
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_CLI](#ga58fc8d99b746b0061177ac5d95341da1)。

灯光色温与亮度客户端（Light CTL Client）。

<a id="r_gafcb1f1ea20bb78b78a9ead4bfdbe3e47"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV 0x1306
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV](#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)。

灯光色温服务器（Light CTL Temperature Server）。

<a id="r_gaa0ddc753a226060d014dcd368feab17e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SRV 0x1307
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SRV](#gaa0ddc753a226060d014dcd368feab17e)。

灯光色相、饱和度与亮度服务器（Light HSL Server）。

<a id="r_ga574d3ba3f629bdbffc8f15db931a263a"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV 0x1308
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV](#ga574d3ba3f629bdbffc8f15db931a263a)。

灯光色相、饱和度与亮度设置服务器（Light HSL Setup Server）。

<a id="r_ga2d111a352322be8e33ba0cba0feb3f0c"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_CLI 0x1309
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_CLI](#ga2d111a352322be8e33ba0cba0feb3f0c)。

灯光色相、饱和度与亮度客户端（Light HSL Client）。

<a id="r_ga865952346db9336a255c71bcb5f09774"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV 0x130a
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV](#ga865952346db9336a255c71bcb5f09774)。

灯光HSL色相服务器（Light HSL Hue Server）。

<a id="r_gae55004e70670a8711e18e9c9b3428720"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV 0x130b
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV](#gae55004e70670a8711e18e9c9b3428720)。

灯光HSL饱和度服务器（Light HSL Saturation Server）。

<a id="r_ga29e1a90f166d88b6773d9b7ccf08e1c7"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SRV 0x130c
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_SRV](#ga29e1a90f166d88b6773d9b7ccf08e1c7)。

灯光色度与亮度服务器（Light xyL Server）。

<a id="r_ga4addae460d6b3c0a914198695b3e31ea"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV 0x130d
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV](#ga4addae460d6b3c0a914198695b3e31ea)。

灯光色度与亮度设置服务器（Light xyL Setup Server）。

<a id="r_ga0ca4d9997e6016b5c27f42549d42a99d"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_CLI 0x130e
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_CLI](#ga0ca4d9997e6016b5c27f42549d42a99d)。

灯光色度与亮度客户端（Light xyL Client）。

<a id="r_ga789412252034939539ba45e4bf21e3e2"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SRV 0x130f
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_SRV](#ga789412252034939539ba45e4bf21e3e2)。

灯光亮度控制服务器（Light LC Server）。

<a id="r_ga436358740bb64d845aa4d849d462a12e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV 0x1310
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV](#ga436358740bb64d845aa4d849d462a12e)。

灯光亮度控制设置服务器（Light LC Setup Server）。

<a id="r_gaadd48b07e1eb53df24df40b7ea412e90"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_CLI 0x1311
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_CLI](#gaadd48b07e1eb53df24df40b7ea412e90)。

灯光亮度控制客户端（Light LC Client）。

## 1.3\_Mesh二进制大对象传输模型规范中的模型（Models from the Mesh Binary Large Object Transfer Model Specification）

<a id="r_gae85d4cf7aad4e94582c24f79d6f60904"></a>

```c
#define BT_MESH_MODEL_ID_BLOB_SRV 0x1400
```

相关声明：[BT_MESH_MODEL_ID_BLOB_SRV](#gae85d4cf7aad4e94582c24f79d6f60904)。

二进制大对象传输服务器（BLOB Transfer Server）。

<a id="r_ga17e2e59a1344e623fe9fec6e27b7f22e"></a>

```c
#define BT_MESH_MODEL_ID_BLOB_CLI 0x1401
```

相关声明：[BT_MESH_MODEL_ID_BLOB_CLI](#ga17e2e59a1344e623fe9fec6e27b7f22e)。

二进制大对象传输客户端（BLOB Transfer Client）。

## 1.4\_Mesh设备固件更新模型规范中的模型（Models from the Mesh Device Firmware Update Model Specification）

<a id="r_ga0215c2c8cd16ab6536ea243864f9604e"></a>

```c
#define BT_MESH_MODEL_ID_DFU_SRV 0x1402
```

相关声明：[BT_MESH_MODEL_ID_DFU_SRV](#ga0215c2c8cd16ab6536ea243864f9604e)。

固件更新服务器（Firmware Update Server）。

<a id="r_gaf477a37238ec577000a646af40862ee1"></a>

```c
#define BT_MESH_MODEL_ID_DFU_CLI 0x1403
```

相关声明：[BT_MESH_MODEL_ID_DFU_CLI](#gaf477a37238ec577000a646af40862ee1)。

固件更新客户端（Firmware Update Client）。

<a id="r_gaf4309dea32d05274f8f3a6ea45faba38"></a>

```c
#define BT_MESH_MODEL_ID_DFD_SRV 0x1404
```

相关声明：[BT_MESH_MODEL_ID_DFD_SRV](#gaf4309dea32d05274f8f3a6ea45faba38)。

固件分发服务器（Firmware Distribution Server）。

<a id="r_ga87d3b5cc207dc3b51e85c9594bb98cad"></a>

```c
#define BT_MESH_MODEL_ID_DFD_CLI 0x1405
```

相关声明：[BT_MESH_MODEL_ID_DFD_CLI](#ga87d3b5cc207dc3b51e85c9594bb98cad)。

固件分发客户端（Firmware Distribution Client）。

## 1.5\_详细说明（Detailed Documentation）

<a id="ga17e2e59a1344e623fe9fec6e27b7f22e"></a>

### `BT_MESH_MODEL_ID_BLOB_CLI`

```c
#define BT_MESH_MODEL_ID_BLOB_CLI 0x1401
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

二进制大对象传输客户端（BLOB Transfer Client）。

<a id="gae85d4cf7aad4e94582c24f79d6f60904"></a>

### `BT_MESH_MODEL_ID_BLOB_SRV`

```c
#define BT_MESH_MODEL_ID_BLOB_SRV 0x1400
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

二进制大对象传输服务器（BLOB Transfer Server）。

<a id="ga9c776b4befd21c15f4867d906f631257"></a>

### `BT_MESH_MODEL_ID_BRG_CFG_CLI`

```c
#define BT_MESH_MODEL_ID_BRG_CFG_CLI 0x0009
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

桥接配置客户端（Bridge Configuration Client）。

<a id="ga599d00e9d63ade6ed1a6803579c1e16e"></a>

### `BT_MESH_MODEL_ID_BRG_CFG_SRV`

```c
#define BT_MESH_MODEL_ID_BRG_CFG_SRV 0x0008
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

桥接配置服务器（Bridge Configuration Sever），原文将 Server 写作 Sever。

<a id="ga3f8442dcd1a110ea0d0023f50057139f"></a>

### `BT_MESH_MODEL_ID_CFG_CLI`

```c
#define BT_MESH_MODEL_ID_CFG_CLI 0x0001
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

配置客户端（Configuration Client）。

<a id="ga004d8d1be55b2aec56abbeeca1d118d8"></a>

### `BT_MESH_MODEL_ID_CFG_SRV`

```c
#define BT_MESH_MODEL_ID_CFG_SRV 0x0000
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

配置服务器（Configuration Server）。

<a id="ga87d3b5cc207dc3b51e85c9594bb98cad"></a>

### `BT_MESH_MODEL_ID_DFD_CLI`

```c
#define BT_MESH_MODEL_ID_DFD_CLI 0x1405
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

固件分发客户端（Firmware Distribution Client）。

<a id="gaf4309dea32d05274f8f3a6ea45faba38"></a>

### `BT_MESH_MODEL_ID_DFD_SRV`

```c
#define BT_MESH_MODEL_ID_DFD_SRV 0x1404
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

固件分发服务器（Firmware Distribution Server）。

<a id="gaf477a37238ec577000a646af40862ee1"></a>

### `BT_MESH_MODEL_ID_DFU_CLI`

```c
#define BT_MESH_MODEL_ID_DFU_CLI 0x1403
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

固件更新客户端（Firmware Update Client）。

<a id="ga0215c2c8cd16ab6536ea243864f9604e"></a>

### `BT_MESH_MODEL_ID_DFU_SRV`

```c
#define BT_MESH_MODEL_ID_DFU_SRV 0x1402
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

固件更新服务器（Firmware Update Server）。

<a id="ga3cc6862e9c72f9282055c5cda2343c89"></a>

### `BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV 0x1011
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用管理员属性服务器（Generic Admin Property Server）。

<a id="ga34bb3d4839e9685ec55f8285aac9a79f"></a>

### `BT_MESH_MODEL_ID_GEN_BATTERY_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_CLI 0x100d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电池客户端（Generic Battery Client）。

<a id="gacf891135f54fb1fbb62beb812235619e"></a>

### `BT_MESH_MODEL_ID_GEN_BATTERY_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_SRV 0x100c
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电池服务器（Generic Battery Server）。

<a id="ga20906658018ef26114d8a6656c258f62"></a>

### `BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV 0x1014
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用客户端属性服务器（Generic Client Property Server）。

<a id="gafa1c6a7d857fe13a139ce2242b4e62f5"></a>

### `BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI 0x1005
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用默认过渡时间客户端（Generic Default Transition Time Client）。

<a id="ga004d5ec0870d47a8d37182e5b0c089a5"></a>

### `BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV 0x1004
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用默认过渡时间服务器（Generic Default Transition Time Server）。

<a id="ga462c578845a17b20cdb3e008f74f93a6"></a>

### `BT_MESH_MODEL_ID_GEN_LEVEL_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_CLI 0x1003
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用级别客户端（Generic Level Client）。

<a id="ga7f10a8332b1406c3ad628b9679e1d7cb"></a>

### `BT_MESH_MODEL_ID_GEN_LEVEL_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_SRV 0x1002
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用级别服务器（Generic Level Server）。

<a id="ga8fa01ddb1f4de4d61500bb650243390d"></a>

### `BT_MESH_MODEL_ID_GEN_LOCATION_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_CLI 0x1010
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用位置客户端（Generic Location Client）。

<a id="ga240d1ed34b7341627773cce862f85620"></a>

### `BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV`

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV 0x100f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用位置设置服务器（Generic Location Setup Server）。

<a id="gad516f513c5c942fbfee65b85332b105e"></a>

### `BT_MESH_MODEL_ID_GEN_LOCATION_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SRV 0x100e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用位置服务器（Generic Location Server）。

<a id="ga32e09ddfebd2e8b22da9a3102e116aae"></a>

### `BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV 0x1012
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用制造商属性服务器（Generic Manufacturer Property Server）。

<a id="ga4f0eee2569b518a5e4250f5b7b294fed"></a>

### `BT_MESH_MODEL_ID_GEN_ONOFF_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_CLI 0x1001
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用开关客户端（Generic OnOff Client）。

<a id="ga83e1ed5398d513cfeb900e41655aa4d8"></a>

### `BT_MESH_MODEL_ID_GEN_ONOFF_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_SRV 0x1000
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用开关服务器（Generic OnOff Server）。

<a id="ga8420454c35afc12c62ede55942f3b6d3"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI 0x100b
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用功率级别客户端（Generic Power Level Client）。

<a id="ga1ff6ec64ce3a86d1cfd00fc98e89c0a5"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV 0x100a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用功率级别设置服务器（Generic Power Level Setup Server）。

<a id="gadd30afe63f89e9c1778e56f722fd82f9"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV 0x1009
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用功率级别服务器（Generic Power Level Server）。

<a id="ga9f6544f7b87f39d0792ea2de13cd45f1"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI 0x1008
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电源开关客户端（Generic Power OnOff Client）。

<a id="ga2a6dad18792ba7f1d81d6c9a1c65f90a"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV 0x1007
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电源开关设置服务器（Generic Power OnOff Setup Server）。

<a id="ga09ac731fff09146ec68557f00e8294e0"></a>

### `BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV 0x1006
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电源开关服务器（Generic Power OnOff Server）。

<a id="ga69455e5b1e6def3d909c4bb6e0dee9ae"></a>

### `BT_MESH_MODEL_ID_GEN_PROP_CLI`

```c
#define BT_MESH_MODEL_ID_GEN_PROP_CLI 0x1015
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用属性客户端（Generic Property Client）。

<a id="ga4b7b6a4b47e87de94ccf11ef1abd64b9"></a>

### `BT_MESH_MODEL_ID_GEN_USER_PROP_SRV`

```c
#define BT_MESH_MODEL_ID_GEN_USER_PROP_SRV 0x1013
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用用户属性服务器（Generic User Property Server）。

<a id="gab58b85b7a77feeb579973177c12bb446"></a>

### `BT_MESH_MODEL_ID_HEALTH_CLI`

```c
#define BT_MESH_MODEL_ID_HEALTH_CLI 0x0003
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

健康客户端（Health Client）。

<a id="ga6416216348d7186f91175ca50bb8c903"></a>

### `BT_MESH_MODEL_ID_HEALTH_SRV`

```c
#define BT_MESH_MODEL_ID_HEALTH_SRV 0x0002
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

健康服务器（Health Server）。

<a id="ga729d67e4183457932e4c837d65abd842"></a>

### `BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI`

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI 0x0013
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

大型组成数据客户端（Large Composition Data Client）。

<a id="gaec3abd6a0bd7b07a71fe5ed6a7a6931a"></a>

### `BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV`

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV 0x0012
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

大型组成数据服务器（Large Composition Data Server）。

<a id="ga58fc8d99b746b0061177ac5d95341da1"></a>

### `BT_MESH_MODEL_ID_LIGHT_CTL_CLI`

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_CLI 0x1305
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色温与亮度客户端（Light CTL Client）。

<a id="ga28ac69b2dbeec70bae4bd3c0381e9e93"></a>

### `BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV 0x1304
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色温与亮度设置服务器（Light CTL Setup Server）。

<a id="gaa9a211341c5b3283b9b0e0842adef053"></a>

### `BT_MESH_MODEL_ID_LIGHT_CTL_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SRV 0x1303
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色温与亮度服务器（Light CTL Server）。

<a id="gafcb1f1ea20bb78b78a9ead4bfdbe3e47"></a>

### `BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV 0x1306
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色温服务器（Light CTL Temperature Server）。

<a id="ga2d111a352322be8e33ba0cba0feb3f0c"></a>

### `BT_MESH_MODEL_ID_LIGHT_HSL_CLI`

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_CLI 0x1309
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色相、饱和度与亮度客户端（Light HSL Client）。

<a id="ga865952346db9336a255c71bcb5f09774"></a>

### `BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV 0x130a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光HSL色相服务器（Light HSL Hue Server）。

<a id="gae55004e70670a8711e18e9c9b3428720"></a>

### `BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV 0x130b
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光HSL饱和度服务器（Light HSL Saturation Server）。

<a id="ga574d3ba3f629bdbffc8f15db931a263a"></a>

### `BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV 0x1308
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色相、饱和度与亮度设置服务器（Light HSL Setup Server）。

<a id="gaa0ddc753a226060d014dcd368feab17e"></a>

### `BT_MESH_MODEL_ID_LIGHT_HSL_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SRV 0x1307
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色相、饱和度与亮度服务器（Light HSL Server）。

<a id="gaadd48b07e1eb53df24df40b7ea412e90"></a>

### `BT_MESH_MODEL_ID_LIGHT_LC_CLI`

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_CLI 0x1311
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度控制客户端（Light LC Client）。

<a id="ga436358740bb64d845aa4d849d462a12e"></a>

### `BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV 0x1310
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度控制设置服务器（Light LC Setup Server）。

<a id="ga789412252034939539ba45e4bf21e3e2"></a>

### `BT_MESH_MODEL_ID_LIGHT_LC_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SRV 0x130f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度控制服务器（Light LC Server）。

<a id="ga960055723dec7b3b366efa7c49cafc2e"></a>

### `BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI`

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI 0x1302
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度客户端（Light Lightness Client）。

<a id="gadb93b2ed2256a5c9c3f66237841b1bf5"></a>

### `BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV 0x1301
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度设置服务器（Light Lightness Setup Server）。

<a id="ga16df49e84e84d0ae4a6ab5d5f3f1b2b6"></a>

### `BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV 0x1300
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光亮度服务器（Light Lightness Server）。

<a id="ga0ca4d9997e6016b5c27f42549d42a99d"></a>

### `BT_MESH_MODEL_ID_LIGHT_XYL_CLI`

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_CLI 0x130e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色度与亮度客户端（Light xyL Client）。

<a id="ga4addae460d6b3c0a914198695b3e31ea"></a>

### `BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV 0x130d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色度与亮度设置服务器（Light xyL Setup Server）。

<a id="ga29e1a90f166d88b6773d9b7ccf08e1c7"></a>

### `BT_MESH_MODEL_ID_LIGHT_XYL_SRV`

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SRV 0x130c
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯光色度与亮度服务器（Light xyL Server）。

<a id="gadd36546fb2cb6d1c731f7ae7674af6a7"></a>

### `BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI`

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI 0x000d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

私有代理客户端（Private Proxy Client）。

<a id="gaddc0bd645180a57cb9cd36745b84f7a1"></a>

### `BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV`

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV 0x000c
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

私有代理服务器（Private Proxy Server）。

<a id="gabac62a77e7d2d7677af21c33c8629187"></a>

### `BT_MESH_MODEL_ID_OP_AGG_CLI`

```c
#define BT_MESH_MODEL_ID_OP_AGG_CLI 0x0011
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

操作码聚合器客户端（Opcodes Aggregator Client）。

<a id="ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a"></a>

### `BT_MESH_MODEL_ID_OP_AGG_SRV`

```c
#define BT_MESH_MODEL_ID_OP_AGG_SRV 0x0010
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

操作码聚合器服务器（Opcodes Aggregator Server）。

<a id="gab3b21cbee4e11319a6e0ba3b02b24a91"></a>

### `BT_MESH_MODEL_ID_PRIV_BEACON_CLI`

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_CLI 0x000b
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

私有信标客户端（Private Beacon Client）。

<a id="gacca0e355982935cfbde46a06b09a7bec"></a>

### `BT_MESH_MODEL_ID_PRIV_BEACON_SRV`

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_SRV 0x000a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

私有信标服务器（Private Beacon Server）。

<a id="gaf373eb4d8af5d6bee76a821bd4d5e48c"></a>

### `BT_MESH_MODEL_ID_REMOTE_PROV_CLI`

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_CLI 0x0005
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

远程配网客户端（Remote Provisioning Client）。

<a id="ga9c7d1c5dfb87a5ce50c08747af47414f"></a>

### `BT_MESH_MODEL_ID_REMOTE_PROV_SRV`

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_SRV 0x0004
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

远程配网服务器（Remote Provisioning Server）。

<a id="gaf214eb7eef3530919432b62ff9b353c3"></a>

### `BT_MESH_MODEL_ID_SAR_CFG_CLI`

```c
#define BT_MESH_MODEL_ID_SAR_CFG_CLI 0x000f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

分段与重组配置客户端（SAR Configuration Client）。

<a id="ga1e9d8be1d2e65d2977aea0306b015258"></a>

### `BT_MESH_MODEL_ID_SAR_CFG_SRV`

```c
#define BT_MESH_MODEL_ID_SAR_CFG_SRV 0x000e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

分段与重组配置服务器（SAR Configuration Server）。

<a id="gad60472aa004a8a913aeb63ef62c45857"></a>

### `BT_MESH_MODEL_ID_SCENE_CLI`

```c
#define BT_MESH_MODEL_ID_SCENE_CLI 0x1205
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

场景客户端（Scene Client）。

<a id="gaa3b08fc8788684abb960fa3516726264"></a>

### `BT_MESH_MODEL_ID_SCENE_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_SCENE_SETUP_SRV 0x1204
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

场景设置服务器（Scene Setup Server）。

<a id="gaaa5554e3d48ae101596476e6bd6caf67"></a>

### `BT_MESH_MODEL_ID_SCENE_SRV`

```c
#define BT_MESH_MODEL_ID_SCENE_SRV 0x1203
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

场景服务器（Scene Server）。

<a id="gac743b26cf7e746b16302c25e8cd56221"></a>

### `BT_MESH_MODEL_ID_SCHEDULER_CLI`

```c
#define BT_MESH_MODEL_ID_SCHEDULER_CLI 0x1208
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

调度器客户端（Scheduler Client）。

<a id="ga3dbec5a3b82cb25a142c4bc851e3fe0e"></a>

### `BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV 0x1207
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

调度器设置服务器（Scheduler Setup Server）。

<a id="ga82b723752e240f22b9bcc8dc3dd10eb9"></a>

### `BT_MESH_MODEL_ID_SCHEDULER_SRV`

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SRV 0x1206
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

调度器服务器（Scheduler Server）。

<a id="ga8f1e4ff66d388627dbe91b2f8d4ed358"></a>

### `BT_MESH_MODEL_ID_SENSOR_CLI`

```c
#define BT_MESH_MODEL_ID_SENSOR_CLI 0x1102
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

传感器客户端（Sensor Client）。

<a id="gad10780bfc1c16866fa28de750e56bec3"></a>

### `BT_MESH_MODEL_ID_SENSOR_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_SENSOR_SETUP_SRV 0x1101
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

传感器设置服务器（Sensor Setup Server）。

<a id="ga3e0dcb14f46f6076e5b1b114b977f630"></a>

### `BT_MESH_MODEL_ID_SENSOR_SRV`

```c
#define BT_MESH_MODEL_ID_SENSOR_SRV 0x1100
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

传感器服务器（Sensor Server）。

<a id="ga6e747dd364bcfaa368e37c5f01afd530"></a>

### `BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI`

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI 0x0015
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

请求PDU重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）。

<a id="ga165bc198dadaa0d534ec82eb8192ebc0"></a>

### `BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV`

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV 0x0014
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

请求PDU重放保护列表配置服务器（Solicitation PDU RPL Configuration Server）。

<a id="ga500df90af7989794c5d72e760e5e65c6"></a>

### `BT_MESH_MODEL_ID_TIME_CLI`

```c
#define BT_MESH_MODEL_ID_TIME_CLI 0x1202
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

时间客户端（Time Client）。

<a id="ga2725121dc8c2c21c0ee469fe4348f45f"></a>

### `BT_MESH_MODEL_ID_TIME_SETUP_SRV`

```c
#define BT_MESH_MODEL_ID_TIME_SETUP_SRV 0x1201
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

时间设置服务器（Time Setup Server）。

<a id="ga93fbf1c661a75d70fdbd2a599353eb94"></a>

### `BT_MESH_MODEL_ID_TIME_SRV`

```c
#define BT_MESH_MODEL_ID_TIME_SRV 0x1200
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

时间服务器（Time Server）。


## 1.6\_原页交叉引用（Cross References）

- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_通用音频配置文件（Common Audio Profile，CAP）.md)
