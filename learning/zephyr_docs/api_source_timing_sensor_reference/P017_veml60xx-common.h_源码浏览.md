---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-17
title: veml60xx-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_veml60xx-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_runtime_reference/P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md)。

## 17.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00050"></a>
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
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="agroup__veml60xx__interface_html_ga030b4553bb1982a3f470dcfe70a74636"></a>
<a id="agroup__veml60xx__interface_html_ga2635095ab9ddf8ffd8e25cbaf08b824a"></a>
<a id="agroup__veml60xx__interface_html_ga8945da51940f67ee875a729d6de4d287"></a>
<a id="agroup__veml60xx__interface_html_ga95d24f44c42ba4d71df013ace6c6d613"></a>
<a id="agroup__veml60xx__interface_html_gaba51cd71795a34af85d21da10cba5b44"></a>
<a id="agroup__veml60xx__interface_html_gacb2554bb01df63048cdcc1894903dd73"></a>
<a id="agroup__veml60xx__interface_html_gacf7907b21bea0f35196db039a709aae2"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b"></a>
<a id="agroup__veml60xx__interface_html_ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393"></a>
<a id="agroup__veml60xx__interface_html_ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4"></a>
<a id="agroup__veml60xx__interface_html_ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1"></a>
<a id="agroup__veml60xx__interface_html_ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da"></a>
<a id="agroup__veml60xx__interface_html_ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4"></a>
<a id="agroup__veml60xx__interface_html_ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5"></a>
<a id="agroup__veml60xx__interface_html_ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b"></a>
<a id="agroup__veml60xx__interface_html_ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructveml60xx__it__data_html"></a>
<a id="astructveml60xx__it__data_html_a42abdd5563a01c9ab95ac2ee0afea321"></a>
<a id="astructveml60xx__it__data_html_a6c835a175515f03a765b25dcee4051d7"></a>
<a id="astructveml60xx__it__data_html_a72d593a2de62dde61d5068401c5b781c"></a>

```c
/*
 * Copyright (c) 2025 Andreas Klinger
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML60XX_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML60XX_COMMON_H_


#ifdef __cplusplus
extern "C" {
#endif

enum veml60xx_it {
        VEML60XX_IT_3_125,
        VEML60XX_IT_6_25,
        VEML60XX_IT_12_5,
        VEML60XX_IT_25,
        VEML60XX_IT_50,
        VEML60XX_IT_100,
        VEML60XX_IT_200,
        VEML60XX_IT_400,
        VEML60XX_IT_COUNT,
};

/*
 * @brief VEML60xx integration time struct.
 */
struct veml60xx_it_data {
        enum veml60xx_it num;
        uint8_t val;
        int us;
};

/*
 * @brief VEML60xx integration time setting values.
 *
 * The enumerators of enum veml60xx_it provide indices into this array to get
 * the related value for the ALS_IT configuration bits.
 */
static const struct veml60xx_it_data veml60xx_it_values[VEML60XX_IT_COUNT] = {
        {VEML60XX_IT_3_125, 0x00, 3125}, /*   3.125 - 0b0000 */
        {VEML60XX_IT_6_25, 0x01, 6250},  /*   6.25  - 0b0001 */
        {VEML60XX_IT_12_5, 0x02, 12500}, /*  12.5   - 0b0010 */
        {VEML60XX_IT_25, 0x03, 25000},   /*  25     - 0b0011 */
        {VEML60XX_IT_50, 0x04, 50000},   /*  50     - 0b0100 */
        {VEML60XX_IT_100, 0x05, 100000}, /* 100     - 0b0101 */
        {VEML60XX_IT_200, 0x06, 200000}, /* 200     - 0b0110 */
        {VEML60XX_IT_400, 0x07, 400000}, /* 400     - 0b0111 */
};

enum veml60xx_gain {
        VEML60XX_GAIN_1 = 0x00,
        VEML60XX_GAIN_2 = 0x01,
        VEML60XX_GAIN_0_66 = 0x02,
        VEML60XX_GAIN_0_5 = 0x03,
        VEML60XX_GAIN_COUNT = 4,
};

enum veml60xx_pers {
        VEML60XX_PERS_1 = 0x00,
        VEML60XX_PERS_2 = 0x01,
        VEML60XX_PERS_4 = 0x02,
        VEML60XX_PERS_8 = 0x03,
};


static inline bool veml60xx_gain_in_range(int32_t gain)
{
        return (gain >= VEML60XX_GAIN_1) && (gain <= VEML60XX_GAIN_0_5);
}

static inline bool veml60xx_it_in_range(int32_t it)
{
        return (it >= VEML60XX_IT_3_125) && (it <= VEML60XX_IT_400);
}

static inline bool veml60xx_pers_in_range(int32_t pers)
{
        return (pers >= VEML60XX_PERS_1) && (pers <= VEML60XX_PERS_8);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML60XX_COMMON_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Andreas Klinger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

@brief VEML60xx 积分时间（integration time）结构体。

### 注释 3：原第 56 行

@brief VEML60xx 积分时间（integration time）设置值。

`enum veml60xx_it` 中的枚举值用作此数组的索引，以获取 `ALS_IT` 配置位对应的值。

### 注释 4：原第 63 行

积分时间与编码：`3.125 - 0b0000`。

### 注释 5：原第 64 行

积分时间与编码：`6.25 - 0b0001`。

### 注释 6：原第 65 行

积分时间与编码：`12.5 - 0b0010`。

### 注释 7：原第 66 行

积分时间与编码：`25 - 0b0011`。

### 注释 8：原第 67 行

积分时间与编码：`50 - 0b0100`。

### 注释 9：原第 68 行

积分时间与编码：`100 - 0b0101`。

### 注释 10：原第 69 行

积分时间与编码：`200 - 0b0110`。

### 注释 11：原第 70 行

积分时间与编码：`400 - 0b0111`。

### 注释 12：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML60XX_COMMON_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_runtime_reference/P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md)
- [veml60xx_it](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga8945da51940f67ee875a729d6de4d287)
- [VEML60XX_IT_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965)
- [VEML60XX_IT_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888)
- [VEML60XX_IT_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa)
- [VEML60XX_IT_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144)
- [VEML60XX_IT_50](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77)
- [VEML60XX_IT_100](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636)
- [VEML60XX_IT_200](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b)
- [VEML60XX_IT_400](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93)
- [veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)
- [num](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a72d593a2de62dde61d5068401c5b781c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [val](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a42abdd5563a01c9ab95ac2ee0afea321)
- [us](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a6c835a175515f03a765b25dcee4051d7)
- [veml60xx_it_values](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga95d24f44c42ba4d71df013ace6c6d613)
- [veml60xx_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacf7907b21bea0f35196db039a709aae2)
- [VEML60XX_GAIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b)
- [VEML60XX_GAIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5)
- [VEML60XX_GAIN_0_66](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f)
- [VEML60XX_GAIN_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4)
- [veml60xx_pers](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacb2554bb01df63048cdcc1894903dd73)
- [VEML60XX_PERS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1)
- [VEML60XX_PERS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da)
- [VEML60XX_PERS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393)
- [VEML60XX_PERS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4)
- [veml60xx_gain_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gaba51cd71795a34af85d21da10cba5b44)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [veml60xx_it_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga2635095ab9ddf8ffd8e25cbaf08b824a)
- [veml60xx_pers_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga030b4553bb1982a3f470dcfe70a74636)
- [veml60xx_it_data::val](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a42abdd5563a01c9ab95ac2ee0afea321)
- [veml60xx_it_data::us](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a6c835a175515f03a765b25dcee4051d7)
- [veml60xx_it_data::num](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md#a72d593a2de62dde61d5068401c5b781c)

---

[上一章](P016_uart_async_rx.h_源码浏览.md) · [返回大纲](大纲.md)
