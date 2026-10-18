---
id: learning.zephyr-docs.api-source-reference.page-258
title: fido2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第258章\_fido2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h.html)。

## 258.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="afido2__types_8h_html"></a>
<a id="agroup__fido2_html_ga020303d5fcc00471feba64eec8e169c2"></a>
<a id="agroup__fido2_html_gab41b4d957882b8d6844316ec2f3ccc95"></a>
<a id="agroup__fido2_html_gabf5068079e94310fb4b942df56ec1d10"></a>
<a id="agroup__fido2_html_gac2fecd9d7d18fbb8ff4b8e1083f86059"></a>
<a id="agroup__fido2_html_gad0a191f4a48998fe857dc6315d225d94"></a>
<a id="agroup__fido2_html_gae7a1b8c0bf42ee2a0c3de0bc54c4fa72"></a>
<a id="agroup__fido2_html_gaeb4e348615069d77a81fb87c6970b640"></a>
<a id="agroup__fido2_html_gaeb569aaa63c3c005d0df0b08c38896e1"></a>
<a id="agroup__fido2_html_ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774"></a>
<a id="agroup__fido2_html_ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a"></a>
<a id="agroup__fido2_html_ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909"></a>
<a id="agroup__fido2_html_ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_H_

#include <zephyr/authentication/fido2/fido2_types.h>


#ifdef __cplusplus
extern "C" {
#endif

enum fido2_runtime_state {
        FIDO2_RUNTIME_STATE_STOPPED = 0,
        FIDO2_RUNTIME_STATE_IDLE,
        FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE,
        FIDO2_RUNTIME_STATE_PROCESSING,
};

typedef void (*fido2_state_callback_t)(enum fido2_runtime_state state, void *user_data);

int fido2_init(void);

int fido2_start(void);

int fido2_stop(void);

int fido2_set_state_callback(fido2_state_callback_t cb, void *user_data);

enum fido2_runtime_state fido2_get_state(void);

int fido2_reset(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_H_ */
```

## 258.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_H_`。

## 258.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h.html)
- [zephyr/authentication/fido2/fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [fido2_runtime_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabf5068079e94310fb4b942df56ec1d10)
- [FIDO2_RUNTIME_STATE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67)
- [FIDO2_RUNTIME_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a)
- [FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909)
- [FIDO2_RUNTIME_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774)
- [fido2_state_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a191f4a48998fe857dc6315d225d94)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [fido2_init](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga020303d5fcc00471feba64eec8e169c2)
- [fido2_start](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7a1b8c0bf42ee2a0c3de0bc54c4fa72)
- [fido2_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab41b4d957882b8d6844316ec2f3ccc95)
- [fido2_set_state_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gac2fecd9d7d18fbb8ff4b8e1083f86059)
- [fido2_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb4e348615069d77a81fb87c6970b640)
- [fido2_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb569aaa63c3c005d0df0b08c38896e1)
- [fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)

---

[上一章](P257_fdt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P259_fido2_attestation.h_源码浏览.md)
