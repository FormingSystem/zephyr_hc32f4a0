---
id: learning.zephyr-docs.api-file-interface-reference.page-6
title: zephyr__mgmt__mcumgr__mgmt__callback_defines.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_mgmt\_\_mcumgr\_\_mgmt\_\_callback\_defines.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_gaa3290bd9a21f9718adac92bfe313161f"></a>

```c
#define MGMT_EVT_GET_GROUP(event)
```

相关声明：[MGMT_EVT_GET_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaa3290bd9a21f9718adac92bfe313161f)。

从事件（event）中提取组（group）。

<a id="r_ga4c6ff3fb3b14a31e65248cec9840b1dd"></a>

```c
#define MGMT_EVT_GET_ID(event)
```

相关声明：[MGMT_EVT_GET_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga4c6ff3fb3b14a31e65248cec9840b1dd)。

从事件中提取事件标识符（event ID）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_ga1ba636c0efb7a91630ed9743e6fd4d6c"></a>

```c
enum mgmt_cb_return { MGMT_CB_OK , MGMT_CB_ERROR_RC , MGMT_CB_ERROR_ERR }
```

相关声明：[mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[MGMT_CB_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da)、[MGMT_CB_ERROR_RC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990)、[MGMT_CB_ERROR_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d)。

管理（MGMT）事件回调的返回值。

<a id="r_ga40ecf8933112abe76d7fedb3dcc7cdbe"></a>

```c
enum mgmt_cb_groups { MGMT_EVT_GRP_ALL = 0 , MGMT_EVT_GRP_SMP , MGMT_EVT_GRP_OS , MGMT_EVT_GRP_IMG , MGMT_EVT_GRP_FS , MGMT_EVT_GRP_SETTINGS , MGMT_EVT_GRP_ENUM , MGMT_EVT_GRP_USER_CUSTOM_START = MGMT_GROUP_ID_PERUSER }
```

相关声明：[mgmt_cb_groups](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga40ecf8933112abe76d7fedb3dcc7cdbe)、[MGMT_EVT_GRP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a)、[MGMT_EVT_GRP_SMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)、[MGMT_EVT_GRP_OS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)、[MGMT_EVT_GRP_IMG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)、[MGMT_EVT_GRP_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)、[MGMT_EVT_GRP_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)、[MGMT_EVT_GRP_ENUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)、[MGMT_EVT_GRP_USER_CUSTOM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d)。

MGMT 事件回调的组标识符（group IDs）。

<a id="r_gaab6470007be89e5aab88838456f9561a"></a>

```c
enum smp_all_events { MGMT_EVT_OP_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ALL) }
```

相关声明：[smp_all_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaab6470007be89e5aab88838456f9561a)、[MGMT_EVT_OP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)。

所有命令处理操作所用的 MGMT 事件操作码（opcodes）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P082_callback_defines.h_源码浏览.md)
- [MGMT_EVT_GET_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaa3290bd9a21f9718adac92bfe313161f)
- [MGMT_EVT_GET_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga4c6ff3fb3b14a31e65248cec9840b1dd)
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
- [smp_all_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaab6470007be89e5aab88838456f9561a)
- [MGMT_EVT_OP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)

---

[上一章](P005_zephyr__bluetooth__crypto.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__bluetooth__audio__ccid.h_文件参考.md)
