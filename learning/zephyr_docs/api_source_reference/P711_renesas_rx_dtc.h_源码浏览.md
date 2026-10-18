---
id: learning.zephyr-docs.api-source-reference.page-711
title: renesas_rx_dtc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第711章\_renesas\_rx\_dtc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html)。

## 711.1\_原始可见代码（Source Code）

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
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="arenesas__rx__dtc_8h_html_a058dc1dc14c2fc4e1be1352be860fd5d"></a>
<a id="arenesas__rx__dtc_8h_html_a058dc1dc14c2fc4e1be1352be860fd5dab853bdecc90c476b995644c273e0ee75"></a>
<a id="arenesas__rx__dtc_8h_html_a058dc1dc14c2fc4e1be1352be860fd5dadab837d29a543149d35ed2fd28d8e4e8"></a>
<a id="arenesas__rx__dtc_8h_html_a058dc1dc14c2fc4e1be1352be860fd5dae974453c306b4959252905e362d75067"></a>
<a id="arenesas__rx__dtc_8h_html_a0ae834acb01772fef5fd38c62486cb72"></a>
<a id="arenesas__rx__dtc_8h_html_a0ae834acb01772fef5fd38c62486cb72a56a87e1587844119831414f3d5e6d761"></a>
<a id="arenesas__rx__dtc_8h_html_a0ae834acb01772fef5fd38c62486cb72a7665741e25c4cc78fd24745efbd2eaad"></a>
<a id="arenesas__rx__dtc_8h_html_a0ae834acb01772fef5fd38c62486cb72ab8b3f8ce28fb6f7a57a1b87db0d612c2"></a>
<a id="arenesas__rx__dtc_8h_html_a0ae834acb01772fef5fd38c62486cb72abf18f9b3701e9e91f44055ee47d0ca47"></a>
<a id="arenesas__rx__dtc_8h_html_a1280f41f5ad8d4b5beb79a87f5724363"></a>
<a id="arenesas__rx__dtc_8h_html_a1c9f7b59f5fcfeaeb6e528c2b3b067ff"></a>
<a id="arenesas__rx__dtc_8h_html_a4c7e963fd2e8a807ed6f1c1c773bc5ef"></a>
<a id="arenesas__rx__dtc_8h_html_a56fa6d340c574db7be73de060d155b4d"></a>
<a id="arenesas__rx__dtc_8h_html_a56fa6d340c574db7be73de060d155b4da0929782b61686db69e12b3cb18175b35"></a>
<a id="arenesas__rx__dtc_8h_html_a56fa6d340c574db7be73de060d155b4dada378ad830e44cc0c25d4fe2413e11de"></a>
<a id="arenesas__rx__dtc_8h_html_a5888188d6d3123522bd75b08d228b53a"></a>
<a id="arenesas__rx__dtc_8h_html_a5888188d6d3123522bd75b08d228b53aa4a1afc72aa44c347439cb8557e930d74"></a>
<a id="arenesas__rx__dtc_8h_html_a5888188d6d3123522bd75b08d228b53aab1bb6f41ed6ce9f46caa06ba7ef158c6"></a>
<a id="arenesas__rx__dtc_8h_html_a5888188d6d3123522bd75b08d228b53aaf4fc44a34b910cbb4bcac8703e4b7d30"></a>
<a id="arenesas__rx__dtc_8h_html_a72e8a62b215ba60e4f99bca338526e4f"></a>
<a id="arenesas__rx__dtc_8h_html_a81a8afa6b36f96ad966677d0efaefce0"></a>
<a id="arenesas__rx__dtc_8h_html_a81a8afa6b36f96ad966677d0efaefce0a18482bfa86e737cde78042be4db54412"></a>
<a id="arenesas__rx__dtc_8h_html_a81a8afa6b36f96ad966677d0efaefce0a8b6b33a085b51ea2eeed1ef119de562f"></a>
<a id="arenesas__rx__dtc_8h_html_a81a8afa6b36f96ad966677d0efaefce0accfeb24892ec24e42ccf14e4d4896c21"></a>
<a id="arenesas__rx__dtc_8h_html_a93829fb00a7ef2349279986aee9f4c94"></a>
<a id="arenesas__rx__dtc_8h_html_a971f4055201125c15f25b4c7ba12d34e"></a>
<a id="arenesas__rx__dtc_8h_html_a998b3e77a5d2fbd41cdc0d1006cc58d5"></a>
<a id="arenesas__rx__dtc_8h_html_aa1b08c5715fd33b689643a82c63301d9"></a>
<a id="arenesas__rx__dtc_8h_html_aa477baa206c2f80a40d473b648596b61"></a>
<a id="arenesas__rx__dtc_8h_html_aad7601ea771de91d82a213a528f97cb3"></a>
<a id="arenesas__rx__dtc_8h_html_aba28c80e24d2d011f0bb389feffa3da6"></a>
<a id="arenesas__rx__dtc_8h_html_abbe162d4578a4ab187a1549bcc850ca6"></a>
<a id="arenesas__rx__dtc_8h_html_abbe162d4578a4ab187a1549bcc850ca6a2002ef7bbc49f7c9ebfac1618ba3c391"></a>
<a id="arenesas__rx__dtc_8h_html_abbe162d4578a4ab187a1549bcc850ca6a77aeeab30b003de23742e40a57f19239"></a>
<a id="arenesas__rx__dtc_8h_html_ac0840ee89a1688a5212d34c5699640dc"></a>
<a id="arenesas__rx__dtc_8h_html_ad550861b5af9e2d116b03ddc440f6c35"></a>
<a id="arenesas__rx__dtc_8h_html_ada156bb47034b335a8e57d7cdff02238"></a>
<a id="arenesas__rx__dtc_8h_html_ae69bf278e293c26a27b5752894ea3678"></a>
<a id="arenesas__rx__dtc_8h_html_ae6c70fe832e1d8873dd4240d90fe8240"></a>
<a id="arenesas__rx__dtc_8h_html_aea0db2ddbbc3831666b0bf2bb4cc0fb5"></a>
<a id="arenesas__rx__dtc_8h_html_aeba55fc712a1caf61abcf5c7f30e7654"></a>
<a id="arenesas__rx__dtc_8h_html_af3895a9c7e54a6ba5014f54ea541ba75"></a>
<a id="arenesas__rx__dtc_8h_html_af5ab2f4c329bd42eb7893a1aece381f5"></a>
<a id="arenesas__rx__dtc_8h_html_af75bb588cec15252fea99d0cf2e4a9f1"></a>
<a id="arenesas__rx__dtc_8h_html_af75bb588cec15252fea99d0cf2e4a9f1a607c41bfd08797c08a5ee9bd4dfb9c8b"></a>
<a id="arenesas__rx__dtc_8h_html_af75bb588cec15252fea99d0cf2e4a9f1aa4f65de2d9454af406f60172ff858d55"></a>
<a id="arenesas__rx__dtc_8h_html_af75bb588cec15252fea99d0cf2e4a9f1ada90d8a89f98ff82475383b14141b08d"></a>
<a id="arenesas__rx__dtc_8h_html_af75bb588cec15252fea99d0cf2e4a9f1afb43c6e62b61f0dbb9a5bcd5575e79e2"></a>
<a id="arenesas__rx__dtc_8h_html_af833ddfd2351d577c540f7daa1549717"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdtc__transfer__status_html"></a>
<a id="astructdtc__transfer__status_html_a2cc3ae3d23f9f5cfbfd5a1cebf4d1291"></a>
<a id="astructdtc__transfer__status_html_ae755e9c68b612b78b52b55faaf49cd0c"></a>
<a id="astructst__transfer__info_html"></a>
<a id="astructst__transfer__info_html_a0f204801dac4e90a7a15b42ab80f4a25"></a>
<a id="astructst__transfer__info_html_a1562895c38866a2a76fe760a8edf9960"></a>
<a id="astructst__transfer__info_html_a1df273b66e7b94cfa7a66acd867f7fc1"></a>
<a id="astructst__transfer__info_html_a49575b1bace4cee0c2eacf7925b3e670"></a>
<a id="astructst__transfer__info_html_a54be0eab840afa257b9fb5e3c407e676"></a>
<a id="astructst__transfer__info_html_a7f7b11076c155d42b2965694c9697799"></a>
<a id="astructst__transfer__info_html_aaec02eb51bd25b81f5d71d19d917ddd6"></a>
<a id="astructst__transfer__info_html_ab9c64e2333ad51986d13bb9e5c0d17ab"></a>
<a id="astructst__transfer__info_html_abbeeb3232253a9556e2773559fead24b"></a>
<a id="astructst__transfer__info_html_ac862423e3f7bbe27210483f695416ce4"></a>
<a id="astructst__transfer__info_html_ad8cd2bd49b28519e6ed2bd0e23799f9e"></a>
<a id="astructst__transfer__info_html_adb22c126009e9e1c4a366c73a0bc7198"></a>
<a id="astructst__transfer__info_html_ae8a814a11a9ba0af8452c1ef813551a0"></a>
<a id="astructst__transfer__info_html_af8d76658b3b39b9fa26169fdced6f48d"></a>
<a id="astructst__transfer__properties_html"></a>
<a id="astructst__transfer__properties_html_a118301424e4b981bf73787f6cac0a1d0"></a>
<a id="astructst__transfer__properties_html_a477f10434b31f151e1ab5154f2d72557"></a>
<a id="astructst__transfer__properties_html_a80c7a09f3f586e7bc44cfc64b498757e"></a>
<a id="astructst__transfer__properties_html_a93150e77bbc172e5743ab64fba5d303c"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_DTC_RENESAS_RX_DTC_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_DTC_RENESAS_RX_DTC_H_

#include <zephyr/drivers/gpio.h>

#define DTC_PLACE_IN_SECTION(x)                                                                    \
        __attribute__((section(x)))                                                                \
        __attribute__((__used__))
#define DTC_ALIGN_VARIABLE(x) __aligned(x)
#define DTC_SECTION_ATTRIBUTE                                                                      \
        DTC_PLACE_IN_SECTION(".dtc_vector_table")

#define DTC_VECTOR_TABLE_ENTRIES (CONFIG_NUM_IRQS)
#define DTC_PRV_ACT_BIT_MASK     (1 << 15)
#define DTC_PRV_VECT_NR_MASK     (0x00FF)
#define DTC_PRV_MASK_CRAL        (0xFFU)
#define DTC_PRV_OFFSET_CRAH      (8U)

#define DTC_MAX_NORMAL_TRANSFER_LENGTH                                                             \
        (0x10000)

#define DTC_MAX_REPEAT_TRANSFER_LENGTH                                                             \
        (0x100)

#define DTC_MAX_BLOCK_TRANSFER_LENGTH                                                              \
        (0x100)
#define DTC_MAX_BLOCK_COUNT                                                                        \
        (0x10000)


typedef enum e_transfer_addr_mode {
        TRANSFER_ADDR_MODE_FIXED = 0,
        TRANSFER_ADDR_MODE_OFFSET = 1,
        TRANSFER_ADDR_MODE_INCREMENTED = 2,
        TRANSFER_ADDR_MODE_DECREMENTED = 3
} transfer_addr_mode_t;

typedef enum e_transfer_repeat_area {
        TRANSFER_REPEAT_AREA_DESTINATION = 0,
        TRANSFER_REPEAT_AREA_SOURCE = 1
} transfer_repeat_area_t;

typedef enum e_transfer_irq {
        TRANSFER_IRQ_END = 0,
        TRANSFER_IRQ_EACH = 1
} transfer_irq_t;

typedef enum e_transfer_chain_mode {
        TRANSFER_CHAIN_MODE_DISABLED = 0,
        TRANSFER_CHAIN_MODE_EACH = 2,
        TRANSFER_CHAIN_MODE_END = 3
} transfer_chain_mode_t;

typedef enum e_transfer_size {
        TRANSFER_SIZE_1_BYTE = 0,
        TRANSFER_SIZE_2_BYTE = 1,
        TRANSFER_SIZE_4_BYTE = 2
} transfer_size_t;

typedef enum e_transfer_mode {
        TRANSFER_MODE_NORMAL = 0,
        TRANSFER_MODE_REPEAT = 1,
        TRANSFER_MODE_BLOCK = 2,
        TRANSFER_MODE_REPEAT_BLOCK = 3
} transfer_mode_t;

typedef enum e_dtc_act_status {
        DTC_ACT_IDLE = 0,
        DTC_ACT_CONFIGURED = 1,
        DTC_ACT_IN_PROGRESS = 2,
} dtc_act_status_t;

typedef struct st_transfer_info {
        union {
                struct {
                        unsigned int: 16;
                        unsigned int: 2;

                        transfer_addr_mode_t dest_addr_mode: 2;

                        transfer_repeat_area_t repeat_area: 1;

                        transfer_irq_t irq: 1;

                        transfer_chain_mode_t chain_mode: 2;

                        unsigned int: 2;

                        transfer_addr_mode_t src_addr_mode: 2;

                        transfer_size_t size: 2;

                        transfer_mode_t mode: 2;
                } transfer_settings_word_b;

                uint32_t transfer_settings_word;
        };

        void const *volatile p_src;
        void *volatile p_dest;
        volatile uint16_t num_blocks;
        volatile uint16_t length;
} transfer_info_t;

typedef struct st_transfer_properties {
        uint32_t block_count_max;
        uint32_t block_count_remaining;
        uint32_t transfer_length_max;
        uint32_t transfer_length_remaining;
} transfer_properties_t;

struct dtc_transfer_status {
        uint8_t activation_irq;
        bool in_progress;
};

int dtc_renesas_rx_off(const struct device *dev);

int dtc_renesas_rx_on(const struct device *dev);

int dtc_renesas_rx_configuration(const struct device *dev, uint8_t activation_irq,
                                 transfer_info_t *p_info);

int dtc_renesas_rx_enable_transfer(uint8_t activation_irq);

int dtc_renesas_rx_disable_transfer(uint8_t activation_irq);

int dtc_renesas_rx_start_transfer(const struct device *dev, uint8_t activation_irq);

int dtc_renesas_rx_stop_transfer(const struct device *dev, uint8_t activation_irq);

int dtc_renesas_rx_reset_transfer(const struct device *dev, uint8_t activation_irq,
                                  void const *p_src, void *p_dest, uint16_t const num_transfers);

void dtc_renesas_rx_get_transfer_status(const struct device *dev,
                                        struct dtc_transfer_status *status);

int dtc_renesas_rx_info_get(const struct device *dev, uint8_t activation_irq,
                            transfer_properties_t *const p_properties);

static ALWAYS_INLINE bool is_valid_activation_irq(uint8_t activation_irq)
{
        if (activation_irq < 0 || activation_irq > DTC_VECTOR_TABLE_ENTRIES) {
                return false;
        }

        return true;
}

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_DTC_RENESAS_RX_DTC_H_ */
```

## 711.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 262 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_DTC_RENESAS_RX_DTC_H_`。

## 711.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [e_transfer_addr_mode](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a0ae834acb01772fef5fd38c62486cb72)
- [TRANSFER_ADDR_MODE_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a0ae834acb01772fef5fd38c62486cb72abf18f9b3701e9e91f44055ee47d0ca47)
- [TRANSFER_ADDR_MODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a0ae834acb01772fef5fd38c62486cb72ab8b3f8ce28fb6f7a57a1b87db0d612c2)
- [TRANSFER_ADDR_MODE_INCREMENTED](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a0ae834acb01772fef5fd38c62486cb72a7665741e25c4cc78fd24745efbd2eaad)
- [TRANSFER_ADDR_MODE_DECREMENTED](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a0ae834acb01772fef5fd38c62486cb72a56a87e1587844119831414f3d5e6d761)
- [transfer_addr_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ae69bf278e293c26a27b5752894ea3678)
- [e_transfer_repeat_area](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#abbe162d4578a4ab187a1549bcc850ca6)
- [TRANSFER_REPEAT_AREA_DESTINATION](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#abbe162d4578a4ab187a1549bcc850ca6a77aeeab30b003de23742e40a57f19239)
- [TRANSFER_REPEAT_AREA_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#abbe162d4578a4ab187a1549bcc850ca6a2002ef7bbc49f7c9ebfac1618ba3c391)
- [transfer_repeat_area_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af5ab2f4c329bd42eb7893a1aece381f5)
- [e_transfer_irq](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a56fa6d340c574db7be73de060d155b4d)
- [TRANSFER_IRQ_END](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a56fa6d340c574db7be73de060d155b4dada378ad830e44cc0c25d4fe2413e11de)
- [TRANSFER_IRQ_EACH](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a56fa6d340c574db7be73de060d155b4da0929782b61686db69e12b3cb18175b35)
- [transfer_irq_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ad550861b5af9e2d116b03ddc440f6c35)
- [e_transfer_chain_mode](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a058dc1dc14c2fc4e1be1352be860fd5d)
- [TRANSFER_CHAIN_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a058dc1dc14c2fc4e1be1352be860fd5dae974453c306b4959252905e362d75067)
- [TRANSFER_CHAIN_MODE_EACH](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a058dc1dc14c2fc4e1be1352be860fd5dadab837d29a543149d35ed2fd28d8e4e8)
- [TRANSFER_CHAIN_MODE_END](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a058dc1dc14c2fc4e1be1352be860fd5dab853bdecc90c476b995644c273e0ee75)
- [transfer_chain_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a1c9f7b59f5fcfeaeb6e528c2b3b067ff)
- [e_transfer_size](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a81a8afa6b36f96ad966677d0efaefce0)
- [TRANSFER_SIZE_1_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a81a8afa6b36f96ad966677d0efaefce0accfeb24892ec24e42ccf14e4d4896c21)
- [TRANSFER_SIZE_2_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a81a8afa6b36f96ad966677d0efaefce0a8b6b33a085b51ea2eeed1ef119de562f)
- [TRANSFER_SIZE_4_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a81a8afa6b36f96ad966677d0efaefce0a18482bfa86e737cde78042be4db54412)
- [transfer_size_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ada156bb47034b335a8e57d7cdff02238)
- [e_transfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af75bb588cec15252fea99d0cf2e4a9f1)
- [TRANSFER_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af75bb588cec15252fea99d0cf2e4a9f1ada90d8a89f98ff82475383b14141b08d)
- [TRANSFER_MODE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af75bb588cec15252fea99d0cf2e4a9f1a607c41bfd08797c08a5ee9bd4dfb9c8b)
- [TRANSFER_MODE_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af75bb588cec15252fea99d0cf2e4a9f1aa4f65de2d9454af406f60172ff858d55)
- [TRANSFER_MODE_REPEAT_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af75bb588cec15252fea99d0cf2e4a9f1afb43c6e62b61f0dbb9a5bcd5575e79e2)
- [transfer_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aea0db2ddbbc3831666b0bf2bb4cc0fb5)
- [e_dtc_act_status](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a5888188d6d3123522bd75b08d228b53a)
- [DTC_ACT_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a5888188d6d3123522bd75b08d228b53aaf4fc44a34b910cbb4bcac8703e4b7d30)
- [DTC_ACT_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a5888188d6d3123522bd75b08d228b53aab1bb6f41ed6ce9f46caa06ba7ef158c6)
- [DTC_ACT_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a5888188d6d3123522bd75b08d228b53aa4a1afc72aa44c347439cb8557e930d74)
- [dtc_act_status_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a93829fb00a7ef2349279986aee9f4c94)
- [st_transfer_info](../device_power_control_model_reference/P090_st_transfer_info_结构体.md)
- [int](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a0f204801dac4e90a7a15b42ab80f4a25)
- [dest_addr_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a1df273b66e7b94cfa7a66acd867f7fc1)
- [repeat_area](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a54be0eab840afa257b9fb5e3c407e676)
- [irq](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ac862423e3f7bbe27210483f695416ce4)
- [chain_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ad8cd2bd49b28519e6ed2bd0e23799f9e)
- [src_addr_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a1562895c38866a2a76fe760a8edf9960)
- [size](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#aaec02eb51bd25b81f5d71d19d917ddd6)
- [mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#adb22c126009e9e1c4a366c73a0bc7198)
- [transfer_settings_word_b](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a49575b1bace4cee0c2eacf7925b3e670)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [transfer_settings_word](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#af8d76658b3b39b9fa26169fdced6f48d)
- [p_src](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a7f7b11076c155d42b2965694c9697799)
- [p_dest](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ab9c64e2333ad51986d13bb9e5c0d17ab)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [num_blocks](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#abbeeb3232253a9556e2773559fead24b)
- [length](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ae8a814a11a9ba0af8452c1ef813551a0)
- [transfer_info_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a971f4055201125c15f25b4c7ba12d34e)
- [st_transfer_properties](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md)
- [block_count_max](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a477f10434b31f151e1ab5154f2d72557)
- [block_count_remaining](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a80c7a09f3f586e7bc44cfc64b498757e)
- [transfer_length_max](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a93150e77bbc172e5743ab64fba5d303c)
- [transfer_length_remaining](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a118301424e4b981bf73787f6cac0a1d0)
- [transfer_properties_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aa1b08c5715fd33b689643a82c63301d9)
- [dtc_transfer_status](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [activation_irq](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md#a2cc3ae3d23f9f5cfbfd5a1cebf4d1291)
- [in_progress](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md#ae755e9c68b612b78b52b55faaf49cd0c)
- [dtc_renesas_rx_off](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a72e8a62b215ba60e4f99bca338526e4f)
- [device](../device_reference/P002_设备对象结构.md)
- [dtc_renesas_rx_on](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aeba55fc712a1caf61abcf5c7f30e7654)
- [dtc_renesas_rx_configuration](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a4c7e963fd2e8a807ed6f1c1c773bc5ef)
- [dtc_renesas_rx_enable_transfer](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ac0840ee89a1688a5212d34c5699640dc)
- [dtc_renesas_rx_disable_transfer](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aba28c80e24d2d011f0bb389feffa3da6)
- [dtc_renesas_rx_start_transfer](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a1280f41f5ad8d4b5beb79a87f5724363)
- [dtc_renesas_rx_stop_transfer](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aad7601ea771de91d82a213a528f97cb3)
- [dtc_renesas_rx_reset_transfer](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ae6c70fe832e1d8873dd4240d90fe8240)
- [dtc_renesas_rx_get_transfer_status](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af833ddfd2351d577c540f7daa1549717)
- [dtc_renesas_rx_info_get](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aa477baa206c2f80a40d473b648596b61)
- [is_valid_activation_irq](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af3895a9c7e54a6ba5014f54ea541ba75)
- [DTC_VECTOR_TABLE_ENTRIES](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a998b3e77a5d2fbd41cdc0d1006cc58d5)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [dtc_transfer_status::activation_irq](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md#a2cc3ae3d23f9f5cfbfd5a1cebf4d1291)
- [dtc_transfer_status::in_progress](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md#ae755e9c68b612b78b52b55faaf49cd0c)
- [st_transfer_info::int](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a0f204801dac4e90a7a15b42ab80f4a25)
- [st_transfer_info::src_addr_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a1562895c38866a2a76fe760a8edf9960)
- [st_transfer_info::dest_addr_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a1df273b66e7b94cfa7a66acd867f7fc1)
- [st_transfer_info::transfer_settings_word_b](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a49575b1bace4cee0c2eacf7925b3e670)
- [st_transfer_info::repeat_area](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a54be0eab840afa257b9fb5e3c407e676)
- [st_transfer_info::p_src](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#a7f7b11076c155d42b2965694c9697799)
- [st_transfer_info::size](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#aaec02eb51bd25b81f5d71d19d917ddd6)
- [st_transfer_info::p_dest](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ab9c64e2333ad51986d13bb9e5c0d17ab)
- [st_transfer_info::num_blocks](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#abbeeb3232253a9556e2773559fead24b)
- [st_transfer_info::irq](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ac862423e3f7bbe27210483f695416ce4)
- [st_transfer_info::chain_mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ad8cd2bd49b28519e6ed2bd0e23799f9e)
- [st_transfer_info::mode](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#adb22c126009e9e1c4a366c73a0bc7198)
- [st_transfer_info::length](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#ae8a814a11a9ba0af8452c1ef813551a0)
- [st_transfer_info::transfer_settings_word](../device_power_control_model_reference/P090_st_transfer_info_结构体.md#af8d76658b3b39b9fa26169fdced6f48d)
- [st_transfer_properties::transfer_length_remaining](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a118301424e4b981bf73787f6cac0a1d0)
- [st_transfer_properties::block_count_max](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a477f10434b31f151e1ab5154f2d72557)
- [st_transfer_properties::block_count_remaining](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a80c7a09f3f586e7bc44cfc64b498757e)
- [st_transfer_properties::transfer_length_max](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md#a93150e77bbc172e5743ab64fba5d303c)

---

[上一章](P710_renesas_rx_cgc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P712_renesas_rx_external_interrupt.h_源码浏览.md)
