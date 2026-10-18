---
id: learning.zephyr-docs.api-source-supplement-reference.page-142
title: phy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/phy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_phy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html)。

## 142.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="foldopen00209"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00237"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="foldopen00307"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="foldopen00329"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00352"></a>
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
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
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
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="foldopen00429"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ethernet__phy_html_ga0ede85fdd6efd8c3520d7baf18d04a68"></a>
<a id="agroup__ethernet__phy_html_ga260e528dee1c967ccc9f4d9cb2aadad5"></a>
<a id="agroup__ethernet__phy_html_ga3ee3db4ac48395f07d0de536b313dfa4"></a>
<a id="agroup__ethernet__phy_html_ga3fcca53d29981e23426b43d5340d8651"></a>
<a id="agroup__ethernet__phy_html_ga492c16dd8b5f2708d9e702ce8906ffd3"></a>
<a id="agroup__ethernet__phy_html_ga4d073c152ad4b6f5745db4f6d8477345"></a>
<a id="agroup__ethernet__phy_html_ga4fa30627b96c9a1d02b43c8e799f2796"></a>
<a id="agroup__ethernet__phy_html_ga520c049d830051ffa48708bb0dea429f"></a>
<a id="agroup__ethernet__phy_html_ga6221da76ffca235eafa291b90eab0d93"></a>
<a id="agroup__ethernet__phy_html_ga9b97fff9fcd6823c9b564b3e86b8da68"></a>
<a id="agroup__ethernet__phy_html_gaaf47828adbc414304d871441217e772c"></a>
<a id="agroup__ethernet__phy_html_gaba1b0bda2a76a6d5db404d24ffec1aa5"></a>
<a id="agroup__ethernet__phy_html_gafce454d5da52532e4588324752c5cec3"></a>
<a id="agroup__ethernet__phy_html_gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga52d277cbf33f76350b2fcb21c24640ee"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructethphy__driver__api_html"></a>
<a id="astructethphy__driver__api_html_a1f56afd3cfc34b759c604b55c11c6214"></a>
<a id="astructethphy__driver__api_html_a1f66a4f770674baa32390c1f2e972694"></a>
<a id="astructethphy__driver__api_html_a307ea6c0541ab578d8ff7ccf2027e0df"></a>
<a id="astructethphy__driver__api_html_a4fd123655cd1dc8ca6c650cf76f3589f"></a>
<a id="astructethphy__driver__api_html_a5f5dc34c75601974ae4046300e6acf85"></a>
<a id="astructethphy__driver__api_html_a68af7c0c8d0e22243b745d09de1a5a47"></a>
<a id="astructethphy__driver__api_html_a9b48f6b3e38da454f658cbcbbd40398c"></a>
<a id="astructethphy__driver__api_html_aa205fb9e753f8a22118be14de07986ad"></a>
<a id="astructethphy__driver__api_html_ace007566a66cc34fb72efa03698dbcf7"></a>
<a id="astructethphy__driver__api_html_ad28d8eedf15a1834492988f4586d7c35"></a>
<a id="astructphy__link__state_html"></a>
<a id="astructphy__link__state_html_aaced7164c07c5f964c952c2b04d68395"></a>
<a id="astructphy__link__state_html_ab47802265dcf47b0aa815f4579467b6f"></a>
<a id="astructphy__plca__cfg_html"></a>
<a id="astructphy__plca__cfg_html_a0be4e9b562c9baabff0fb8c91868e549"></a>
<a id="astructphy__plca__cfg_html_a22346f28e7959b87038e938b169e670a"></a>
<a id="astructphy__plca__cfg_html_a2c5eafc46d4869f11336094657978879"></a>
<a id="astructphy__plca__cfg_html_a3f8580797874684e64fed0bd9bf25a94"></a>
<a id="astructphy__plca__cfg_html_a7b98e4e26e7571aa7e4d1a99d81ea84a"></a>
<a id="astructphy__plca__cfg_html_a841b0ab053ea1903e8d0756f2ec6be87"></a>
<a id="astructphy__plca__cfg_html_aed0ad2e0da7dd1f7fb9e90dcd9d206ca"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2021 IP-Logix Inc.
 * Copyright 2022 NXP
 * Copyright (c) 2025 Aerlync Labs Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_NET_PHY_H_
#define ZEPHYR_INCLUDE_NET_PHY_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/util_macro.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum phy_link_speed {
        LINK_HALF_10BASE = BIT(0),
        LINK_FULL_10BASE = BIT(1),
        LINK_HALF_100BASE = BIT(2),
        LINK_FULL_100BASE = BIT(3),
        LINK_HALF_1000BASE = BIT(4),
        LINK_FULL_1000BASE = BIT(5),
        LINK_FULL_2500BASE = BIT(6),
        LINK_FULL_5000BASE = BIT(7),
};

#define PHY_LINK_IS_FULL_DUPLEX(x)                                                                 \
        (x & (LINK_FULL_10BASE | LINK_FULL_100BASE | LINK_FULL_1000BASE | LINK_FULL_2500BASE |     \
              LINK_FULL_5000BASE))

#define PHY_LINK_IS_SPEED_1000M(x) (x & (LINK_HALF_1000BASE | LINK_FULL_1000BASE))

#define PHY_LINK_IS_SPEED_100M(x) (x & (LINK_HALF_100BASE | LINK_FULL_100BASE))

#define PHY_LINK_IS_SPEED_10M(x) (x & (LINK_HALF_10BASE | LINK_FULL_10BASE))

struct phy_link_state {
        enum phy_link_speed speed;
        bool is_up;
};

enum phy_cfg_link_flag {
        PHY_FLAG_AUTO_NEGOTIATION_DISABLED = BIT(0),
};

struct phy_plca_cfg {
        uint8_t version;
        bool enable;
        uint8_t node_id;
        uint8_t node_count;
        uint8_t burst_count;
        uint8_t burst_timer;
        uint8_t to_timer;
};

typedef void (*phy_callback_t)(const struct device *dev, struct phy_link_state *state,
                               void *user_data);


__subsystem struct ethphy_driver_api {
        int (*get_link)(const struct device *dev, struct phy_link_state *state);

        int (*cfg_link)(const struct device *dev, enum phy_link_speed adv_speeds,
                        enum phy_cfg_link_flag flags);

        int (*link_cb_set)(const struct device *dev, phy_callback_t cb, void *user_data);

        int (*read)(const struct device *dev, uint16_t reg_addr, uint32_t *data);

        int (*write)(const struct device *dev, uint16_t reg_addr, uint32_t data);

        int (*read_c45)(const struct device *dev, uint8_t devad, uint16_t regad, uint16_t *data);

        int (*write_c45)(const struct device *dev, uint8_t devad, uint16_t regad, uint16_t data);

#if defined(CONFIG_ETH_PHY_API_PLCA) || defined(__DOXYGEN__)
        int (*set_plca_cfg)(const struct device *dev, struct phy_plca_cfg *plca_cfg);

        int (*get_plca_cfg)(const struct device *dev, struct phy_plca_cfg *plca_cfg);

        int (*get_plca_sts)(const struct device *dev, bool *plca_sts);
#endif /* CONFIG_ETH_PHY_API_PLCA */
};


static inline int phy_configure_link(const struct device *dev, enum phy_link_speed speeds,
                                     enum phy_cfg_link_flag flags)
{
        if (DEVICE_API_GET(ethphy, dev)->cfg_link == NULL) {
                return -ENOSYS;
        }

        /* Check if only one speed is set, when auto-negotiation is disabled */
        if ((flags & PHY_FLAG_AUTO_NEGOTIATION_DISABLED) && !IS_POWER_OF_TWO(speeds)) {
                return -EINVAL;
        }

        return DEVICE_API_GET(ethphy, dev)->cfg_link(dev, speeds, flags);
}

static inline int phy_get_link_state(const struct device *dev, struct phy_link_state *state)
{
        if (DEVICE_API_GET(ethphy, dev)->get_link == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->get_link(dev, state);
}

static inline int phy_link_callback_set(const struct device *dev, phy_callback_t callback,
                                        void *user_data)
{
        if (DEVICE_API_GET(ethphy, dev)->link_cb_set == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->link_cb_set(dev, callback, user_data);
}

static inline int phy_read(const struct device *dev, uint16_t reg_addr, uint32_t *value)
{
        if (DEVICE_API_GET(ethphy, dev)->read == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->read(dev, reg_addr, value);
}

static inline int phy_write(const struct device *dev, uint16_t reg_addr, uint32_t value)
{
        if (DEVICE_API_GET(ethphy, dev)->write == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->write(dev, reg_addr, value);
}

static inline int phy_read_c45(const struct device *dev, uint8_t devad, uint16_t regad,
                               uint16_t *data)
{
        if (DEVICE_API_GET(ethphy, dev)->read_c45 == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->read_c45(dev, devad, regad, data);
}

static inline int phy_write_c45(const struct device *dev, uint8_t devad, uint16_t regad,
                                uint16_t data)
{
        if (DEVICE_API_GET(ethphy, dev)->write_c45 == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->write_c45(dev, devad, regad, data);
}

static inline int phy_set_plca_cfg(__maybe_unused const struct device *dev,
                                   __maybe_unused struct phy_plca_cfg *plca_cfg)
{
#if defined(CONFIG_ETH_PHY_API_PLCA)
        if (DEVICE_API_GET(ethphy, dev)->set_plca_cfg == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->set_plca_cfg(dev, plca_cfg);
#else
        return -ENOSYS;
#endif /* CONFIG_ETH_PHY_API_PLCA */
}

static inline int phy_get_plca_cfg(__maybe_unused const struct device *dev,
                                   __maybe_unused struct phy_plca_cfg *plca_cfg)
{
#if defined(CONFIG_ETH_PHY_API_PLCA)
        if (DEVICE_API_GET(ethphy, dev)->get_plca_cfg == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->get_plca_cfg(dev, plca_cfg);
#else
        return -ENOSYS;
#endif /* CONFIG_ETH_PHY_API_PLCA */
}

static inline int phy_get_plca_sts(__maybe_unused const struct device *dev,
                                   __maybe_unused bool *plca_status)
{
#if defined(CONFIG_ETH_PHY_API_PLCA)
        if (DEVICE_API_GET(ethphy, dev)->get_plca_sts == NULL) {
                return -ENOSYS;
        }

        return DEVICE_API_GET(ethphy, dev)->get_plca_sts(dev, plca_status);
#else
        return -ENOSYS;
#endif /* CONFIG_ETH_PHY_API_PLCA */
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_PHY_H_ */
```

## 142.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2021 IP-Logix Inc.。

版权（Copyright）：2022 NXP。

版权（Copyright）：© 2025 Aerlync Labs Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 190 行

条件编译配置（Configuration）标记：`CONFIG_ETH_PHY_API_PLCA`。

### 注释 3：原第 216 行

禁用自动协商（Auto-negotiation）时，检查是否只设置了一种速率。

### 注释 4：原第 386 行

条件编译配置（Configuration）标记：`CONFIG_ETH_PHY_API_PLCA`。

### 注释 5：原第 413 行

条件编译配置（Configuration）标记：`CONFIG_ETH_PHY_API_PLCA`。

### 注释 6：原第 440 行

条件编译配置（Configuration）标记：`CONFIG_ETH_PHY_API_PLCA`。

### 注释 7：原第 451 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PHY_H_`。

## 142.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)
- [LINK_HALF_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [LINK_FULL_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)
- [LINK_HALF_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)
- [LINK_FULL_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)
- [LINK_HALF_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)
- [LINK_FULL_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)
- [LINK_FULL_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)
- [LINK_FULL_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)
- [phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)
- [speed](../network_service_model_reference/P040_phy_link_state_结构体.md#ab47802265dcf47b0aa815f4579467b6f)
- [is_up](../network_service_model_reference/P040_phy_link_state_结构体.md#aaced7164c07c5f964c952c2b04d68395)
- [phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)
- [PHY_FLAG_AUTO_NEGOTIATION_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)
- [phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [version](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a2c5eafc46d4869f11336094657978879)
- [enable](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a3f8580797874684e64fed0bd9bf25a94)
- [node_id](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a7b98e4e26e7571aa7e4d1a99d81ea84a)
- [node_count](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a22346f28e7959b87038e938b169e670a)
- [burst_count](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a841b0ab053ea1903e8d0756f2ec6be87)
- [burst_timer](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)
- [to_timer](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a0be4e9b562c9baabff0fb8c91868e549)
- [phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)
- [device](../device_reference/P002_设备对象结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [ethphy_driver_api](../network_service_model_reference/P014_ethphy_driver_api_结构体.md)
- [get_link](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#aa205fb9e753f8a22118be14de07986ad)
- [cfg_link](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a307ea6c0541ab578d8ff7ccf2027e0df)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [link_cb_set](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#ad28d8eedf15a1834492988f4586d7c35)
- [read](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#ace007566a66cc34fb72efa03698dbcf7)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [write](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a5f5dc34c75601974ae4046300e6acf85)
- [read_c45](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a4fd123655cd1dc8ca6c650cf76f3589f)
- [write_c45](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a1f66a4f770674baa32390c1f2e972694)
- [set_plca_cfg](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a1f56afd3cfc34b759c604b55c11c6214)
- [get_plca_cfg](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a9b48f6b3e38da454f658cbcbbd40398c)
- [get_plca_sts](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a68af7c0c8d0e22243b745d09de1a5a47)
- [phy_configure_link](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [IS_POWER_OF_TWO](../util_reference/P001_通用工具公共接口.md#ga52d277cbf33f76350b2fcb21c24640ee)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [phy_get_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4d073c152ad4b6f5745db4f6d8477345)
- [phy_link_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga0ede85fdd6efd8c3520d7baf18d04a68)
- [phy_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3fcca53d29981e23426b43d5340d8651)
- [phy_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga520c049d830051ffa48708bb0dea429f)
- [phy_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4fa30627b96c9a1d02b43c8e799f2796)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [phy_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga492c16dd8b5f2708d9e702ce8906ffd3)
- [phy_set_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga260e528dee1c967ccc9f4d9cb2aadad5)
- [phy_get_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaba1b0bda2a76a6d5db404d24ffec1aa5)
- [phy_get_plca_sts](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaaf47828adbc414304d871441217e772c)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ethphy_driver_api::set_plca_cfg](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a1f56afd3cfc34b759c604b55c11c6214)
- [ethphy_driver_api::write_c45](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a1f66a4f770674baa32390c1f2e972694)
- [ethphy_driver_api::cfg_link](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a307ea6c0541ab578d8ff7ccf2027e0df)
- [ethphy_driver_api::read_c45](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a4fd123655cd1dc8ca6c650cf76f3589f)
- [ethphy_driver_api::write](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a5f5dc34c75601974ae4046300e6acf85)
- [ethphy_driver_api::get_plca_sts](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a68af7c0c8d0e22243b745d09de1a5a47)
- [ethphy_driver_api::get_plca_cfg](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#a9b48f6b3e38da454f658cbcbbd40398c)
- [ethphy_driver_api::get_link](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#aa205fb9e753f8a22118be14de07986ad)
- [ethphy_driver_api::read](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#ace007566a66cc34fb72efa03698dbcf7)
- [ethphy_driver_api::link_cb_set](../network_service_model_reference/P014_ethphy_driver_api_结构体.md#ad28d8eedf15a1834492988f4586d7c35)
- [phy_link_state::is_up](../network_service_model_reference/P040_phy_link_state_结构体.md#aaced7164c07c5f964c952c2b04d68395)
- [phy_link_state::speed](../network_service_model_reference/P040_phy_link_state_结构体.md#ab47802265dcf47b0aa815f4579467b6f)
- [phy_plca_cfg::to_timer](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a0be4e9b562c9baabff0fb8c91868e549)
- [phy_plca_cfg::node_count](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a22346f28e7959b87038e938b169e670a)
- [phy_plca_cfg::version](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a2c5eafc46d4869f11336094657978879)
- [phy_plca_cfg::enable](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a3f8580797874684e64fed0bd9bf25a94)
- [phy_plca_cfg::node_id](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a7b98e4e26e7571aa7e4d1a99d81ea84a)
- [phy_plca_cfg::burst_count](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#a841b0ab053ea1903e8d0756f2ec6be87)
- [phy_plca_cfg::burst_timer](../network_service_model_reference/P041_phy_plca_cfg_结构体.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P141_pcie_ep.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P143_pinctrl-rcar-common.h_源码浏览.md)
