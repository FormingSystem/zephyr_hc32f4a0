---
id: learning.zephyr-docs.api-source-runtime-reference.page-10
title: conn_mgr_connectivity.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_conn\_mgr\_connectivity.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)。

## 10.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00033"></a>
<a id="l00034"></a>
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
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00325"></a>
<a id="l00334"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__conn__mgr__connectivity__bulk_html_ga3ce45d9040d3799e1387776257dfa8b7"></a>
<a id="agroup__conn__mgr__connectivity__bulk_html_ga48e3c1b98f505af9f8ac811a25f94e1b"></a>
<a id="agroup__conn__mgr__connectivity__bulk_html_ga9e006b8b5095c223d77055fd619710c3"></a>
<a id="agroup__conn__mgr__connectivity__bulk_html_gabf6f8e5d8ce51b4c1cbf48f18a57efb2"></a>
<a id="agroup__conn__mgr__connectivity_html_ga09a1169a89eac1a3291185281952ce05"></a>
<a id="agroup__conn__mgr__connectivity_html_ga2a2e6d7fbb7b1ed0327706a8c253d3e4"></a>
<a id="agroup__conn__mgr__connectivity_html_ga4079113088236aede697538d79e5272f"></a>
<a id="agroup__conn__mgr__connectivity_html_ga465c9491106cba3c9cb1cf296090612b"></a>
<a id="agroup__conn__mgr__connectivity_html_ga467ecbb330d21b8dfea3e0ce08448400"></a>
<a id="agroup__conn__mgr__connectivity_html_ga575d367c95592fd9f4ead694ff94543f"></a>
<a id="agroup__conn__mgr__connectivity_html_ga5d22b2a44c3595a5b7b240c8fe7d0db1"></a>
<a id="agroup__conn__mgr__connectivity_html_ga93f333199c87b2d7668e94c92efd31ce"></a>
<a id="agroup__conn__mgr__connectivity_html_gaa79794ce9c773c0c3932121c931ac2d6"></a>
<a id="agroup__conn__mgr__connectivity_html_gada2b5271b3e5dbcab629e1538b3d8eb4"></a>
<a id="agroup__conn__mgr__connectivity_html_gada9c37847acc604d82604351cbbb5e64"></a>
<a id="agroup__conn__mgr__connectivity_html_gae86d1c808f31b8ca5e67bacbc844ef47"></a>
<a id="agroup__conn__mgr__connectivity_html_gaf10fb532a3dd07ec8c692a72643d0e3f"></a>
<a id="agroup__conn__mgr__connectivity_html_ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f"></a>
<a id="agroup__conn__mgr__connectivity_html_ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d"></a>
<a id="agroup__conn__mgr__connectivity_html_ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astructnet__if_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_H_
#define ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_H_

#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif




/* Connectivity Events */
#define NET_MGMT_CONN_LAYER                     NET_MGMT_LAYER(NET_MGMT_LAYER_L2)
#define NET_MGMT_CONN_CODE                      NET_MGMT_LAYER_CODE(NET_MGMT_LAYER_CODE_CONN)
#define NET_MGMT_CONN_BASE                      (NET_MGMT_CONN_LAYER | NET_MGMT_CONN_CODE | \
                                                 NET_MGMT_EVENT_BIT)
#define NET_MGMT_CONN_IF_EVENT                  (NET_MGMT_IFACE_BIT | NET_MGMT_CONN_BASE)

enum {
        NET_EVENT_CONN_CMD_IF_TIMEOUT_VAL,
        NET_EVENT_CONN_CMD_IF_FATAL_ERROR_VAL,
        NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT_VAL,
        NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION_VAL,

        NET_EVENT_CONN_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_CONN_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_conn_cmd exceeds the limit");

enum net_event_conn_cmd {
        NET_MGMT_CMD(NET_EVENT_CONN_CMD_IF_TIMEOUT),
        NET_MGMT_CMD(NET_EVENT_CONN_CMD_IF_FATAL_ERROR),
        NET_MGMT_CMD(NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT),
        NET_MGMT_CMD(NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION),
};


#define NET_EVENT_CONN_IF_TIMEOUT                                       \
        (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_TIMEOUT)

#define NET_EVENT_CONN_IF_FATAL_ERROR                                   \
        (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_FATAL_ERROR)

#define NET_EVENT_CONN_IF_IDLE_TIMEOUT                                  \
        (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT)

#define NET_EVENT_CONN_IF_NO_CONFIGURATION                                      \
        (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION)

enum conn_mgr_if_flag {
        CONN_MGR_IF_PERSISTENT,

        CONN_MGR_IF_NO_AUTO_CONNECT,

        CONN_MGR_IF_NO_AUTO_DOWN,

        CONN_MGR_IF_DISCONNECTING,

        /* Total number of flags - must be at the end of the enum */
        CONN_MGR_NUM_IF_FLAGS,
};

#define CONN_MGR_IF_NO_TIMEOUT 0

int conn_mgr_if_connect(struct net_if *iface);

int conn_mgr_if_disconnect(struct net_if *iface);

bool conn_mgr_if_is_bound(struct net_if *iface);

int conn_mgr_if_set_opt(struct net_if *iface, int optname, const void *optval, size_t optlen);

int conn_mgr_if_get_opt(struct net_if *iface, int optname, void *optval, size_t *optlen);

bool conn_mgr_if_get_flag(struct net_if *iface, enum conn_mgr_if_flag flag);

int conn_mgr_if_set_flag(struct net_if *iface, enum conn_mgr_if_flag flag, bool value);

int conn_mgr_if_get_timeout(struct net_if *iface);

int conn_mgr_if_set_timeout(struct net_if *iface, int timeout);

int conn_mgr_if_get_idle_timeout(struct net_if *iface);

int conn_mgr_if_set_idle_timeout(struct net_if *iface, int timeout);

#if defined(CONFIG_NET_CONNECTION_MANAGER) || defined(__DOXYGEN__)
void conn_mgr_if_used(struct net_if *iface);
#else
#define conn_mgr_if_used(iface) (void)(iface)
#endif /* defined(CONFIG_NET_CONNECTION_MANAGER) || defined(__DOXYGEN__) */



int conn_mgr_all_if_up(bool skip_ignored);


int conn_mgr_all_if_down(bool skip_ignored);

int conn_mgr_all_if_connect(bool skip_ignored);

int conn_mgr_all_if_disconnect(bool skip_ignored);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

连接性事件（Connectivity Events）。

### 注释 3：原第 124 行

标志总数，必须位于枚举末尾。

### 注释 4：原第 320 行

条件编译表达式：`defined(CONFIG_NET_CONNECTION_MANAGER) || defined(__DOXYGEN__)`。

### 注释 5：原第 394 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [CONN_MGR_IF_PERSISTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f)
- [CONN_MGR_IF_NO_AUTO_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd)
- [CONN_MGR_IF_NO_AUTO_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d)
- [conn_mgr_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga575d367c95592fd9f4ead694ff94543f)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_if_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada2b5271b3e5dbcab629e1538b3d8eb4)
- [conn_mgr_if_is_bound](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga09a1169a89eac1a3291185281952ce05)
- [conn_mgr_if_set_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)
- [conn_mgr_if_get_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaa79794ce9c773c0c3932121c931ac2d6)
- [conn_mgr_if_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga465c9491106cba3c9cb1cf296090612b)
- [conn_mgr_if_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gae86d1c808f31b8ca5e67bacbc844ef47)
- [conn_mgr_if_get_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada9c37847acc604d82604351cbbb5e64)
- [conn_mgr_if_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga467ecbb330d21b8dfea3e0ce08448400)
- [conn_mgr_if_get_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5d22b2a44c3595a5b7b240c8fe7d0db1)
- [conn_mgr_if_set_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga93f333199c87b2d7668e94c92efd31ce)
- [conn_mgr_if_used](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga4079113088236aede697538d79e5272f)
- [conn_mgr_all_if_up](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html#ga9e006b8b5095c223d77055fd619710c3)
- [conn_mgr_all_if_down](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)
- [conn_mgr_all_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html#ga48e3c1b98f505af9f8ac811a25f94e1b)
- [conn_mgr_all_if_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html#ga3ce45d9040d3799e1387776257dfa8b7)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P009_coap_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_conn_mgr_connectivity_impl.h_源码浏览.md)
