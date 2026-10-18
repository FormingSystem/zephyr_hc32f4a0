---
id: learning.zephyr-docs.api-source-reference.page-82
title: callback_defines.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_callback\_defines.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h.html)。

## 82.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00020"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="agroup__mcumgr__callback__api_html_ga1ba636c0efb7a91630ed9743e6fd4d6c"></a>
<a id="agroup__mcumgr__callback__api_html_ga40ecf8933112abe76d7fedb3dcc7cdbe"></a>
<a id="agroup__mcumgr__callback__api_html_gaab6470007be89e5aab88838456f9561a"></a>
<a id="agroup__mcumgr__callback__api_html_gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990"></a>
<a id="agroup__mcumgr__callback__api_html_gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da"></a>
<a id="agroup__mcumgr__callback__api_html_gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1"></a>
<a id="agroup__mcumgr__callback__api_html_ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACK_DEFINES_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACK_DEFINES_H_

#ifdef __cplusplus
extern "C" {
#endif


#define MGMT_EVT_OP_ID_ALL 0xffff

#define MGMT_DEF_EVT_OP_ID(group, event_id) ((group << 16) | BIT(event_id))

#define MGMT_DEF_EVT_OP_ALL(group) ((group << 16) | MGMT_EVT_OP_ID_ALL)

#define MGMT_EVT_GET_GROUP(event) ((event >> 16) & MGMT_EVT_OP_ID_ALL)

#define MGMT_EVT_GET_ID(event) (event & MGMT_EVT_OP_ID_ALL)

enum mgmt_cb_return {
        MGMT_CB_OK,

        MGMT_CB_ERROR_RC,

        MGMT_CB_ERROR_ERR,
};

enum mgmt_cb_groups {
        MGMT_EVT_GRP_ALL                        = 0,
        MGMT_EVT_GRP_SMP,
        MGMT_EVT_GRP_OS,
        MGMT_EVT_GRP_IMG,
        MGMT_EVT_GRP_FS,
        MGMT_EVT_GRP_SETTINGS,
        MGMT_EVT_GRP_ENUM,

        MGMT_EVT_GRP_USER_CUSTOM_START          = MGMT_GROUP_ID_PERUSER,
};

enum smp_all_events {
        MGMT_EVT_OP_ALL                         = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ALL),
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACK_DEFINES_H_ */
```

## 82.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACK_DEFINES_H_`。

## 82.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h.html)
- [mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)
- [MGMT_CB_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da)
- [MGMT_CB_ERROR_RC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990)
- [MGMT_CB_ERROR_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d)
- [mgmt_cb_groups](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga40ecf8933112abe76d7fedb3dcc7cdbe)
- [MGMT_EVT_GRP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a)
- [MGMT_EVT_GRP_SMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)
- [MGMT_EVT_GRP_OS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)
- [MGMT_EVT_GRP_IMG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)
- [MGMT_EVT_GRP_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)
- [MGMT_EVT_GRP_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)
- [MGMT_EVT_GRP_ENUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)
- [MGMT_EVT_GRP_USER_CUSTOM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d)
- [MGMT_GROUP_ID_PERUSER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)
- [smp_all_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaab6470007be89e5aab88838456f9561a)
- [MGMT_EVT_OP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)

---

[上一章](P081_buzzer.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P083_callbacks.h_源码浏览.md)
