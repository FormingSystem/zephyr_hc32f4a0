---
id: learning.zephyr-docs.api-source-supplement-reference.page-83
title: grow_r502a.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_grow\_r502a.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h.html)。

## 83.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00142"></a>
<a id="l00147"></a>
<a id="l00153"></a>
<a id="l00159"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00175"></a>
<a id="l00182"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="agroup__grow__r502a__interface_html_ga16242f27a53b430ea3cf165fbc7ce70b"></a>
<a id="agroup__grow__r502a__interface_html_ga3298eb4d591ba56131bae8137888dcd8"></a>
<a id="agroup__grow__r502a__interface_html_ga3b6f1ea1024c0d855a7bbf05f79c19c8"></a>
<a id="agroup__grow__r502a__interface_html_ga3dbc5cd5f5295741e99735ec0279b48d"></a>
<a id="agroup__grow__r502a__interface_html_ga48154de53541aced1e78537f10f2f3d1"></a>
<a id="agroup__grow__r502a__interface_html_ga638da7a83d9339b17e5d9c8ce92b684b"></a>
<a id="agroup__grow__r502a__interface_html_ga721dcba985d9010bb1f48e82b0027eb4"></a>
<a id="agroup__grow__r502a__interface_html_ga843fa88a16ab6b47c4e517ddbc01b4a8"></a>
<a id="agroup__grow__r502a__interface_html_ga8ff24814059dda20e6b36fe8cc0be30c"></a>
<a id="agroup__grow__r502a__interface_html_gad16b787e54f20627c4bf15b1732c05ae"></a>
<a id="agroup__grow__r502a__interface_html_gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519"></a>
<a id="agroup__grow__r502a__interface_html_gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1"></a>
<a id="agroup__grow__r502a__interface_html_gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721"></a>
<a id="agroup__grow__r502a__interface_html_gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101"></a>
<a id="agroup__grow__r502a__interface_html_gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee"></a>
<a id="agroup__grow__r502a__interface_html_gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf"></a>
<a id="agroup__grow__r502a__interface_html_gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe"></a>
<a id="agroup__grow__r502a__interface_html_gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9"></a>
<a id="agroup__grow__r502a__interface_html_gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7"></a>
<a id="agroup__grow__r502a__interface_html_gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef"></a>
<a id="agroup__grow__r502a__interface_html_gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1"></a>
<a id="agroup__grow__r502a__interface_html_gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b"></a>
<a id="agroup__grow__r502a__interface_html_gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922"></a>
<a id="agroup__grow__r502a__interface_html_gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4"></a>
<a id="agroup__grow__r502a__interface_html_gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845"></a>
<a id="agroup__grow__r502a__interface_html_gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c"></a>
<a id="agroup__grow__r502a__interface_html_gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c"></a>
<a id="agroup__grow__r502a__interface_html_gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructr502a__sys__param_html"></a>
<a id="astructr502a__sys__param_html_a076a36d66a6908eee2131a8f652fefa4"></a>
<a id="astructr502a__sys__param_html_a4cc85b5b8ec7a511f9fc5dd3912c0a39"></a>
<a id="astructr502a__sys__param_html_a8c3470762665d940a3ec2dc214150bf8"></a>
<a id="astructr502a__sys__param_html_aaa11e04312322afa3f406f872763d8be"></a>
<a id="astructr502a__sys__param_html_ac3f2dc2456a29eeda55417ba91a29f62"></a>
<a id="astructr502a__sys__param_html_adb966712020f826ecc646c04a93edd5f"></a>
<a id="astructr502a__sys__param_html_adf5a91c5972af06d1bf9beb6a9040bac"></a>
<a id="astructr502a__template_html"></a>
<a id="astructr502a__template_html_a2d4ab0b0ea4e4cf8b061705910639ae4"></a>
<a id="astructr502a__template_html_aca6dc417fc7e1de22da94e4d4e2b96a9"></a>

```c
/*
 * Copyright (c) 2022 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_GROW_R502A_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_GROW_R502A_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

/*LED color code*/
enum r502a_led_color_idx {
        R502A_LED_COLOR_RED = 0x01,
        R502A_LED_COLOR_BLUE,
        R502A_LED_COLOR_PURPLE,
};


#define R502A_BAUD_9600   1
#define R502A_BAUD_19200  2
#define R502A_BAUD_38400  4
#define R502A_BAUD_57600  6
#define R502A_BAUD_115200 12


enum r502a_sec_level {
        R502A_SEC_LEVEL_1 = 1,
        R502A_SEC_LEVEL_2,
        R502A_SEC_LEVEL_3,
        R502A_SEC_LEVEL_4,
        R502A_SEC_LEVEL_5
};

enum r502a_data_len {
        R502A_PKG_LEN_32,
        R502A_PKG_LEN_64,
        R502A_PKG_LEN_128,
        R502A_PKG_LEN_256
};

enum r502a_sys_param_set {
        R502A_BAUD_RATE = 4,
        R502A_SECURITY_LEVEL,
        R502A_DATA_PKG_LEN
};

struct r502a_sys_param {
        uint16_t status_reg;
        uint16_t system_id;
        uint16_t lib_size;
        uint16_t sec_level;
        uint32_t addr;
        uint16_t data_pkt_size;
        uint32_t baud;
} __packed;

struct r502a_template {
        uint8_t *data;
        size_t len;
};

enum sensor_channel_grow_r502a {
        SENSOR_CHAN_FINGERPRINT = SENSOR_CHAN_PRIV_START,
};

enum sensor_trigger_type_grow_r502a {
        SENSOR_TRIG_TOUCH = SENSOR_TRIG_PRIV_START,
};

enum sensor_attribute_grow_r502a {
        SENSOR_ATTR_R502A_CAPTURE = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_R502A_TEMPLATE_CREATE,
        SENSOR_ATTR_R502A_RECORD_ADD,
        SENSOR_ATTR_R502A_RECORD_FIND,
        SENSOR_ATTR_R502A_RECORD_DEL,
        SENSOR_ATTR_R502A_RECORD_FREE_IDX,
        SENSOR_ATTR_R502A_RECORD_EMPTY,
        SENSOR_ATTR_R502A_RECORD_LOAD,
        SENSOR_ATTR_R502A_COMPARE,
        SENSOR_ATTR_R502A_SYS_PARAM,
};

int r502a_read_sys_param(const struct device *dev, struct r502a_sys_param *val);

int fps_upload_char_buf(const struct device *dev, struct r502a_template *temp);

int fps_download_char_buf(const struct device *dev, uint8_t char_buf_id,
                                const struct r502a_template *temp);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_SENSOR_GROW_R502A_H_ */
```

## 83.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

LED 颜色代码（Color code）。

### 注释 3：原第 237 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_SENSOR_GROW_R502A_H_`。

## 83.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [r502a_led_color_idx](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga843fa88a16ab6b47c4e517ddbc01b4a8)
- [R502A_LED_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c)
- [R502A_LED_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845)
- [R502A_LED_COLOR_PURPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c)
- [r502a_sec_level](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga48154de53541aced1e78537f10f2f3d1)
- [R502A_SEC_LEVEL_1](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7)
- [R502A_SEC_LEVEL_2](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef)
- [R502A_SEC_LEVEL_3](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa)
- [R502A_SEC_LEVEL_4](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9)
- [R502A_SEC_LEVEL_5](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)
- [r502a_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3298eb4d591ba56131bae8137888dcd8)
- [R502A_PKG_LEN_32](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf)
- [R502A_PKG_LEN_64](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee)
- [R502A_PKG_LEN_128](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe)
- [R502A_PKG_LEN_256](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)
- [r502a_sys_param_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga16242f27a53b430ea3cf165fbc7ce70b)
- [R502A_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721)
- [R502A_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519)
- [R502A_DATA_PKG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)
- [r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [status_reg](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#adb966712020f826ecc646c04a93edd5f)
- [system_id](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#aaa11e04312322afa3f406f872763d8be)
- [lib_size](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a4cc85b5b8ec7a511f9fc5dd3912c0a39)
- [sec_level](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a076a36d66a6908eee2131a8f652fefa4)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [addr](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#ac3f2dc2456a29eeda55417ba91a29f62)
- [data_pkt_size](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a8c3470762665d940a3ec2dc214150bf8)
- [baud](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#adf5a91c5972af06d1bf9beb6a9040bac)
- [r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../sensor_navigation_model_reference/P023_r502a_template_结构体.md#aca6dc417fc7e1de22da94e4d4e2b96a9)
- [len](../sensor_navigation_model_reference/P023_r502a_template_结构体.md#a2d4ab0b0ea4e4cf8b061705910639ae4)
- [sensor_channel_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga8ff24814059dda20e6b36fe8cc0be30c)
- [SENSOR_CHAN_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor_trigger_type_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga721dcba985d9010bb1f48e82b0027eb4)
- [SENSOR_TRIG_TOUCH](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)
- [SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)
- [sensor_attribute_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga638da7a83d9339b17e5d9c8ce92b684b)
- [SENSOR_ATTR_R502A_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_R502A_TEMPLATE_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965)
- [SENSOR_ATTR_R502A_RECORD_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)
- [SENSOR_ATTR_R502A_RECORD_FIND](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)
- [SENSOR_ATTR_R502A_RECORD_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)
- [SENSOR_ATTR_R502A_RECORD_FREE_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)
- [SENSOR_ATTR_R502A_RECORD_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)
- [SENSOR_ATTR_R502A_RECORD_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13)
- [SENSOR_ATTR_R502A_COMPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689)
- [SENSOR_ATTR_R502A_SYS_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)
- [r502a_read_sys_param](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3dbc5cd5f5295741e99735ec0279b48d)
- [device](../device_reference/P002_设备对象结构.md)
- [fps_upload_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gad16b787e54f20627c4bf15b1732c05ae)
- [fps_download_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3b6f1ea1024c0d855a7bbf05f79c19c8)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [r502a_sys_param::sec_level](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a076a36d66a6908eee2131a8f652fefa4)
- [r502a_sys_param::lib_size](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a4cc85b5b8ec7a511f9fc5dd3912c0a39)
- [r502a_sys_param::data_pkt_size](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#a8c3470762665d940a3ec2dc214150bf8)
- [r502a_sys_param::system_id](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#aaa11e04312322afa3f406f872763d8be)
- [r502a_sys_param::addr](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#ac3f2dc2456a29eeda55417ba91a29f62)
- [r502a_sys_param::status_reg](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#adb966712020f826ecc646c04a93edd5f)
- [r502a_sys_param::baud](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md#adf5a91c5972af06d1bf9beb6a9040bac)
- [r502a_template::len](../sensor_navigation_model_reference/P023_r502a_template_结构体.md#a2d4ab0b0ea4e4cf8b061705910639ae4)
- [r502a_template::data](../sensor_navigation_model_reference/P023_r502a_template_结构体.md#aca6dc417fc7e1de22da94e4d4e2b96a9)

---

[上一章](P082_gpio_rts5912.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P084_handlers.h_源码浏览.md)
