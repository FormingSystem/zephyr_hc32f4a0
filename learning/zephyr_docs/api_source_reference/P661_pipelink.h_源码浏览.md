---
id: learning.zephyr-docs.api-source-reference.page-661
title: pipelink.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第661章\_pipelink.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html)。

## 661.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00152"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__modem__pipelink_html_ga399168cacd287e376df68c4cf221ba00"></a>
<a id="agroup__modem__pipelink_html_ga4f93732f1df6cab41cc352526d6a849e"></a>
<a id="agroup__modem__pipelink_html_ga684ff47ddb0e0487022cea62052b32e2"></a>
<a id="agroup__modem__pipelink_html_ga7c7638ad3f22533f374e002b787b11ce"></a>
<a id="agroup__modem__pipelink_html_ga7ee7b3454a9fe94c20855a893dd2b2a1"></a>
<a id="agroup__modem__pipelink_html_gab09d76f7bd93a19b82a7d5e818b80d80"></a>
<a id="agroup__modem__pipelink_html_gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f"></a>
<a id="agroup__modem__pipelink_html_gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d"></a>
<a id="apipe_8h_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/modem/pipe.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util.h>

#ifndef ZEPHYR_INCLUDE_MODEM_PIPELINK_H_
#define ZEPHYR_INCLUDE_MODEM_PIPELINK_H_

#ifdef __cplusplus
extern "C" {
#endif


enum modem_pipelink_event {
        MODEM_PIPELINK_EVENT_CONNECTED = 0,
        MODEM_PIPELINK_EVENT_DISCONNECTED,
};


struct modem_pipelink;


typedef void (*modem_pipelink_callback)(struct modem_pipelink *link,
                                        enum modem_pipelink_event event,
                                        void *user_data);


struct modem_pipelink {
        struct modem_pipe *pipe;
        modem_pipelink_callback callback;
        void *user_data;
        bool connected;
        struct k_spinlock spinlock;
};


void modem_pipelink_attach(struct modem_pipelink *link,
                           modem_pipelink_callback callback,
                           void *user_data);

bool modem_pipelink_is_connected(struct modem_pipelink *link);

struct modem_pipe *modem_pipelink_get_pipe(struct modem_pipelink *link);

void modem_pipelink_release(struct modem_pipelink *link);


void modem_pipelink_init(struct modem_pipelink *link, struct modem_pipe *pipe);

void modem_pipelink_notify_connected(struct modem_pipelink *link);

void modem_pipelink_notify_disconnected(struct modem_pipelink *link);



#define MODEM_PIPELINK_DT_SYM(node_id, name) \
        CONCAT(__modem_pipelink_, DT_DEP_ORD(node_id), _, name)


#define MODEM_PIPELINK_DT_DECLARE(node_id, name) \
        extern struct modem_pipelink MODEM_PIPELINK_DT_SYM(node_id, name)

#define MODEM_PIPELINK_DT_DEFINE(node_id, name) \
        struct modem_pipelink MODEM_PIPELINK_DT_SYM(node_id, name)

#define MODEM_PIPELINK_DT_GET(node_id, name) \
        (&MODEM_PIPELINK_DT_SYM(node_id, name))


#define MODEM_PIPELINK_DT_INST_DECLARE(inst, name) \
        MODEM_PIPELINK_DT_DECLARE(DT_DRV_INST(inst), name)

#define MODEM_PIPELINK_DT_INST_DEFINE(inst, name) \
        MODEM_PIPELINK_DT_DEFINE(DT_DRV_INST(inst), name)

#define MODEM_PIPELINK_DT_INST_GET(inst, name) \
        MODEM_PIPELINK_DT_GET(DT_DRV_INST(inst), name)



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_PIPELINK_H_ */
```

## 661.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_PIPELINK_H_`。

## 661.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [modem_pipelink_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga399168cacd287e376df68c4cf221ba00)
- [MODEM_PIPELINK_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f)
- [MODEM_PIPELINK_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d)
- [modem_pipelink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga4f93732f1df6cab41cc352526d6a849e)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [modem_pipelink_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7ee7b3454a9fe94c20855a893dd2b2a1)
- [modem_pipelink_is_connected](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7c7638ad3f22533f374e002b787b11ce)
- [modem_pipelink_get_pipe](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gab09d76f7bd93a19b82a7d5e818b80d80)
- [modem_pipelink_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga684ff47ddb0e0487022cea62052b32e2)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P660_pio_rpi_pico.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P662_pm.h_源码浏览.md)
