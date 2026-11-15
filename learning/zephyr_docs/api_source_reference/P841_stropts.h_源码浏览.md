---
id: learning.zephyr-docs.api-source-reference.page-841
title: stropts.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第841章\_stropts.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html)。

## 841.1\_原始可见代码（Source Code）

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
<a id="foldopen00014"></a>
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
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astropts_8h_html_a2e8c9b125d5b2b9e9c0f119bb8489c5e"></a>
<a id="astropts_8h_html_a49857bef3fb1cecd099e67c8df35c8ef"></a>
<a id="astropts_8h_html_a55b37250892d8a0821df369a5f744099"></a>
<a id="astropts_8h_html_aad1d52cad379cd124cbed912aa636ad1"></a>
<a id="astropts_8h_html_ace3f43f93319016fce6e1ce8bb135ee2"></a>
<a id="astropts_8h_html_add5237bf6844593ab11f8daa15d16070"></a>
<a id="astructstrbuf_html"></a>
<a id="astructstrbuf_html_a2ce53f2d390a31cdabe5299c73e489b0"></a>
<a id="astructstrbuf_html_a421c67aa5a9400a826e8e274f1ffb900"></a>
<a id="astructstrbuf_html_a7937239c2a6c2a6b4d76f71b96743589"></a>

```c
/*
 * Copyright (c) 2024 Abhinav Srivastava
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_STROPTS_H_
#define ZEPHYR_INCLUDE_POSIX_STROPTS_H_
#define RS_HIPRI BIT(0)

#ifdef __cplusplus
extern "C" {
#endif

struct strbuf {
        int maxlen;
        int len;
        char *buf;
};

int putmsg(int fildes, const struct strbuf *ctlptr, const struct strbuf *dataptr, int flags);
int fdetach(const char *path);
int fattach(int fildes, const char *path);
int getmsg(int fildes, struct strbuf *ctlptr, struct strbuf *dataptr, int *flagsp);
int getpmsg(int fildes, struct strbuf *ctlptr, struct strbuf *dataptr, int *bandp, int *flagsp);
int isastream(int fildes);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_STROPTS_H_ */
```

## 841.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Abhinav Srivastava。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_STROPTS_H_`。

## 841.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html)
- [strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)
- [maxlen](../posix_system_model_reference/P023_strbuf_结构体.md#a7937239c2a6c2a6b4d76f71b96743589)
- [len](../posix_system_model_reference/P023_strbuf_结构体.md#a2ce53f2d390a31cdabe5299c73e489b0)
- [buf](../posix_system_model_reference/P023_strbuf_结构体.md#a421c67aa5a9400a826e8e274f1ffb900)
- [putmsg](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#a2e8c9b125d5b2b9e9c0f119bb8489c5e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [fdetach](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#ace3f43f93319016fce6e1ce8bb135ee2)
- [fattach](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#aad1d52cad379cd124cbed912aa636ad1)
- [getmsg](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#a49857bef3fb1cecd099e67c8df35c8ef)
- [getpmsg](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#a55b37250892d8a0821df369a5f744099)
- [isastream](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html#add5237bf6844593ab11f8daa15d16070)
- [strbuf::len](../posix_system_model_reference/P023_strbuf_结构体.md#a2ce53f2d390a31cdabe5299c73e489b0)
- [strbuf::buf](../posix_system_model_reference/P023_strbuf_结构体.md#a421c67aa5a9400a826e8e274f1ffb900)
- [strbuf::maxlen](../posix_system_model_reference/P023_strbuf_结构体.md#a7937239c2a6c2a6b4d76f71b96743589)

---

[上一章](P840_store.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P842_stts22h.h_源码浏览.md)
