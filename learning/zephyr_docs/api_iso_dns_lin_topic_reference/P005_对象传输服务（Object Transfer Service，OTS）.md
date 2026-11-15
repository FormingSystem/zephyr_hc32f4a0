---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-5
title: 对象传输服务（Object Transfer Service，OTS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_对象传输服务（Object Transfer Service，OTS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（Object Transfer Service，OTS）

<a id="details"></a>

对象传输服务（Object Transfer Service，OTS）。自 2.4 引入，版本 0.1.0。[实验性（Experimental）] 使用者应注意，API 可能随持续开发而变化。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fots_5Fobj_5Ftype"></a>

```c
struct bt_ots_obj_type
```

相关声明：[bt_ots_obj_type](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md)。

对象传输服务（OTS）对象的类型。

<a id="r_bt_5Fots_5Fobj_5Fsize"></a>

```c
struct bt_ots_obj_size
```

相关声明：[bt_ots_obj_size](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md)。

对象传输服务（OTS）对象大小（Object Size）参数的描述符。

<a id="r_bt_5Fots_5Ffeat"></a>

```c
struct bt_ots_feat
```

相关声明：[bt_ots_feat](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md)。

对象传输服务（OTS）的特性。

<a id="r_bt_5Fots_5Fdate_5Ftime"></a>

```c
struct bt_ots_date_time
```

相关声明：[bt_ots_date_time](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md)。

日期与时间（Date and Time）结构。

<a id="r_bt_5Fots_5Fobj_5Fmetadata"></a>

```c
struct bt_ots_obj_metadata
```

相关声明：[bt_ots_obj_metadata](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md)。

对象传输服务（OTS）对象的元数据。

<a id="r_bt_5Fots_5Fobj_5Fadd_5Fparam"></a>

```c
struct bt_ots_obj_add_param
```

相关声明：[bt_ots_obj_add_param](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md)。

对象传输服务（OTS）添加对象的描述符。

<a id="r_bt_5Fots_5Fobj_5Fcreated_5Fdesc"></a>

```c
struct bt_ots_obj_created_desc
```

相关声明：[bt_ots_obj_created_desc](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md)。

对象传输服务（OTS）已创建对象的描述符。

<a id="r_bt_5Fots_5Fcb"></a>

```c
struct bt_ots_cb
```

相关声明：[bt_ots_cb](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md)。

对象传输服务（OTS）的回调结构。

<a id="r_bt_5Fots_5Finit_5Fparam"></a>

```c
struct bt_ots_init_param
```

相关声明：[bt_ots_init_param](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md)。

对象传输服务（OTS）初始化的描述符。

<a id="r_bt_5Fots_5Fclient"></a>

```c
struct bt_ots_client
```

相关声明：[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)。

对象传输服务（OTS）的客户端实例。

<a id="r_bt_5Fots_5Fclient_5Fcb"></a>

```c
struct bt_ots_client_cb
```

相关声明：[bt_ots_client_cb](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md)。

对象传输服务（OTS）的客户端回调结构。

<a id="r_bt_5Fots"></a>

```c
struct bt_ots
```

相关声明：[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)。

不透明的对象传输服务（OTS）实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_gad5e4a66f017facc2a185ee0a55a0c3ee"></a>

```c
#define BT_OTS_OBJ_ID_SIZE 6
```

相关声明：[BT_OTS_OBJ_ID_SIZE](#gad5e4a66f017facc2a185ee0a55a0c3ee)。

对象传输服务对象标识符（OTS Object ID）的大小，单位为字节。

<a id="r_ga79110fa56a524754d74bf20ac6a766aa"></a>

```c
#define BT_OTS_OBJ_ID_MIN 0x000000000100ULL
```

相关声明：[BT_OTS_OBJ_ID_MIN](#ga79110fa56a524754d74bf20ac6a766aa)。

对象 ID 的最小允许值，目录列表（Directory Listing）ID 除外。

<a id="r_gabd777e7a1b7adaaacfec3e084c3a9bfe"></a>

```c
#define BT_OTS_OBJ_ID_MAX 0xFFFFFFFFFFFFULL
```

相关声明：[BT_OTS_OBJ_ID_MAX](#gabd777e7a1b7adaaacfec3e084c3a9bfe)。

对象 ID 的最大允许值，目录列表（Directory Listing）ID 除外。

<a id="r_ga4a6a0b0a3c8d10f3668e61c9dee0e05e"></a>

```c
#define OTS_OBJ_ID_DIR_LIST 0x000000000000ULL
```

相关声明：[OTS_OBJ_ID_DIR_LIST](#ga4a6a0b0a3c8d10f3668e61c9dee0e05e)。

目录列表对象（Directory Listing Object）的 ID。

<a id="r_gabe3d54a6dfa0d52a97826c140c603d78"></a>

```c
#define BT_OTS_OBJ_ID_MASK BIT64_MASK(48)
```

相关声明：[BT_OTS_OBJ_ID_MASK](#gabe3d54a6dfa0d52a97826c140c603d78)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

对象传输服务对象标识符（OTS Object ID）的掩码，保留其中的 48 位。

<a id="r_ga2754eeb7418ed762a3119fc56871d37e"></a>

```c
#define BT_OTS_OBJ_ID_STR_LEN 15
```

相关声明：[BT_OTS_OBJ_ID_STR_LEN](#ga2754eeb7418ed762a3119fc56871d37e)。

对象传输服务对象标识符字符串（OTS Object ID String）的长度，单位为字节。

<a id="r_ga6ad37ee172d6518e7316b4e0ec8f27c7"></a>

```c
#define BT_OTS_OBJ_SET_PROP_DELETE(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_DELETE](#ga6ad37ee172d6518e7316b4e0ec8f27c7)。

设置 `BT_OTS_OBJ_PROP_DELETE` 属性（Property）。

<a id="r_ga2342f00ef480b279d737bcddc8e2faf0"></a>

```c
#define BT_OTS_OBJ_SET_PROP_EXECUTE(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_EXECUTE](#ga2342f00ef480b279d737bcddc8e2faf0)。

设置 `BT_OTS_OBJ_PROP_EXECUTE` 属性（Property）。

<a id="r_gaba26016beff74b1b6ec75ba083cf808d"></a>

```c
#define BT_OTS_OBJ_SET_PROP_READ(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_READ](#gaba26016beff74b1b6ec75ba083cf808d)。

设置 `BT_OTS_OBJ_PROP_READ` 属性（Property）。

<a id="r_gaeb1a5a907478fd668199a27e20fc2173"></a>

```c
#define BT_OTS_OBJ_SET_PROP_WRITE(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_WRITE](#gaeb1a5a907478fd668199a27e20fc2173)。

设置 `BT_OTS_OBJ_PROP_WRITE` 属性（Property）。

<a id="r_gaa1eff1b4ee05fb91d87dcb85dd7469e1"></a>

```c
#define BT_OTS_OBJ_SET_PROP_APPEND(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_APPEND](#gaa1eff1b4ee05fb91d87dcb85dd7469e1)。

设置 `BT_OTS_OBJ_PROP_APPEND` 属性（Property）。

<a id="r_ga8f99514414958d031a4e9985c8cc976b"></a>

```c
#define BT_OTS_OBJ_SET_PROP_TRUNCATE(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_TRUNCATE](#ga8f99514414958d031a4e9985c8cc976b)。

设置 `BT_OTS_OBJ_PROP_TRUNCATE` 属性（Property）。

<a id="r_gac36c68dfeb21bf705f87f11e847c5aed"></a>

```c
#define BT_OTS_OBJ_SET_PROP_PATCH(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_PATCH](#gac36c68dfeb21bf705f87f11e847c5aed)。

设置 `BT_OTS_OBJ_PROP_PATCH` 属性（Property）。

<a id="r_gae21e599a85549d5cd4462c0f36c291ac"></a>

```c
#define BT_OTS_OBJ_SET_PROP_MARKED(prop)
```

相关声明：[BT_OTS_OBJ_SET_PROP_MARKED](#gae21e599a85549d5cd4462c0f36c291ac)。

设置 `BT_OTS_OBJ_PROP_MARKED` 属性（Property）。

<a id="r_ga7a735cf89c9986624e34b183282a65ee"></a>

```c
#define BT_OTS_OBJ_GET_PROP_DELETE(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_DELETE](#ga7a735cf89c9986624e34b183282a65ee)。

获取 `BT_OTS_OBJ_PROP_DELETE` 属性（Property）。

<a id="r_ga90619bdcf5ec9a942f7d81f6c87465fc"></a>

```c
#define BT_OTS_OBJ_GET_PROP_EXECUTE(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_EXECUTE](#ga90619bdcf5ec9a942f7d81f6c87465fc)。

获取 `BT_OTS_OBJ_PROP_EXECUTE` 属性（Property）。

<a id="r_gae846afdc9f6c40b2bf6d2ae67deb8eef"></a>

```c
#define BT_OTS_OBJ_GET_PROP_READ(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_READ](#gae846afdc9f6c40b2bf6d2ae67deb8eef)。

获取 `BT_OTS_OBJ_PROP_READ` 属性（Property）。

<a id="r_ga9769628cbe2c81161607c6518d3d4798"></a>

```c
#define BT_OTS_OBJ_GET_PROP_WRITE(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_WRITE](#ga9769628cbe2c81161607c6518d3d4798)。

获取 `BT_OTS_OBJ_PROP_WRITE` 属性（Property）。

<a id="r_gaccbf81f9a9ebcc70801739a4a8fafcd8"></a>

```c
#define BT_OTS_OBJ_GET_PROP_APPEND(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_APPEND](#gaccbf81f9a9ebcc70801739a4a8fafcd8)。

获取 `BT_OTS_OBJ_PROP_APPEND` 属性（Property）。

<a id="r_gac7b6632aac554db5b4d5b9f3e8bf78b4"></a>

```c
#define BT_OTS_OBJ_GET_PROP_TRUNCATE(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_TRUNCATE](#gac7b6632aac554db5b4d5b9f3e8bf78b4)。

获取 `BT_OTS_OBJ_PROP_TRUNCATE` 属性（Property）。

<a id="r_ga6c8ccb5f8919f062b1b44e1b4981907d"></a>

```c
#define BT_OTS_OBJ_GET_PROP_PATCH(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_PATCH](#ga6c8ccb5f8919f062b1b44e1b4981907d)。

获取 `BT_OTS_OBJ_PROP_PATCH` 属性（Property）。

<a id="r_gaeffab993f4fbe15090a7a626cd56f034"></a>

```c
#define BT_OTS_OBJ_GET_PROP_MARKED(prop)
```

相关声明：[BT_OTS_OBJ_GET_PROP_MARKED](#gaeffab993f4fbe15090a7a626cd56f034)。

获取 `BT_OTS_OBJ_PROP_MARKED` 属性（Property）。

<a id="r_ga8cc851f268de24fe3445a9a0c3af6abf"></a>

```c
#define BT_OTS_OACP_SET_FEAT_CREATE(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_CREATE](#ga8cc851f268de24fe3445a9a0c3af6abf)。

设置 `BT_OTS_OACP_FEAT_CREATE` 特性（Feature）。

<a id="r_ga9306e9a2b8ea468f28eb73b7d412032e"></a>

```c
#define BT_OTS_OACP_SET_FEAT_DELETE(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_DELETE](#ga9306e9a2b8ea468f28eb73b7d412032e)。

设置 `BT_OTS_OACP_FEAT_DELETE` 特性（Feature）。

<a id="r_gaba4d7e446212dc6c2139c324d22edc10"></a>

```c
#define BT_OTS_OACP_SET_FEAT_CHECKSUM(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_CHECKSUM](#gaba4d7e446212dc6c2139c324d22edc10)。

设置 `BT_OTS_OACP_FEAT_CHECKSUM` 特性（Feature）。

<a id="r_ga4b19d199947053e7b2f93b64ea83c29a"></a>

```c
#define BT_OTS_OACP_SET_FEAT_EXECUTE(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_EXECUTE](#ga4b19d199947053e7b2f93b64ea83c29a)。

设置 `BT_OTS_OACP_FEAT_EXECUTE` 特性（Feature）。

<a id="r_ga5508cf6698e2927333f31cb0cffce831"></a>

```c
#define BT_OTS_OACP_SET_FEAT_READ(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_READ](#ga5508cf6698e2927333f31cb0cffce831)。

设置 `BT_OTS_OACP_FEAT_READ` 特性（Feature）。

<a id="r_gac035cb71a2caabd16bb64d27b56e32c7"></a>

```c
#define BT_OTS_OACP_SET_FEAT_WRITE(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_WRITE](#gac035cb71a2caabd16bb64d27b56e32c7)。

设置 `BT_OTS_OACP_FEAT_WRITE` 特性（Feature）。

<a id="r_gaabae304227bed27796ad2a346963fa86"></a>

```c
#define BT_OTS_OACP_SET_FEAT_APPEND(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_APPEND](#gaabae304227bed27796ad2a346963fa86)。

设置 `BT_OTS_OACP_FEAT_APPEND` 特性（Feature）。

<a id="r_gae5f0e14f685d40782952345ebe50eb3d"></a>

```c
#define BT_OTS_OACP_SET_FEAT_TRUNCATE(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_TRUNCATE](#gae5f0e14f685d40782952345ebe50eb3d)。

设置 `BT_OTS_OACP_FEAT_TRUNCATE` 特性（Feature）。

<a id="r_gabca8354bc176bd819005ca213a148b87"></a>

```c
#define BT_OTS_OACP_SET_FEAT_PATCH(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_PATCH](#gabca8354bc176bd819005ca213a148b87)。

设置 `BT_OTS_OACP_FEAT_PATCH` 特性（Feature）。

<a id="r_ga3bb8eb9f732947daf289dfe40e171248"></a>

```c
#define BT_OTS_OACP_SET_FEAT_ABORT(feat)
```

相关声明：[BT_OTS_OACP_SET_FEAT_ABORT](#ga3bb8eb9f732947daf289dfe40e171248)。

设置 `BT_OTS_OACP_FEAT_ABORT` 特性（Feature）。

<a id="r_ga058d8d1fb255ca66057c1edfc547def4"></a>

```c
#define BT_OTS_OACP_GET_FEAT_CREATE(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_CREATE](#ga058d8d1fb255ca66057c1edfc547def4)。

获取 `BT_OTS_OACP_FEAT_CREATE` 特性（Feature）。

<a id="r_ga815632fc160921a074bec60250df47f2"></a>

```c
#define BT_OTS_OACP_GET_FEAT_DELETE(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_DELETE](#ga815632fc160921a074bec60250df47f2)。

获取 `BT_OTS_OACP_FEAT_DELETE` 特性（Feature）。

<a id="r_gabbc141c9a7d5614971b87b727cbf01af"></a>

```c
#define BT_OTS_OACP_GET_FEAT_CHECKSUM(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_CHECKSUM](#gabbc141c9a7d5614971b87b727cbf01af)。

获取 `BT_OTS_OACP_FEAT_CHECKSUM` 特性（Feature）。

<a id="r_ga2ac0d82e8fab9fa22b5dc3396c8641ad"></a>

```c
#define BT_OTS_OACP_GET_FEAT_EXECUTE(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_EXECUTE](#ga2ac0d82e8fab9fa22b5dc3396c8641ad)。

获取 `BT_OTS_OACP_FEAT_EXECUTE` 特性（Feature）。

<a id="r_gac53739b9fd65124f601e92b29b9123cd"></a>

```c
#define BT_OTS_OACP_GET_FEAT_READ(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_READ](#gac53739b9fd65124f601e92b29b9123cd)。

获取 `BT_OTS_OACP_FEAT_READ` 特性（Feature）。

<a id="r_ga390d957c514b2f182ff3d1d0c2221822"></a>

```c
#define BT_OTS_OACP_GET_FEAT_WRITE(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_WRITE](#ga390d957c514b2f182ff3d1d0c2221822)。

获取 `BT_OTS_OACP_FEAT_WRITE` 特性（Feature）。

<a id="r_ga36f5cc04fce18390bf1cde3e0e8a6184"></a>

```c
#define BT_OTS_OACP_GET_FEAT_APPEND(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_APPEND](#ga36f5cc04fce18390bf1cde3e0e8a6184)。

获取 `BT_OTS_OACP_FEAT_APPEND` 特性（Feature）。

<a id="r_ga9ca79d43292354f1558943f944dd53a7"></a>

```c
#define BT_OTS_OACP_GET_FEAT_TRUNCATE(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_TRUNCATE](#ga9ca79d43292354f1558943f944dd53a7)。

获取 `BT_OTS_OACP_FEAT_TRUNCATE` 特性（Feature）。

<a id="r_gaca6591a0c7e8650fa827a7a43fcca81e"></a>

```c
#define BT_OTS_OACP_GET_FEAT_PATCH(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_PATCH](#gaca6591a0c7e8650fa827a7a43fcca81e)。

获取 `BT_OTS_OACP_FEAT_PATCH` 特性（Feature）。

<a id="r_ga196a2aceeecd620baacf0727e1427341"></a>

```c
#define BT_OTS_OACP_GET_FEAT_ABORT(feat)
```

相关声明：[BT_OTS_OACP_GET_FEAT_ABORT](#ga196a2aceeecd620baacf0727e1427341)。

获取 `BT_OTS_OACP_FEAT_ABORT` 特性（Feature）。

<a id="r_gafe219709f2bd318af66cad4e118df658"></a>

```c
#define BT_OTS_OLCP_SET_FEAT_GO_TO(feat)
```

相关声明：[BT_OTS_OLCP_SET_FEAT_GO_TO](#gafe219709f2bd318af66cad4e118df658)。

设置 `BT_OTS_OLCP_FEAT_GO_TO` 特性（Feature）。

<a id="r_ga1248c694ff2d9ded862f37d03d98e2f0"></a>

```c
#define BT_OTS_OLCP_SET_FEAT_ORDER(feat)
```

相关声明：[BT_OTS_OLCP_SET_FEAT_ORDER](#ga1248c694ff2d9ded862f37d03d98e2f0)。

设置 `BT_OTS_OLCP_FEAT_ORDER` 特性（Feature）。

<a id="r_ga1cee6e1affdff27aa0ba6a655c9bf09c"></a>

```c
#define BT_OTS_OLCP_SET_FEAT_NUM_REQ(feat)
```

相关声明：[BT_OTS_OLCP_SET_FEAT_NUM_REQ](#ga1cee6e1affdff27aa0ba6a655c9bf09c)。

设置 `BT_OTS_OLCP_FEAT_NUM_REQ` 特性（Feature）。

<a id="r_ga7a3f8d3b725c8c31d5e3062d46db4438"></a>

```c
#define BT_OTS_OLCP_SET_FEAT_CLEAR(feat)
```

相关声明：[BT_OTS_OLCP_SET_FEAT_CLEAR](#ga7a3f8d3b725c8c31d5e3062d46db4438)。

设置 `BT_OTS_OLCP_FEAT_CLEAR` 特性（Feature）。

<a id="r_ga7ec49843849613ee3f8f72209cae68c2"></a>

```c
#define BT_OTS_OLCP_GET_FEAT_GO_TO(feat)
```

相关声明：[BT_OTS_OLCP_GET_FEAT_GO_TO](#ga7ec49843849613ee3f8f72209cae68c2)。

获取 `BT_OTS_OLCP_GET_FEAT_GO_TO` 特性（Feature）。

<a id="r_gad4393e56c94c2484cd344b48cb54b255"></a>

```c
#define BT_OTS_OLCP_GET_FEAT_ORDER(feat)
```

相关声明：[BT_OTS_OLCP_GET_FEAT_ORDER](#gad4393e56c94c2484cd344b48cb54b255)。

获取 `BT_OTS_OLCP_GET_FEAT_ORDER` 特性（Feature）。

<a id="r_ga2a1a62e410586b1117fd3571e42363d8"></a>

```c
#define BT_OTS_OLCP_GET_FEAT_NUM_REQ(feat)
```

相关声明：[BT_OTS_OLCP_GET_FEAT_NUM_REQ](#ga2a1a62e410586b1117fd3571e42363d8)。

获取 `BT_OTS_OLCP_GET_FEAT_NUM_REQ` 特性（Feature）。

<a id="r_ga0f57d172615d1c6ea857506dc0c10e55"></a>

```c
#define BT_OTS_OLCP_GET_FEAT_CLEAR(feat)
```

相关声明：[BT_OTS_OLCP_GET_FEAT_CLEAR](#ga0f57d172615d1c6ea857506dc0c10e55)。

获取 `BT_OTS_OLCP_GET_FEAT_CLEAR` 特性（Feature）。

<a id="r_ga56cd1131414fa19e3ec30e2a1a241689"></a>

```c
#define BT_OTS_DATE_TIME_FIELD_SIZE 7
```

相关声明：[BT_OTS_DATE_TIME_FIELD_SIZE](#ga56cd1131414fa19e3ec30e2a1a241689)。

<a id="r_ga4f18ea10855379414dd8a70b6c119d6b"></a>

```c
#define BT_OTS_STOP 0
```

相关声明：[BT_OTS_STOP](#ga4f18ea10855379414dd8a70b6c119d6b)。

<a id="r_ga8ccd0dec55069aa01bb9740a6520fd51"></a>

```c
#define BT_OTS_CONTINUE 1
```

相关声明：[BT_OTS_CONTINUE](#ga8ccd0dec55069aa01bb9740a6520fd51)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gaa1a9db6e8aa6ee716e4fdd2e34157f46"></a>

```c
typedef int(* bt_ots_client_dirlisting_cb) (struct bt_ots_obj_metadata *meta)
```

相关声明：[bt_ots_client_dirlisting_cb](#gaa1a9db6e8aa6ee716e4fdd2e34157f46)、[bt_ots_obj_metadata](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md)。

目录列表对象元数据回调（Directory Listing Object Metadata Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_gaea054a2be05dca63c0cd0375649af26b"></a>

```c
enum { BT_OTS_OBJ_PROP_DELETE = 0 , BT_OTS_OBJ_PROP_EXECUTE = 1 , BT_OTS_OBJ_PROP_READ = 2 , BT_OTS_OBJ_PROP_WRITE = 3 , BT_OTS_OBJ_PROP_APPEND = 4 , BT_OTS_OBJ_PROP_TRUNCATE = 5 , BT_OTS_OBJ_PROP_PATCH = 6 , BT_OTS_OBJ_PROP_MARKED = 7 }
```

相关声明：[BT_OTS_OBJ_PROP_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10)、[BT_OTS_OBJ_PROP_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad)、[BT_OTS_OBJ_PROP_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102)、[BT_OTS_OBJ_PROP_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2)、[BT_OTS_OBJ_PROP_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775)、[BT_OTS_OBJ_PROP_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446)、[BT_OTS_OBJ_PROP_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed)、[BT_OTS_OBJ_PROP_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3)。

对象传输服务对象的属性（OTS Object Properties）。

<a id="r_ga141f5762339600942eb229bfdc183ebb"></a>

```c
enum { BT_OTS_OACP_FEAT_CREATE = 0 , BT_OTS_OACP_FEAT_DELETE = 1 , BT_OTS_OACP_FEAT_CHECKSUM = 2 , BT_OTS_OACP_FEAT_EXECUTE = 3 , BT_OTS_OACP_FEAT_READ = 4 , BT_OTS_OACP_FEAT_WRITE = 5 , BT_OTS_OACP_FEAT_APPEND = 6 , BT_OTS_OACP_FEAT_TRUNCATE = 7 , BT_OTS_OACP_FEAT_PATCH = 8 , BT_OTS_OACP_FEAT_ABORT = 9 }
```

相关声明：[BT_OTS_OACP_FEAT_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9)、[BT_OTS_OACP_FEAT_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee)、[BT_OTS_OACP_FEAT_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f)、[BT_OTS_OACP_FEAT_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c)、[BT_OTS_OACP_FEAT_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465)、[BT_OTS_OACP_FEAT_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab)、[BT_OTS_OACP_FEAT_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b)、[BT_OTS_OACP_FEAT_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225)、[BT_OTS_OACP_FEAT_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf)、[BT_OTS_OACP_FEAT_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440)。

对象动作控制点特性位（Object Action Control Point Feature Bits）。

<a id="r_gaebdd2b8a80948d1050d42fa3963cc863"></a>

```c
enum bt_ots_oacp_write_op_mode { BT_OTS_OACP_WRITE_OP_MODE_NONE = 0 , BT_OTS_OACP_WRITE_OP_MODE_TRUNCATE = BIT(1) }
```

相关声明：[bt_ots_oacp_write_op_mode](#gaebdd2b8a80948d1050d42fa3963cc863)、[BT_OTS_OACP_WRITE_OP_MODE_NONE](#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab)、[BT_OTS_OACP_WRITE_OP_MODE_TRUNCATE](#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a)。

<a id="r_ga39716a5c8e5097ad2ddeaf8db407024e"></a>

```c
enum { BT_OTS_OLCP_FEAT_GO_TO = 0 , BT_OTS_OLCP_FEAT_ORDER = 1 , BT_OTS_OLCP_FEAT_NUM_REQ = 2 , BT_OTS_OLCP_FEAT_CLEAR = 3 }
```

相关声明：[BT_OTS_OLCP_FEAT_GO_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713)、[BT_OTS_OLCP_FEAT_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d)、[BT_OTS_OLCP_FEAT_NUM_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660)、[BT_OTS_OLCP_FEAT_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af)。

对象列表控制点特性位（Object List Control Point Feature Bits）。

<a id="r_ga9bbade1b48363f0f486968723afefb45"></a>

```c
enum { BT_OTS_METADATA_REQ_NAME = BIT(0) , BT_OTS_METADATA_REQ_TYPE = BIT(1) , BT_OTS_METADATA_REQ_SIZE = BIT(2) , BT_OTS_METADATA_REQ_CREATED = BIT(3) , BT_OTS_METADATA_REQ_MODIFIED = BIT(4) , BT_OTS_METADATA_REQ_ID = BIT(5) , BT_OTS_METADATA_REQ_PROPS = BIT(6) , BT_OTS_METADATA_REQ_ALL = 0x7F }
```

相关声明：[BT_OTS_METADATA_REQ_NAME](#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb)、[BT_OTS_METADATA_REQ_TYPE](#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9)、[BT_OTS_METADATA_REQ_SIZE](#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5)、[BT_OTS_METADATA_REQ_CREATED](#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095)、[BT_OTS_METADATA_REQ_MODIFIED](#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e)、[BT_OTS_METADATA_REQ_ID](#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2)、[BT_OTS_METADATA_REQ_PROPS](#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f)、[BT_OTS_METADATA_REQ_ALL](#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf)。

对象元数据请求位字段值（Object Metadata Request Bit Field Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_gabf59844edd0ffd434acd94bad9a7b52c"></a>

```c
int bt_ots_obj_add (struct bt_ots *ots, const struct bt_ots_obj_add_param *param)
```

相关声明：[bt_ots_obj_add](#gabf59844edd0ffd434acd94bad9a7b52c)、[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[bt_ots_obj_add_param](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md)。

向对象传输服务（OTS）实例添加对象。

<a id="r_ga872ba5a73fa4e617b9d48e7361af74c7"></a>

```c
int bt_ots_obj_delete (struct bt_ots *ots, uint64_t id)
```

相关声明：[bt_ots_obj_delete](#ga872ba5a73fa4e617b9d48e7361af74c7)、[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从对象传输服务（OTS）实例删除对象。

<a id="r_gabe637ba9febb514f7346d71696b70c73"></a>

```c
void * bt_ots_svc_decl_get (struct bt_ots *ots)
```

相关声明：[bt_ots_svc_decl_get](#gabe637ba9febb514f7346d71696b70c73)、[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_ga1c9dcb35c8f07432fd9249a34e597819"></a>

```c
int bt_ots_init (struct bt_ots *ots, struct bt_ots_init_param *ots_init)
```

相关声明：[bt_ots_init](#ga1c9dcb35c8f07432fd9249a34e597819)、[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[bt_ots_init_param](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md)。

初始化对象传输服务（OTS）实例。

<a id="r_gafc71de8fd65212045fa26b2a81e3876d"></a>

```c
struct bt_ots * bt_ots_free_instance_get (void)
```

相关声明：[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[bt_ots_free_instance_get](#gafc71de8fd65212045fa26b2a81e3876d)。

从池中获取空闲的对象传输服务（OTS）实例。

<a id="r_gadefd2ccb46a686a4aa2999da5851184b"></a>

```c
int bt_ots_client_register (struct bt_ots_client *ots_inst)
```

相关声明：[bt_ots_client_register](#gadefd2ccb46a686a4aa2999da5851184b)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)。

注册对象传输服务实例（Object Transfer Service Instance）。

<a id="r_gabba031c38c7503c1f434a761d9f65df4"></a>

```c
int bt_ots_client_unregister (uint8_t index)
```

相关声明：[bt_ots_client_unregister](#gabba031c38c7503c1f434a761d9f65df4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销对象传输服务实例（Object Transfer Service Instance）。

<a id="r_gac270137f15596777287f68b3d6a6a11c"></a>

```c
uint8_t bt_ots_client_indicate_handler (struct bt_conn *conn, struct bt_gatt_subscribe_params *params, const void *data, uint16_t length)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_ots_client_indicate_handler](#gac270137f15596777287f68b3d6a6a11c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

对象传输服务指示处理函数（OTS Indicate Handler）。

<a id="r_gaf11589afc37efe18dcac122835a4c95d"></a>

```c
int bt_ots_client_read_feature (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_read_feature](#gaf11589afc37efe18dcac122835a4c95d)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取对象传输服务特性特征（OTS Feature Characteristic）。

<a id="r_ga5f2d0b0e4d54e00a1a96157fcfaf172b"></a>

```c
int bt_ots_client_select_id (struct bt_ots_client *otc_inst, struct bt_conn *conn, uint64_t obj_id)
```

相关声明：[bt_ots_client_select_id](#ga5f2d0b0e4d54e00a1a96157fcfaf172b)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

按对象标识符（Object ID）选择对象。

<a id="r_ga70cae251cf40a5c3c8d2a8c7e1f1e181"></a>

```c
int bt_ots_client_select_first (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_select_first](#ga70cae251cf40a5c3c8d2a8c7e1f1e181)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

选择第一个对象（First Object）。

<a id="r_ga89fc03d68725de0b5f306c899452b1a8"></a>

```c
int bt_ots_client_select_last (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_select_last](#ga89fc03d68725de0b5f306c899452b1a8)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

选择最后一个对象（Last Object）。

<a id="r_ga81997ab2f1718c6856e676eb9b3f72bb"></a>

```c
int bt_ots_client_select_next (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_select_next](#ga81997ab2f1718c6856e676eb9b3f72bb)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

选择下一个对象（Next Object）。

<a id="r_gac84ed7f16fa86d87531d04e2957568f9"></a>

```c
int bt_ots_client_select_prev (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_select_prev](#gac84ed7f16fa86d87531d04e2957568f9)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

选择上一个对象（Previous Object）。

<a id="r_ga936f392c880c9d1a73f2bd632e5b63e0"></a>

```c
int bt_ots_client_read_object_metadata (struct bt_ots_client *otc_inst, struct bt_conn *conn, uint8_t metadata)
```

相关声明：[bt_ots_client_read_object_metadata](#ga936f392c880c9d1a73f2bd632e5b63e0)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取当前对象的元数据（Metadata）。

<a id="r_ga8ad1c53325c1b77271307507317a5965"></a>

```c
int bt_ots_client_read_object_data (struct bt_ots_client *otc_inst, struct bt_conn *conn)
```

相关声明：[bt_ots_client_read_object_data](#ga8ad1c53325c1b77271307507317a5965)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前选定对象的数据。

<a id="r_ga9444b064c616718dae1577b21540fb9a"></a>

```c
int bt_ots_client_write_object_data (struct bt_ots_client *otc_inst, struct bt_conn *conn, const void *buf, size_t len, off_t offset, enum bt_ots_oacp_write_op_mode mode)
```

相关声明：[bt_ots_client_write_object_data](#ga9444b064c616718dae1577b21540fb9a)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[bt_ots_oacp_write_op_mode](#gaebdd2b8a80948d1050d42fa3963cc863)。

写入当前选定对象的数据。

<a id="r_ga9cfd057d39ce3fe9bbecaa103ec44f77"></a>

```c
int bt_ots_client_get_object_checksum (struct bt_ots_client *otc_inst, struct bt_conn *conn, off_t offset, size_t len)
```

相关声明：[bt_ots_client_get_object_checksum](#ga9cfd057d39ce3fe9bbecaa103ec44f77)、[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

获取当前选定对象的校验和（Checksum）。

<a id="r_gabe485816a2e536758a7ce85c593ea486"></a>

```c
int bt_ots_client_decode_dirlisting (uint8_t *data, uint16_t length, bt_ots_client_dirlisting_cb cb)
```

相关声明：[bt_ots_client_decode_dirlisting](#gabe485816a2e536758a7ce85c593ea486)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_ots_client_dirlisting_cb](#gaa1a9db6e8aa6ee716e4fdd2e34157f46)。

将目录列表对象（Directory Listing Object）解码为对象元数据（Object Metadata）。

<a id="r_gac9be2770fc7f2932ea2e31392d956f0a"></a>

```c
static int bt_ots_obj_id_to_str (uint64_t obj_id, char *str, size_t len)
```

相关声明：[bt_ots_obj_id_to_str](#gac9be2770fc7f2932ea2e31392d956f0a)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将二进制对象传输服务对象标识符（OTS Object ID）转换为字符串。

<a id="r_ga8324cc14e8812648cc3663144591af89"></a>

```c
void bt_ots_metadata_display (struct bt_ots_obj_metadata *metadata, uint16_t count)
```

相关声明：[bt_ots_metadata_display](#ga8324cc14e8812648cc3663144591af89)、[bt_ots_obj_metadata](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用 `LOG_INF` 将一个或多个对象的元数据（Metadata）显示为文本。

<a id="r_ga63e4408702fee1be0501a715cd32c957"></a>

```c
static uint32_t bt_ots_client_calc_checksum (const uint8_t *data, size_t len)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_ots_client_calc_checksum](#ga63e4408702fee1be0501a715cd32c957)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

生成符合 IEEE 标准的 CRC32 校验和（Checksum）。

## 5.6\_详细说明（Detailed Documentation）

<a id="ga8ccd0dec55069aa01bb9740a6520fd51"></a>

### `BT_OTS_CONTINUE`

```c
#define BT_OTS_CONTINUE 1
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="ga56cd1131414fa19e3ec30e2a1a241689"></a>

### `BT_OTS_DATE_TIME_FIELD_SIZE`

```c
#define BT_OTS_DATE_TIME_FIELD_SIZE 7
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="ga196a2aceeecd620baacf0727e1427341"></a>

### `BT_OTS_OACP_GET_FEAT_ABORT`

```c
#define BT_OTS_OACP_GET_FEAT_ABORT ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_ABORT))
```

获取 `BT_OTS_OACP_FEAT_ABORT` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga36f5cc04fce18390bf1cde3e0e8a6184"></a>

### `BT_OTS_OACP_GET_FEAT_APPEND`

```c
#define BT_OTS_OACP_GET_FEAT_APPEND ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_APPEND))
```

获取 `BT_OTS_OACP_FEAT_APPEND` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gabbc141c9a7d5614971b87b727cbf01af"></a>

### `BT_OTS_OACP_GET_FEAT_CHECKSUM`

```c
#define BT_OTS_OACP_GET_FEAT_CHECKSUM ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_CHECKSUM))
```

获取 `BT_OTS_OACP_FEAT_CHECKSUM` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga058d8d1fb255ca66057c1edfc547def4"></a>

### `BT_OTS_OACP_GET_FEAT_CREATE`

```c
#define BT_OTS_OACP_GET_FEAT_CREATE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_CREATE))
```

获取 `BT_OTS_OACP_FEAT_CREATE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga815632fc160921a074bec60250df47f2"></a>

### `BT_OTS_OACP_GET_FEAT_DELETE`

```c
#define BT_OTS_OACP_GET_FEAT_DELETE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_DELETE))
```

获取 `BT_OTS_OACP_FEAT_DELETE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga2ac0d82e8fab9fa22b5dc3396c8641ad"></a>

### `BT_OTS_OACP_GET_FEAT_EXECUTE`

```c
#define BT_OTS_OACP_GET_FEAT_EXECUTE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_EXECUTE))
```

获取 `BT_OTS_OACP_FEAT_EXECUTE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gaca6591a0c7e8650fa827a7a43fcca81e"></a>

### `BT_OTS_OACP_GET_FEAT_PATCH`

```c
#define BT_OTS_OACP_GET_FEAT_PATCH ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_PATCH))
```

获取 `BT_OTS_OACP_FEAT_PATCH` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gac53739b9fd65124f601e92b29b9123cd"></a>

### `BT_OTS_OACP_GET_FEAT_READ`

```c
#define BT_OTS_OACP_GET_FEAT_READ ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_READ))
```

获取 `BT_OTS_OACP_FEAT_READ` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga9ca79d43292354f1558943f944dd53a7"></a>

### `BT_OTS_OACP_GET_FEAT_TRUNCATE`

```c
#define BT_OTS_OACP_GET_FEAT_TRUNCATE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_TRUNCATE))
```

获取 `BT_OTS_OACP_FEAT_TRUNCATE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga390d957c514b2f182ff3d1d0c2221822"></a>

### `BT_OTS_OACP_GET_FEAT_WRITE`

```c
#define BT_OTS_OACP_GET_FEAT_WRITE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OACP_FEAT_WRITE))
```

获取 `BT_OTS_OACP_FEAT_WRITE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga3bb8eb9f732947daf289dfe40e171248"></a>

### `BT_OTS_OACP_SET_FEAT_ABORT`

```c
#define BT_OTS_OACP_SET_FEAT_ABORT ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_ABORT, 1)
```

设置 `BT_OTS_OACP_FEAT_ABORT` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gaabae304227bed27796ad2a346963fa86"></a>

### `BT_OTS_OACP_SET_FEAT_APPEND`

```c
#define BT_OTS_OACP_SET_FEAT_APPEND ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_APPEND, 1)
```

设置 `BT_OTS_OACP_FEAT_APPEND` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gaba4d7e446212dc6c2139c324d22edc10"></a>

### `BT_OTS_OACP_SET_FEAT_CHECKSUM`

```c
#define BT_OTS_OACP_SET_FEAT_CHECKSUM ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_CHECKSUM, 1)
```

设置 `BT_OTS_OACP_FEAT_CHECKSUM` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga8cc851f268de24fe3445a9a0c3af6abf"></a>

### `BT_OTS_OACP_SET_FEAT_CREATE`

```c
#define BT_OTS_OACP_SET_FEAT_CREATE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_CREATE, 1)
```

设置 `BT_OTS_OACP_FEAT_CREATE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga9306e9a2b8ea468f28eb73b7d412032e"></a>

### `BT_OTS_OACP_SET_FEAT_DELETE`

```c
#define BT_OTS_OACP_SET_FEAT_DELETE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_DELETE, 1)
```

设置 `BT_OTS_OACP_FEAT_DELETE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga4b19d199947053e7b2f93b64ea83c29a"></a>

### `BT_OTS_OACP_SET_FEAT_EXECUTE`

```c
#define BT_OTS_OACP_SET_FEAT_EXECUTE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_EXECUTE, 1)
```

设置 `BT_OTS_OACP_FEAT_EXECUTE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gabca8354bc176bd819005ca213a148b87"></a>

### `BT_OTS_OACP_SET_FEAT_PATCH`

```c
#define BT_OTS_OACP_SET_FEAT_PATCH ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_PATCH, 1)
```

设置 `BT_OTS_OACP_FEAT_PATCH` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga5508cf6698e2927333f31cb0cffce831"></a>

### `BT_OTS_OACP_SET_FEAT_READ`

```c
#define BT_OTS_OACP_SET_FEAT_READ ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_READ, 1)
```

设置 `BT_OTS_OACP_FEAT_READ` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gae5f0e14f685d40782952345ebe50eb3d"></a>

### `BT_OTS_OACP_SET_FEAT_TRUNCATE`

```c
#define BT_OTS_OACP_SET_FEAT_TRUNCATE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_TRUNCATE, 1)
```

设置 `BT_OTS_OACP_FEAT_TRUNCATE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gac035cb71a2caabd16bb64d27b56e32c7"></a>

### `BT_OTS_OACP_SET_FEAT_WRITE`

```c
#define BT_OTS_OACP_SET_FEAT_WRITE ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OACP_FEAT_WRITE, 1)
```

设置 `BT_OTS_OACP_FEAT_WRITE` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gaccbf81f9a9ebcc70801739a4a8fafcd8"></a>

### `BT_OTS_OBJ_GET_PROP_APPEND`

```c
#define BT_OTS_OBJ_GET_PROP_APPEND ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_APPEND))
```

获取 `BT_OTS_OBJ_PROP_APPEND` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga7a735cf89c9986624e34b183282a65ee"></a>

### `BT_OTS_OBJ_GET_PROP_DELETE`

```c
#define BT_OTS_OBJ_GET_PROP_DELETE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_DELETE))
```

获取 `BT_OTS_OBJ_PROP_DELETE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga90619bdcf5ec9a942f7d81f6c87465fc"></a>

### `BT_OTS_OBJ_GET_PROP_EXECUTE`

```c
#define BT_OTS_OBJ_GET_PROP_EXECUTE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_EXECUTE))
```

获取 `BT_OTS_OBJ_PROP_EXECUTE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gaeffab993f4fbe15090a7a626cd56f034"></a>

### `BT_OTS_OBJ_GET_PROP_MARKED`

```c
#define BT_OTS_OBJ_GET_PROP_MARKED ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_MARKED))
```

获取 `BT_OTS_OBJ_PROP_MARKED` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga6c8ccb5f8919f062b1b44e1b4981907d"></a>

### `BT_OTS_OBJ_GET_PROP_PATCH`

```c
#define BT_OTS_OBJ_GET_PROP_PATCH ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_PATCH))
```

获取 `BT_OTS_OBJ_PROP_PATCH` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gae846afdc9f6c40b2bf6d2ae67deb8eef"></a>

### `BT_OTS_OBJ_GET_PROP_READ`

```c
#define BT_OTS_OBJ_GET_PROP_READ ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_READ))
```

获取 `BT_OTS_OBJ_PROP_READ` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gac7b6632aac554db5b4d5b9f3e8bf78b4"></a>

### `BT_OTS_OBJ_GET_PROP_TRUNCATE`

```c
#define BT_OTS_OBJ_GET_PROP_TRUNCATE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_TRUNCATE))
```

获取 `BT_OTS_OBJ_PROP_TRUNCATE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga9769628cbe2c81161607c6518d3d4798"></a>

### `BT_OTS_OBJ_GET_PROP_WRITE`

```c
#define BT_OTS_OBJ_GET_PROP_WRITE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((prop) & BIT(BT_OTS_OBJ_PROP_WRITE))
```

获取 `BT_OTS_OBJ_PROP_WRITE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gabe3d54a6dfa0d52a97826c140c603d78"></a>

### `BT_OTS_OBJ_ID_MASK`

```c
#define BT_OTS_OBJ_ID_MASK BIT64_MASK(48)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象传输服务对象标识符（OTS Object ID）的掩码，保留其中的 48 位。

<a id="gabd777e7a1b7adaaacfec3e084c3a9bfe"></a>

### `BT_OTS_OBJ_ID_MAX`

```c
#define BT_OTS_OBJ_ID_MAX 0xFFFFFFFFFFFFULL
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象 ID 的最大允许值，目录列表（Directory Listing）ID 除外。

<a id="ga79110fa56a524754d74bf20ac6a766aa"></a>

### `BT_OTS_OBJ_ID_MIN`

```c
#define BT_OTS_OBJ_ID_MIN 0x000000000100ULL
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象 ID 的最小允许值，目录列表（Directory Listing）ID 除外。

<a id="gad5e4a66f017facc2a185ee0a55a0c3ee"></a>

### `BT_OTS_OBJ_ID_SIZE`

```c
#define BT_OTS_OBJ_ID_SIZE 6
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象传输服务对象标识符（OTS Object ID）的大小，单位为字节。

<a id="ga2754eeb7418ed762a3119fc56871d37e"></a>

### `BT_OTS_OBJ_ID_STR_LEN`

```c
#define BT_OTS_OBJ_ID_STR_LEN 15
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象传输服务对象标识符字符串（OTS Object ID String）的长度，单位为字节。

<a id="gaa1eff1b4ee05fb91d87dcb85dd7469e1"></a>

### `BT_OTS_OBJ_SET_PROP_APPEND`

```c
#define BT_OTS_OBJ_SET_PROP_APPEND ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_APPEND, 1)
```

设置 `BT_OTS_OBJ_PROP_APPEND` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga6ad37ee172d6518e7316b4e0ec8f27c7"></a>

### `BT_OTS_OBJ_SET_PROP_DELETE`

```c
#define BT_OTS_OBJ_SET_PROP_DELETE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_DELETE, 1)
```

设置 `BT_OTS_OBJ_PROP_DELETE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga2342f00ef480b279d737bcddc8e2faf0"></a>

### `BT_OTS_OBJ_SET_PROP_EXECUTE`

```c
#define BT_OTS_OBJ_SET_PROP_EXECUTE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_EXECUTE, 1)
```

设置 `BT_OTS_OBJ_PROP_EXECUTE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gae21e599a85549d5cd4462c0f36c291ac"></a>

### `BT_OTS_OBJ_SET_PROP_MARKED`

```c
#define BT_OTS_OBJ_SET_PROP_MARKED ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_MARKED, 1)
```

设置 `BT_OTS_OBJ_PROP_MARKED` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gac36c68dfeb21bf705f87f11e847c5aed"></a>

### `BT_OTS_OBJ_SET_PROP_PATCH`

```c
#define BT_OTS_OBJ_SET_PROP_PATCH ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_PATCH, 1)
```

设置 `BT_OTS_OBJ_PROP_PATCH` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gaba26016beff74b1b6ec75ba083cf808d"></a>

### `BT_OTS_OBJ_SET_PROP_READ`

```c
#define BT_OTS_OBJ_SET_PROP_READ ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_READ, 1)
```

设置 `BT_OTS_OBJ_PROP_READ` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga8f99514414958d031a4e9985c8cc976b"></a>

### `BT_OTS_OBJ_SET_PROP_TRUNCATE`

```c
#define BT_OTS_OBJ_SET_PROP_TRUNCATE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_TRUNCATE, 1)
```

设置 `BT_OTS_OBJ_PROP_TRUNCATE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="gaeb1a5a907478fd668199a27e20fc2173"></a>

### `BT_OTS_OBJ_SET_PROP_WRITE`

```c
#define BT_OTS_OBJ_SET_PROP_WRITE ( prop)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(prop, BT_OTS_OBJ_PROP_WRITE, 1)
```

设置 `BT_OTS_OBJ_PROP_WRITE` 属性（Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 对象属性（Object properties）。 |

<a id="ga0f57d172615d1c6ea857506dc0c10e55"></a>

### `BT_OTS_OLCP_GET_FEAT_CLEAR`

```c
#define BT_OTS_OLCP_GET_FEAT_CLEAR ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OLCP_FEAT_CLEAR))
```

获取 `BT_OTS_OLCP_GET_FEAT_CLEAR` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga7ec49843849613ee3f8f72209cae68c2"></a>

### `BT_OTS_OLCP_GET_FEAT_GO_TO`

```c
#define BT_OTS_OLCP_GET_FEAT_GO_TO ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OLCP_FEAT_GO_TO))
```

获取 `BT_OTS_OLCP_GET_FEAT_GO_TO` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga2a1a62e410586b1117fd3571e42363d8"></a>

### `BT_OTS_OLCP_GET_FEAT_NUM_REQ`

```c
#define BT_OTS_OLCP_GET_FEAT_NUM_REQ ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OLCP_FEAT_NUM_REQ))
```

获取 `BT_OTS_OLCP_GET_FEAT_NUM_REQ` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gad4393e56c94c2484cd344b48cb54b255"></a>

### `BT_OTS_OLCP_GET_FEAT_ORDER`

```c
#define BT_OTS_OLCP_GET_FEAT_ORDER ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
((feat) & BIT(BT_OTS_OLCP_FEAT_ORDER))
```

获取 `BT_OTS_OLCP_GET_FEAT_ORDER` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga7a3f8d3b725c8c31d5e3062d46db4438"></a>

### `BT_OTS_OLCP_SET_FEAT_CLEAR`

```c
#define BT_OTS_OLCP_SET_FEAT_CLEAR ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OLCP_FEAT_CLEAR, 1)
```

设置 `BT_OTS_OLCP_FEAT_CLEAR` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="gafe219709f2bd318af66cad4e118df658"></a>

### `BT_OTS_OLCP_SET_FEAT_GO_TO`

```c
#define BT_OTS_OLCP_SET_FEAT_GO_TO ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OLCP_FEAT_GO_TO, 1)
```

设置 `BT_OTS_OLCP_FEAT_GO_TO` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga1cee6e1affdff27aa0ba6a655c9bf09c"></a>

### `BT_OTS_OLCP_SET_FEAT_NUM_REQ`

```c
#define BT_OTS_OLCP_SET_FEAT_NUM_REQ ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OLCP_FEAT_NUM_REQ, 1)
```

设置 `BT_OTS_OLCP_FEAT_NUM_REQ` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga1248c694ff2d9ded862f37d03d98e2f0"></a>

### `BT_OTS_OLCP_SET_FEAT_ORDER`

```c
#define BT_OTS_OLCP_SET_FEAT_ORDER ( feat)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

展开值（Value）：

```c
WRITE_BIT(feat, BT_OTS_OLCP_FEAT_ORDER, 1)
```

设置 `BT_OTS_OLCP_FEAT_ORDER` 特性（Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `feat` | 对象传输服务（OTS）的功能（Features）。 |

<a id="ga4f18ea10855379414dd8a70b6c119d6b"></a>

### `BT_OTS_STOP`

```c
#define BT_OTS_STOP 0
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="ga4a6a0b0a3c8d10f3668e61c9dee0e05e"></a>

### `OTS_OBJ_ID_DIR_LIST`

```c
#define OTS_OBJ_ID_DIR_LIST 0x000000000000ULL
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

目录列表对象（Directory Listing Object）的 ID。

<a id="gaa1a9db6e8aa6ee716e4fdd2e34157f46"></a>

### `bt_ots_client_dirlisting_cb`

```c
typedef int(* bt_ots_client_dirlisting_cb) (struct bt_ots_obj_metadata *meta)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

目录列表对象元数据回调（Directory Listing Object Metadata Callback）。

使用 bt_ots_client_decode_dirlisting() 解码目录列表（Directory Listing）时，将针对列表中的每个对象调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta` | 已解码对象的元数据（Metadata）。 |

**返回（Returns）**：返回：int 类型的 BT_OTS_STOP 或 BT_OTS_CONTINUE。可使用 BT_OTS_STOP 停止解码。

<a id="gaea054a2be05dca63c0cd0375649af26b"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象传输服务对象的属性（OTS Object Properties）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OTS_OBJ_PROP_DELETE` | 位 0：允许删除（Deletion）此对象。 |
| `BT_OTS_OBJ_PROP_EXECUTE` | 位 1：允许执行（Execution）此对象。 |
| `BT_OTS_OBJ_PROP_READ` | 位 2：允许读取（Reading）此对象。 |
| `BT_OTS_OBJ_PROP_WRITE` | 位 3：允许向此对象写入（Writing）数据。 |
| `BT_OTS_OBJ_PROP_APPEND` | 位 4：允许向此对象追加（Appending）数据。追加数据会增大其已分配大小（Allocated Size）。 |
| `BT_OTS_OBJ_PROP_TRUNCATE` | 位 5：允许截断（Truncation）此对象。 |
| `BT_OTS_OBJ_PROP_PATCH` | 位 6：允许修补（Patching）此对象。修补会覆盖对象的部分现有内容。 |
| `BT_OTS_OBJ_PROP_MARKED` | 位 7：此对象是已标记对象（Marked Object）。 |

<a id="ga39716a5c8e5097ad2ddeaf8db407024e"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象列表控制点特性位（Object List Control Point Feature Bits）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OTS_OLCP_FEAT_GO_TO` | 位 0：支持对象列表控制点（OLCP）的转到（Go To）操作码。 |
| `BT_OTS_OLCP_FEAT_ORDER` | 位 1：支持对象列表控制点（OLCP）的排序（Order）操作码。 |
| `BT_OTS_OLCP_FEAT_NUM_REQ` | 位 2：支持对象列表控制点（OLCP）的请求对象数量（Request Number of Objects）操作码。 |
| `BT_OTS_OLCP_FEAT_CLEAR` | 位 3：支持对象列表控制点（OLCP）的清除标记（Clear Marking）操作码。 |

<a id="ga9bbade1b48363f0f486968723afefb45"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象元数据请求位字段值（Object Metadata Request Bit Field Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OTS_METADATA_REQ_NAME` | 请求对象名称（Object Name）。 |
| `BT_OTS_METADATA_REQ_TYPE` | 请求对象类型（Object Type）。 |
| `BT_OTS_METADATA_REQ_SIZE` | 请求对象大小（Object Size）。 |
| `BT_OTS_METADATA_REQ_CREATED` | 请求对象首次创建时间（Object First Created Time）。 |
| `BT_OTS_METADATA_REQ_MODIFIED` | 请求对象最后修改时间（Object Last Modified Time）。 |
| `BT_OTS_METADATA_REQ_ID` | 请求对象 ID（Object ID）。 |
| `BT_OTS_METADATA_REQ_PROPS` | 请求对象属性（Object Properties）。 |
| `BT_OTS_METADATA_REQ_ALL` | 请求全部对象元数据（Object Metadata）。 |

<a id="ga141f5762339600942eb229bfdc183ebb"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象动作控制点特性位（Object Action Control Point Feature Bits）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OTS_OACP_FEAT_CREATE` | 位 0：支持对象动作控制点（OACP）的创建（Create）操作码。 |
| `BT_OTS_OACP_FEAT_DELETE` | 位 1：支持对象动作控制点（OACP）的删除（Delete）操作码。 |
| `BT_OTS_OACP_FEAT_CHECKSUM` | 位 2：支持对象动作控制点（OACP）的计算校验和（Calculate Checksum）操作码。 |
| `BT_OTS_OACP_FEAT_EXECUTE` | 位 3：支持对象动作控制点（OACP）的执行（Execute）操作码。 |
| `BT_OTS_OACP_FEAT_READ` | 位 4：支持对象动作控制点（OACP）的读取（Read）操作码。 |
| `BT_OTS_OACP_FEAT_WRITE` | 位 5：支持对象动作控制点（OACP）的写入（Write）操作码。 |
| `BT_OTS_OACP_FEAT_APPEND` | 位 6：支持向对象追加额外数据（Appending Additional Data）。 |
| `BT_OTS_OACP_FEAT_TRUNCATE` | 位 7：支持对象截断（Truncation）。 |
| `BT_OTS_OACP_FEAT_PATCH` | 位 8：支持对象修补（Patching）。 |
| `BT_OTS_OACP_FEAT_ABORT` | 位 9：支持对象动作控制点（OACP）的中止（Abort）操作码。 |

<a id="gaebdd2b8a80948d1050d42fa3963cc863"></a>

### `bt_ots_oacp_write_op_mode`

```c
enum bt_ots_oacp_write_op_mode
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OTS_OACP_WRITE_OP_MODE_NONE` |  |
| `BT_OTS_OACP_WRITE_OP_MODE_TRUNCATE` |  |

<a id="ga63e4408702fee1be0501a715cd32c957"></a>

### `bt_ots_client_calc_checksum()`

```c
uint32_t bt_ots_client_calc_checksum ( const uint8_t * data, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/services/ots.h>
```

生成符合 IEEE 标准的 CRC32 校验和（Checksum）。

为服务层抽象 IEEE 实现（IEEE Implementation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 指向要计算循环冗余校验（CRC）的数据的指针。 |
| `len` | 数据长度（Data Length）。 |

**返回（Returns）**：返回：CRC32 值。

<a id="gabe485816a2e536758a7ce85c593ea486"></a>

### `bt_ots_client_decode_dirlisting()`

```c
int bt_ots_client_decode_dirlisting ( uint8_t * data, uint16_t length, bt_ots_client_dirlisting_cb cb )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

将目录列表对象（Directory Listing Object）解码为对象元数据（Object Metadata）。

如果目录列表对象（Directory Listing Object）包含多个对象，则会针对每个对象调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 接收到的目录列表对象（Directory Listing Object）数据。 |
| `length` | 数据长度（Data Length）。 |
| `cb` | 针对每个对象调用的回调（Callback）。 |

<a id="ga9cfd057d39ce3fe9bbecaa103ec44f77"></a>

### `bt_ots_client_get_object_checksum()`

```c
int bt_ots_client_get_object_checksum ( struct bt_ots_client * otc_inst, struct bt_conn * conn, off_t offset, size_t len )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

获取当前选定对象的校验和（Checksum）。

这会针对当前对象触发 OACP 计算校验和操作（Calculate Checksum），使用指定的偏移量和长度。

校验和（Checksum）通过 OACP 指示（IND）和 obj_checksum_calculated() 回调传递。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |
| `offset` | 开始计算的偏移量（Offset），通常为 0。 |
| `len` | 要计算校验和的数据长度（Len）。可小于当前对象大小，但不得大于它。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="gac270137f15596777287f68b3d6a6a11c"></a>

### `bt_ots_client_indicate_handler()`

```c
uint8_t bt_ots_client_indicate_handler ( struct bt_conn * conn, struct bt_gatt_subscribe_params * params, const void * data, uint16_t length )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

对象传输服务指示处理函数（OTS Indicate Handler）。

发现 OTS 时，将此函数设为指示处理程序（Indicate Handler）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。可以为 NULL，表示正在取消与对端的配对。 |
| `params` | 订阅参数（Subscription Parameters）。 |
| `data` | 属性值数据（Attribute Value Data）。若为 NULL，表示订阅已移除。 |
| `length` | 属性值长度（Attribute Value Length）。 |

<a id="gaf11589afc37efe18dcac122835a4c95d"></a>

### `bt_ots_client_read_feature()`

```c
int bt_ots_client_read_feature ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

读取对象传输服务特性特征（OTS Feature Characteristic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga8ad1c53325c1b77271307507317a5965"></a>

### `bt_ots_client_read_object_data()`

```c
int bt_ots_client_read_object_data ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

读取当前选定对象的数据。

这会以偏移量 0、对象当前大小为长度触发 OACP 读取操作（Read），随后等待通过 L2CAP 面向连接信道（CoC）接收内容。

对象数据通过 obj_data_read() 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga936f392c880c9d1a73f2bd632e5b63e0"></a>

### `bt_ots_client_read_object_metadata()`

```c
int bt_ots_client_read_object_metadata ( struct bt_ots_client * otc_inst, struct bt_conn * conn, uint8_t metadata )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

读取当前对象的元数据（Metadata）。

元数据（Metadata）通过 obj_metadata_read() 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |
| `metadata` | 要读取的元数据位域（Metadata Bitfield），使用 BT_OTS_METADATA_REQ_*。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="gadefd2ccb46a686a4aa2999da5851184b"></a>

### `bt_ots_client_register()`

```c
int bt_ots_client_register ( struct bt_ots_client * ots_inst)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

注册对象传输服务实例（Object Transfer Service Instance）。

注册在对端发现的对象传输服务实例（Object Transfer Service Instance）。发现 OTS 实例时调用此函数；发现过程由上层处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ots_inst` | 发现的 OTS 实例（Instance）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga70cae251cf40a5c3c8d2a8c7e1f1e181"></a>

### `bt_ots_client_select_first()`

```c
int bt_ots_client_select_first ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

选择第一个对象（First Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga5f2d0b0e4d54e00a1a96157fcfaf172b"></a>

### `bt_ots_client_select_id()`

```c
int bt_ots_client_select_id ( struct bt_ots_client * otc_inst, struct bt_conn * conn, uint64_t obj_id )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

按对象标识符（Object ID）选择对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |
| `obj_id` | 对象 ID（Object ID）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga89fc03d68725de0b5f306c899452b1a8"></a>

### `bt_ots_client_select_last()`

```c
int bt_ots_client_select_last ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

选择最后一个对象（Last Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga81997ab2f1718c6856e676eb9b3f72bb"></a>

### `bt_ots_client_select_next()`

```c
int bt_ots_client_select_next ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

选择下一个对象（Next Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="gac84ed7f16fa86d87531d04e2957568f9"></a>

### `bt_ots_client_select_prev()`

```c
int bt_ots_client_select_prev ( struct bt_ots_client * otc_inst, struct bt_conn * conn )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

选择上一个对象（Previous Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="gabba031c38c7503c1f434a761d9f65df4"></a>

### `bt_ots_client_unregister()`

```c
int bt_ots_client_unregister ( uint8_t index)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

注销对象传输服务实例（Object Transfer Service Instance）。

与对端断开时，注销对象传输服务实例（Object Transfer Service Instance）。使用 OTS 实例的 ACL 断开时调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] index` | OTS 实例索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="ga9444b064c616718dae1577b21540fb9a"></a>

### `bt_ots_client_write_object_data()`

```c
int bt_ots_client_write_object_data ( struct bt_ots_client * otc_inst, struct bt_conn * conn, const void * buf, size_t len, off_t offset, enum bt_ots_oacp_write_op_mode mode )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

写入当前选定对象的数据。

这会针对当前对象以指定偏移量触发 OACP 写入操作（Write），随后准备通过 L2CAP 面向连接信道（CoC）传输内容。

写入对象的数据长度通过 obj_data_written() 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otc_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 指向连接对象（Connection Object）的指针。 |
| `buf` | 指向待写入数据缓冲区的指针。 |
| `len` | 数据大小（Data Size）。 |
| `offset` | 写入偏移量（Offset），通常为 0。 |
| `mode` | OACP 写入操作码（Write Op Code）的模式参数（Mode Parameter）。参见 bt_ots_oacp_write_op_mode。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 ERRNO。

<a id="gafc71de8fd65212045fa26b2a81e3876d"></a>

### `bt_ots_free_instance_get()`

```c
struct bt_ots * bt_ots_free_instance_get ( void )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

从池中获取空闲的对象传输服务（OTS）实例。

**返回（Returns）**：返回：成功时为 OTS 实例，发生错误时为 NULL。

<a id="ga1c9dcb35c8f07432fd9249a34e597819"></a>

### `bt_ots_init()`

```c
int bt_ots_init ( struct bt_ots * ots, struct bt_ots_init_param * ots_init )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

初始化对象传输服务（OTS）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `ots_init` | OTS 初始化描述符（Initialization Descriptor）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga8324cc14e8812648cc3663144591af89"></a>

### `bt_ots_metadata_display()`

```c
void bt_ots_metadata_display ( struct bt_ots_obj_metadata * metadata, uint16_t count )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

使用 `LOG_INF` 将一个或多个对象的元数据（Metadata）显示为文本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `metadata` | 指向数组中第一个或唯一一个元数据（Metadata）元素的指针。 |
| `count` | 要显示信息的元数据对象（Metadata Objects）数量。 |

<a id="gabf59844edd0ffd434acd94bad9a7b52c"></a>

### `bt_ots_obj_add()`

```c
int bt_ots_obj_add ( struct bt_ots * ots, const struct bt_ots_obj_add_param * param )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

向对象传输服务（OTS）实例添加对象。

此函数向 OTS 数据库（Database）添加对象。添加对象时，会调用 obj_created() 回调，向使用者通知新对象的 ID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `param` | 对象添加参数（Object Addition Parameters）。 |

**返回（Returns）**：返回：成功时为已创建对象的 ID，发生错误时为负值。

<a id="ga872ba5a73fa4e617b9d48e7361af74c7"></a>

### `bt_ots_obj_delete()`

```c
int bt_ots_obj_delete ( struct bt_ots * ots, uint64_t id )
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

从对象传输服务（OTS）实例删除对象。

此函数从 OTS 数据库（Database）删除对象。删除对象时，会调用 obj_deleted() 回调通知使用者。此时可释放为对象数据分配的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `id` | 要删除对象的 ID，类型为 uint48。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac9be2770fc7f2932ea2e31392d956f0a"></a>

### `bt_ots_obj_id_to_str()`

```c
int bt_ots_obj_id_to_str ( uint64_t obj_id, char * str, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/services/ots.h>
```

将二进制对象传输服务对象标识符（OTS Object ID）转换为字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj_id` | 对象标识（Object ID）。 |
| `str` | 用户缓冲区（User Buffer）的地址；缓冲区须有足够空间保存由二进制对象 ID 格式化得到的字符串。 |
| `len` | 要复制到用户字符串缓冲区的数据长度。推荐值参见 BT_OTS_OBJ_ID_STR_LEN。 |

**返回（Returns）**：返回：从二进制 ID 成功格式化得到的字节数。

<a id="gabe637ba9febb514f7346d71696b70c73"></a>

### `bt_ots_svc_decl_get()`

```c
void * bt_ots_svc_decl_get ( struct bt_ots * ots)
```

```c
#include <zephyr/bluetooth/services/ots.h>
```

获取服务声明属性（Service Declaration Attribute）。

在 CONFIG_BT_OTS_SECONDARY_SVC 配置下启用此函数。可将第一个服务属性（Service Attribute）包含在任何其他 GATT 服务中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |

**返回（Returns）**：返回：第一个 OTS 属性实例（Attribute Instance）。


## 5.7\_原页交叉引用（Cross References）

- [bt_ots_obj_type](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md)
- [bt_ots_obj_size](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md)
- [bt_ots_feat](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md)
- [bt_ots_date_time](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md)
- [bt_ots_obj_metadata](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md)
- [bt_ots_obj_add_param](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md)
- [bt_ots_obj_created_desc](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md)
- [bt_ots_cb](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md)
- [bt_ots_init_param](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md)
- [bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)
- [bt_ots_client_cb](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md)
- [bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/bluetooth/services/ots.h](../api_file_power_ots_reference/P004_zephyr__bluetooth__services__ots.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [WRITE_BIT](../util_reference/P001_通用工具公共接口.md#ga23a900e882ecb48455e70f01fd45b246)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab"></a>
<a id="agroup__sys-util_html_ga23a900e882ecb48455e70f01fd45b246"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed"></a>
<a id="ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3"></a>
<a id="gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713"></a>
<a id="gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d"></a>
<a id="gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660"></a>
<a id="gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af"></a>
<a id="gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb"></a>
<a id="gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9"></a>
<a id="gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5"></a>
<a id="gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095"></a>
<a id="gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e"></a>
<a id="gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2"></a>
<a id="gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f"></a>
<a id="gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf"></a>
<a id="gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9"></a>
<a id="gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee"></a>
<a id="gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f"></a>
<a id="gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c"></a>
<a id="gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465"></a>
<a id="gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab"></a>
<a id="gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b"></a>
<a id="gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225"></a>
<a id="gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf"></a>
<a id="gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440"></a>
<a id="ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab"></a>
<a id="ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_逻辑链路控制与适配协议（L2CAP）.md) · [返回大纲](大纲.md) · [下一章](P006_数字音频接口（DAI）.md)
