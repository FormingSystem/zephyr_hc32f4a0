---
id: learning.zephyr-docs.api-source-reference.page-164
title: mipi_dbi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第164章\_mipi\_dbi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h.html)。

## 164.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="foldopen00157"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00176"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00242"></a>
<a id="l00246"></a>
<a id="l00250"></a>
<a id="l00254"></a>
<a id="l00258"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00267"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="foldopen00318"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="foldopen00350"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00439"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2display_8h_html"></a>
<a id="adrivers_2spi_8h_html"></a>
<a id="adt-bindings_2mipi__dbi_2mipi__dbi_8h_html"></a>
<a id="agroup__clock__apis_html_ga302af954e87b10a9b731f1ad07775e9f"></a>
<a id="agroup__clock__apis_html_ga91198e325210ec052a8308e642058c0b"></a>
<a id="agroup__display__interface_html_gac346bc56771052a8fe919c3ec23d7c9c"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__mipi__dbi__interface__backend_html_ga12f0446626ab4feb996f33fcea4129dd"></a>
<a id="agroup__mipi__dbi__interface__backend_html_ga2000c1dc2ac1efe0eb6179a18da1e5c2"></a>
<a id="agroup__mipi__dbi__interface__backend_html_ga37ac264a3130d34a8d594c7482b09870"></a>
<a id="agroup__mipi__dbi__interface__backend_html_ga3ea6251e2fe3a18c8daba66c4ded41d6"></a>
<a id="agroup__mipi__dbi__interface__backend_html_ga7c6f09c6fece9c343aa4717150ca170e"></a>
<a id="agroup__mipi__dbi__interface__backend_html_gad973c1d30050ea3b6c3f9e1032e5383c"></a>
<a id="agroup__mipi__dbi__interface_html_ga1c1a117ae5db5f7508f302d48dc72013"></a>
<a id="agroup__mipi__dbi__interface_html_ga62aa7b9677da010a678580d956f7d0e3"></a>
<a id="agroup__mipi__dbi__interface_html_gab74f96d99f9702f29b51cc2fe0b48d95"></a>
<a id="agroup__mipi__dbi__interface_html_gad36e3d57fd931236c4ed4e58dfef1cca"></a>
<a id="agroup__mipi__dbi__interface_html_gade0b635bcd4f16fb3ec5d122d1b09161"></a>
<a id="agroup__mipi__dbi__interface_html_gafac64feca9fdee3803154bacb58e8e47"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="amipi__display_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdisplay__buffer__descriptor_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmipi__dbi__config_html"></a>
<a id="astructmipi__dbi__config_html_a2eafaaa6cda8f17f4b518c007bb3a7c3"></a>
<a id="astructmipi__dbi__config_html_a50d0893838455e3b8faa29d6459bc9c8"></a>
<a id="astructmipi__dbi__config_html_ab8182314f21f49de880b4b78ccf8a0aa"></a>
<a id="astructmipi__dbi__driver__api_html"></a>
<a id="astructmipi__dbi__driver__api_html_a33702cb0358588ffebeb11bd97b287c5"></a>
<a id="astructmipi__dbi__driver__api_html_a62eb8d9e45d888a9db25e0a44374e098"></a>
<a id="astructmipi__dbi__driver__api_html_a74275012d87749477c7c05a437b0a8d4"></a>
<a id="astructmipi__dbi__driver__api_html_a8987136f1e4f903cb0177fe9b16094d3"></a>
<a id="astructmipi__dbi__driver__api_html_aa615fbe9f882fd10d967c4693bb7664f"></a>
<a id="astructmipi__dbi__driver__api_html_ab53ff7394b4b56128fd17e2a0bfa2045"></a>
<a id="astructspi__config_html"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MIPI_DBI_H_
#define ZEPHYR_INCLUDE_DRIVERS_MIPI_DBI_H_


#include <zephyr/device.h>
#include <zephyr/drivers/display.h>
#include <zephyr/display/mipi_display.h>
#include <zephyr/drivers/spi.h>
#include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MIPI_DBI_DT_SPI_DEV(node_id)                                    \
        DT_PHANDLE(DT_PARENT(node_id), spi_dev)

#define MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id)                          \
        DT_PROP_HAS_IDX(MIPI_DBI_DT_SPI_DEV(node_id), cs_gpios,         \
                        DT_REG_ADDR_RAW(node_id))

#define MIPI_DBI_SPI_CS_GPIOS_DT_SPEC_GET(node_id)                      \
        GPIO_DT_SPEC_GET_BY_IDX_OR(MIPI_DBI_DT_SPI_DEV(node_id),        \
                cs_gpios, DT_REG_ADDR_RAW(node_id), {})

#define MIPI_DBI_SPI_CS_CONTROL_INIT_GPIO(node_id, delay_)              \
        .gpio = MIPI_DBI_SPI_CS_GPIOS_DT_SPEC_GET(node_id),             \
        .delay = delay_,

#define MIPI_DBI_SPI_CONFIG_DT(node_id, operation_, delay_)             \
        {                                                               \
                .frequency = DT_PROP(node_id, mipi_max_frequency),      \
                .operation = (operation_) |                             \
                        DT_PROP_OR(node_id, duplex, 0) |                        \
                        COND_CODE_1(DT_PROP(node_id, mipi_cpol), SPI_MODE_CPOL, (0)) |  \
                        COND_CODE_1(DT_PROP(node_id, mipi_cpha), SPI_MODE_CPHA, (0)) |  \
                        COND_CODE_1(DT_PROP(node_id, mipi_hold_cs), SPI_HOLD_ON_CS, (0)),       \
                .peripheral = DT_REG_ADDR(node_id),                             \
                .cs = {                                                                 \
                        COND_CODE_1(MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id),                     \
                        (MIPI_DBI_SPI_CS_CONTROL_INIT_GPIO(node_id, delay_)),           \
                        (SPI_CS_CONTROL_INIT_NATIVE(node_id)))                          \
                        .cs_is_gpio = MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id),           \
                },                                                                      \
        }

#define MIPI_DBI_SPI_CONFIG_DT_INST(inst, operation_, delay_)           \
        MIPI_DBI_SPI_CONFIG_DT(DT_DRV_INST(inst), operation_, delay_)

#define MIPI_DBI_CONFIG_DT(node_id, operation_, delay_)                 \
        {                                                               \
                .mode = DT_STRING_UPPER_TOKEN(node_id, mipi_mode),      \
                .color_coding = DT_STRING_UPPER_TOKEN_OR(node_id, color_coding, 0), \
                .config = MIPI_DBI_SPI_CONFIG_DT(node_id, operation_, delay_), \
        }

#define MIPI_DBI_CONFIG_DT_INST(inst, operation_, delay_)               \
        MIPI_DBI_CONFIG_DT(DT_DRV_INST(inst), operation_, delay_)

#define MIPI_DBI_TE_MODE_DT(node_id, edge_prop)                           \
        DT_STRING_UPPER_TOKEN(node_id, edge_prop)

#define MIPI_DBI_TE_MODE_DT_INST(inst, edge_prop)                         \
        DT_STRING_UPPER_TOKEN(DT_DRV_INST(inst), edge_prop)


struct mipi_dbi_config {
        uint8_t mode;
        uint8_t color_coding;
        struct spi_config config;
};

typedef int (*mipi_dbi_command_write_t)(const struct device *dev,
                                        const struct mipi_dbi_config *config, uint8_t cmd,
                                        const uint8_t *data, size_t len);

typedef int (*mipi_dbi_command_read_t)(const struct device *dev,
                                       const struct mipi_dbi_config *config, uint8_t *cmds,
                                       size_t num_cmds, uint8_t *response, size_t len);

typedef int (*mipi_dbi_write_display_t)(const struct device *dev,
                                        const struct mipi_dbi_config *config,
                                        const uint8_t *framebuf,
                                        struct display_buffer_descriptor *desc,
                                        enum display_pixel_format pixfmt);

typedef int (*mipi_dbi_reset_t)(const struct device *dev, k_timeout_t delay);

typedef int (*mipi_dbi_release_t)(const struct device *dev, const struct mipi_dbi_config *config);

typedef int (*mipi_dbi_configure_te_t)(const struct device *dev, uint8_t edge, k_timeout_t delay);

__subsystem struct mipi_dbi_driver_api {
        mipi_dbi_command_write_t command_write;
        mipi_dbi_command_read_t command_read;
        mipi_dbi_write_display_t write_display;
        mipi_dbi_reset_t reset;
        mipi_dbi_release_t release;
        mipi_dbi_configure_te_t configure_te;
};


static inline int mipi_dbi_command_write(const struct device *dev,
                                         const struct mipi_dbi_config *config,
                                         uint8_t cmd, const uint8_t *data,
                                         size_t len)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->command_write == NULL) {
                return -ENOSYS;
        }
        return api->command_write(dev, config, cmd, data, len);
}

static inline int mipi_dbi_command_read(const struct device *dev,
                                        const struct mipi_dbi_config *config,
                                        uint8_t *cmds, size_t num_cmd,
                                        uint8_t *response, size_t len)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->command_read == NULL) {
                return -ENOSYS;
        }
        return api->command_read(dev, config, cmds, num_cmd, response, len);
}

static inline int mipi_dbi_write_display(const struct device *dev,
                                         const struct mipi_dbi_config *config,
                                         const uint8_t *framebuf,
                                         struct display_buffer_descriptor *desc,
                                         enum display_pixel_format pixfmt)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->write_display == NULL) {
                return -ENOSYS;
        }
        return api->write_display(dev, config, framebuf, desc, pixfmt);
}

static inline int mipi_dbi_reset(const struct device *dev, uint32_t delay_ms)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->reset == NULL) {
                return -ENOSYS;
        }
        return api->reset(dev, K_MSEC(delay_ms));
}

static inline int mipi_dbi_release(const struct device *dev,
                                   const struct mipi_dbi_config *config)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->release == NULL) {
                return -ENOSYS;
        }
        return api->release(dev, config);
}

static inline int mipi_dbi_configure_te(const struct device *dev,
                                        uint8_t edge,
                                        uint32_t delay_us)
{
        const struct mipi_dbi_driver_api *api = DEVICE_API_GET(mipi_dbi, dev);

        if (api->configure_te == NULL) {
                return -ENOSYS;
        }
        return api->configure_te(dev, edge, K_USEC(delay_us));
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MIPI_DBI_H_ */
```

## 164.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 459 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MIPI_DBI_H_`。

## 164.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dbi_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [zephyr/display/mipi_display.h](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)
- [zephyr/drivers/spi.h](../spi_driver_reference/P001_SPI驱动头文件参考.md)
- [zephyr/dt-bindings/mipi_dbi/mipi_dbi.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html)
- [mipi_dbi_config](../hardware/P247_MIPI显示总线配置.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mode](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a2eafaaa6cda8f17f4b518c007bb3a7c3)
- [color_coding](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#ab8182314f21f49de880b4b78ccf8a0aa)
- [spi_config](../hardware/P320_SPI控制器配置结构.md)
- [config](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a50d0893838455e3b8faa29d6459bc9c8)
- [mipi_dbi_command_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga3ea6251e2fe3a18c8daba66c4ded41d6)
- [device](../device_reference/P002_设备对象结构.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mipi_dbi_command_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga7c6f09c6fece9c343aa4717150ca170e)
- [mipi_dbi_write_display_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#gad973c1d30050ea3b6c3f9e1032e5383c)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [mipi_dbi_reset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga37ac264a3130d34a8d594c7482b09870)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mipi_dbi_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga12f0446626ab4feb996f33fcea4129dd)
- [mipi_dbi_configure_te_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga2000c1dc2ac1efe0eb6179a18da1e5c2)
- [mipi_dbi_driver_api](../hardware/P252_MIPI显示总线函数表.md)
- [command_write](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a62eb8d9e45d888a9db25e0a44374e098)
- [command_read](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a8987136f1e4f903cb0177fe9b16094d3)
- [write_display](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a33702cb0358588ffebeb11bd97b287c5)
- [reset](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a74275012d87749477c7c05a437b0a8d4)
- [release](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#ab53ff7394b4b56128fd17e2a0bfa2045)
- [configure_te](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#aa615fbe9f882fd10d967c4693bb7664f)
- [mipi_dbi_command_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [mipi_dbi_command_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafac64feca9fdee3803154bacb58e8e47)
- [mipi_dbi_write_display](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3)
- [mipi_dbi_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga1c1a117ae5db5f7508f302d48dc72013)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [K_MSEC](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)
- [mipi_dbi_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161)
- [mipi_dbi_configure_te](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab74f96d99f9702f29b51cc2fe0b48d95)
- [K_USEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga91198e325210ec052a8308e642058c0b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [display.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [spi.h](../spi_driver_reference/P001_SPI驱动头文件参考.md)
- [mipi_dbi.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html)
- [mipi_display.h](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)
- [mipi_dbi_config::mode](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a2eafaaa6cda8f17f4b518c007bb3a7c3)
- [mipi_dbi_config::config](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a50d0893838455e3b8faa29d6459bc9c8)
- [mipi_dbi_config::color_coding](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#ab8182314f21f49de880b4b78ccf8a0aa)
- [mipi_dbi_driver_api::write_display](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a33702cb0358588ffebeb11bd97b287c5)
- [mipi_dbi_driver_api::command_write](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a62eb8d9e45d888a9db25e0a44374e098)
- [mipi_dbi_driver_api::reset](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a74275012d87749477c7c05a437b0a8d4)
- [mipi_dbi_driver_api::command_read](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a8987136f1e4f903cb0177fe9b16094d3)
- [mipi_dbi_driver_api::configure_te](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#aa615fbe9f882fd10d967c4693bb7664f)
- [mipi_dbi_driver_api::release](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#ab53ff7394b4b56128fd17e2a0bfa2045)

---

[上一章](P163_npm2100.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P165_nxp_rtxxx_dsp_ctrl.h_源码浏览.md)
