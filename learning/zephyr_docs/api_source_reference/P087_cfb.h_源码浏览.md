---
id: learning.zephyr-docs.api-source-reference.page-87
title: cfb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_cfb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h.html)。

## 87.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
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
<a id="l00031"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2display_8h_html"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga029d0f320157e6b2936bb9f0794024d6"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga02dbf9751af0ee01e20a293b94fcfb7a"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga0b26cd0d9e2de71f754f85849ccba001"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga29343c61a7a9e28c50cb384ba4f383cf"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga2a87d5fd58bb7a56081668313f7038f6"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga2bbe913d7f0a10b4ba543d83ef6fac95"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga32e8edb517093dbc1b612a1bef24c7af"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga496b3b161fa0bc2e42e3d5de83c4f544"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga5ef3b84b6169eaef398cf47b3583c827"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga63ea5f559391ed735da8afa78745e458"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga81af74d2831d5a4fc1338da693401958"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga8e86d48a0c6d951de34089f5d6cf5fb1"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga981f062bb314c107230e068f575f81ef"></a>
<a id="agroup__monochrome__character__framebuffer_html_ga9d0b3f63c2b52458ab040993b3c3b97d"></a>
<a id="agroup__monochrome__character__framebuffer_html_gac0918644cb24a39ef578e54acac46d64"></a>
<a id="agroup__monochrome__character__framebuffer_html_gac9a957b5dd6e99377d9c070085df3252"></a>
<a id="agroup__monochrome__character__framebuffer_html_gae1943e8d138f5e612f6508dd0f510134"></a>
<a id="agroup__monochrome__character__framebuffer_html_gae98337479a5339d4171797e96313fee5"></a>
<a id="agroup__monochrome__character__framebuffer_html_gaeb46dfb72c31474c1acbc46d2f08803e"></a>
<a id="agroup__monochrome__character__framebuffer_html_gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630"></a>
<a id="agroup__monochrome__character__framebuffer_html_gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c"></a>
<a id="agroup__monochrome__character__framebuffer_html_gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f"></a>
<a id="agroup__monochrome__character__framebuffer_html_gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a"></a>
<a id="agroup__monochrome__character__framebuffer_html_gga32e8edb517093dbc1b612a1bef24c7afaf5bdbd92f8d454caa8d8e2ddf484aaba"></a>
<a id="agroup__monochrome__character__framebuffer_html_ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c"></a>
<a id="agroup__monochrome__character__framebuffer_html_ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6"></a>
<a id="agroup__monochrome__character__framebuffer_html_ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructcfb__font_html"></a>
<a id="astructcfb__font_html_a204e414d8b0add418fb92914402d14e2"></a>
<a id="astructcfb__font_html_a4ac3e8578e577909058fdcd8bce62f3b"></a>
<a id="astructcfb__font_html_a79ca54ef1b7928c9bde7bc4d730aa417"></a>
<a id="astructcfb__font_html_ab58695cca74151c86f442366bd80a039"></a>
<a id="astructcfb__font_html_abe8771187455817e8085a42820079aea"></a>
<a id="astructcfb__font_html_ad50168c069d5cda8e924ba336875ef85"></a>
<a id="astructcfb__position_html"></a>
<a id="astructcfb__position_html_a0d2f18bfdd4b4e1e6f2538e0f3084fd6"></a>
<a id="astructcfb__position_html_ab18cfc5749666113659c5703e68ea61a"></a>
<a id="astructdevice_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2018 PHYTEC Messtechnik GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DISPLAY_CFB_H_
#define ZEPHYR_INCLUDE_DISPLAY_CFB_H_

#include <zephyr/device.h>
#include <zephyr/drivers/display.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


enum cfb_display_param {
        CFB_DISPLAY_HEIGHT              = 0,
        CFB_DISPLAY_WIDTH,
        CFB_DISPLAY_PPT,
        CFB_DISPLAY_ROWS,
        CFB_DISPLAY_COLS,
};

enum cfb_font_caps {
        CFB_FONT_MONO_VPACKED           = BIT(0),
        CFB_FONT_MONO_HPACKED           = BIT(1),
        CFB_FONT_MSB_FIRST              = BIT(2),
};

struct cfb_font {
        const void *data;
        enum cfb_font_caps caps;
        uint8_t width;
        uint8_t height;
        uint8_t first_char;
        uint8_t last_char;
};

struct cfb_position {
        int16_t x;
        int16_t y;
};

#define FONT_ENTRY_DEFINE(_name, _width, _height, _caps, _data, _fc, _lc)      \
        static const STRUCT_SECTION_ITERABLE(cfb_font, _name) = {              \
                .data = _data,                                                 \
                .caps = _caps,                                                 \
                .width = _width,                                               \
                .height = _height,                                             \
                .first_char = _fc,                                             \
                .last_char = _lc,                                              \
        }

int cfb_print(const struct device *dev, const char *const str, int16_t x, int16_t y);

int cfb_draw_text(const struct device *dev, const char *const str, int16_t x, int16_t y);

int cfb_draw_point(const struct device *dev, const struct cfb_position *pos);

int cfb_draw_line(const struct device *dev, const struct cfb_position *start,
                  const struct cfb_position *end);

int cfb_draw_rect(const struct device *dev, const struct cfb_position *start,
                  const struct cfb_position *end);

int cfb_draw_circle(const struct device *dev, const struct cfb_position *start, uint16_t radius);

int cfb_framebuffer_clear(const struct device *dev, bool clear_display);

int cfb_framebuffer_invert(const struct device *dev);

int cfb_invert_area(const struct device *dev, int16_t x, int16_t y,
                    uint16_t width, uint16_t height);

int cfb_framebuffer_finalize(const struct device *dev);

int cfb_get_display_parameter(const struct device *dev,
                              enum cfb_display_param);

int cfb_framebuffer_set_font(const struct device *dev, uint8_t idx);

int cfb_set_kerning(const struct device *dev, int8_t kerning);

int cfb_get_font_size(const struct device *dev, uint8_t idx, uint8_t *width,
                      uint8_t *height);

int cfb_get_numof_fonts(const struct device *dev);

int cfb_framebuffer_init(const struct device *dev);

void cfb_framebuffer_deinit(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DISPLAY_CFB_H_ */
```

## 87.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 PHYTEC Messtechnik GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 274 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DISPLAY_CFB_H_`。

## 87.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [cfb_display_param](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga32e8edb517093dbc1b612a1bef24c7af)
- [CFB_DISPLAY_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afaf5bdbd92f8d454caa8d8e2ddf484aaba)
- [CFB_DISPLAY_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a)
- [CFB_DISPLAY_PPT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630)
- [CFB_DISPLAY_ROWS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c)
- [CFB_DISPLAY_COLS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)
- [cfb_font_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae98337479a5339d4171797e96313fee5)
- [CFB_FONT_MONO_VPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CFB_FONT_MONO_HPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c)
- [CFB_FONT_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b)
- [cfb_font](../hardware/P185_字符帧缓冲字体结构.md)
- [data](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#abe8771187455817e8085a42820079aea)
- [caps](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a4ac3e8578e577909058fdcd8bce62f3b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [width](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#ab58695cca74151c86f442366bd80a039)
- [height](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#ad50168c069d5cda8e924ba336875ef85)
- [first_char](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a204e414d8b0add418fb92914402d14e2)
- [last_char](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a79ca54ef1b7928c9bde7bc4d730aa417)
- [cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [x](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__position.html#a0d2f18bfdd4b4e1e6f2538e0f3084fd6)
- [y](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__position.html#ab18cfc5749666113659c5703e68ea61a)
- [cfb_print](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga029d0f320157e6b2936bb9f0794024d6)
- [device](../device_reference/P002_设备对象结构.md)
- [cfb_draw_text](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga496b3b161fa0bc2e42e3d5de83c4f544)
- [cfb_draw_point](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae1943e8d138f5e612f6508dd0f510134)
- [cfb_draw_line](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga81af74d2831d5a4fc1338da693401958)
- [cfb_draw_rect](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga0b26cd0d9e2de71f754f85849ccba001)
- [cfb_draw_circle](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2a87d5fd58bb7a56081668313f7038f6)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [cfb_framebuffer_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac9a957b5dd6e99377d9c070085df3252)
- [cfb_framebuffer_invert](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga8e86d48a0c6d951de34089f5d6cf5fb1)
- [cfb_invert_area](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga02dbf9751af0ee01e20a293b94fcfb7a)
- [cfb_framebuffer_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga9d0b3f63c2b52458ab040993b3c3b97d)
- [cfb_get_display_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gaeb46dfb72c31474c1acbc46d2f08803e)
- [cfb_framebuffer_set_font](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga29343c61a7a9e28c50cb384ba4f383cf)
- [cfb_set_kerning](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac0918644cb24a39ef578e54acac46d64)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [cfb_get_font_size](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga63ea5f559391ed735da8afa78745e458)
- [cfb_get_numof_fonts](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga5ef3b84b6169eaef398cf47b3583c827)
- [cfb_framebuffer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2bbe913d7f0a10b4ba543d83ef6fac95)
- [cfb_framebuffer_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga981f062bb314c107230e068f575f81ef)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [cfb_font::first_char](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a204e414d8b0add418fb92914402d14e2)
- [cfb_font::caps](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a4ac3e8578e577909058fdcd8bce62f3b)
- [cfb_font::last_char](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#a79ca54ef1b7928c9bde7bc4d730aa417)
- [cfb_font::width](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#ab58695cca74151c86f442366bd80a039)
- [cfb_font::data](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#abe8771187455817e8085a42820079aea)
- [cfb_font::height](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__font.html#ad50168c069d5cda8e924ba336875ef85)
- [cfb_position::x](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__position.html#a0d2f18bfdd4b4e1e6f2538e0f3084fd6)
- [cfb_position::y](https://docs.zephyrproject.org/latest/doxygen/html/structcfb__position.html#ab18cfc5749666113659c5703e68ea61a)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P086_cdefs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P088_cfg_cli.h_源码浏览.md)
