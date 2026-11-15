---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-1
title: pcie.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_pcie.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
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
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
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
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="foldopen00490"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="foldopen00504"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00519"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="foldopen00529"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="foldopen00538"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="foldopen00551"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="adevicetree_8h_html"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html"></a>
<a id="agroup__pcie__host__interface_html_ga10ecc667c564548e4ddf3ca4374242b5"></a>
<a id="agroup__pcie__host__interface_html_ga14970194de1024a1a4669b69f932a4f5"></a>
<a id="agroup__pcie__host__interface_html_ga30840d0e312e35f00790660193fd4c04"></a>
<a id="agroup__pcie__host__interface_html_ga3516fec89df75eb3d77f54193059fc5c"></a>
<a id="agroup__pcie__host__interface_html_ga3523bbdfd67d4b56cf6cd86c98c830bf"></a>
<a id="agroup__pcie__host__interface_html_ga47a2e88935e04330d449db5463d9f21a"></a>
<a id="agroup__pcie__host__interface_html_ga56e724c9bfd7f44c550ccff1b46978a8"></a>
<a id="agroup__pcie__host__interface_html_ga5db0d2a5946d20406070b47a1a7acf21"></a>
<a id="agroup__pcie__host__interface_html_ga922580e4fb6200ef75425bb54801ceda"></a>
<a id="agroup__pcie__host__interface_html_ga9a7b3c202f91d37fe8445d5016f4c6ab"></a>
<a id="agroup__pcie__host__interface_html_gaa81d98a9ee58062c02be576fb0dfefd9"></a>
<a id="agroup__pcie__host__interface_html_gad69ae431e5f91992f071dee9d7fa9110"></a>
<a id="agroup__pcie__host__interface_html_gad8463013e51c4ddcca7b5f805f918685"></a>
<a id="agroup__pcie__host__interface_html_gadeb891fbb5b900eb60de22d40afe355e"></a>
<a id="agroup__pcie__host__interface_html_gaed7fef462ba02a22b5875b1a2c0d965a"></a>
<a id="agroup__pcie__host__interface_html_gaf9748042a4f3c8d912d19df1ccf737fb"></a>
<a id="agroup__pcie__host__interface_html_gafb69216f9224a9040b1f0b58eb286196"></a>
<a id="agroup__pcie__host__interface_html_ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4"></a>
<a id="agroup__pcie__host__interface_html_ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructpcie__bar_html"></a>
<a id="astructpcie__bar_html_a75ed340a7d80a6825f3c60469194dae8"></a>
<a id="astructpcie__bar_html_ab68c921f2993c94d2ae65684568bf770"></a>
<a id="astructpcie__dev_html"></a>
<a id="astructpcie__dev_html_a5709ef678d9e81d4d3a61f6c26371076"></a>
<a id="astructpcie__dev_html_a798e25696997a74ed01f8df6cec64489"></a>
<a id="astructpcie__dev_html_a7cc2f61e85b1d9c4985115b91fc6e832"></a>
<a id="astructpcie__dev_html_abedf281cdce4961dd02abba849747f45"></a>
<a id="astructpcie__scan__opt_html"></a>
<a id="astructpcie__scan__opt_html_a036225c7a5730ba2040e03cab491b9da"></a>
<a id="astructpcie__scan__opt_html_a11b39138d2a2b6b1e8e1bd80216a8da6"></a>
<a id="astructpcie__scan__opt_html_a28ad6c4993eed7bdf08ce682692bf306"></a>
<a id="astructpcie__scan__opt_html_a7e485fb824dea16f9d5fdcb7079ebb7e"></a>
<a id="astructpcie__scan__opt_html_af3b4de1e2cb9263ddcdc2849f5773be8"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PCIE_PCIE_H_
#define ZEPHYR_INCLUDE_DRIVERS_PCIE_PCIE_H_


#include <stddef.h>
#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/pcie/pcie.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef uint32_t pcie_bdf_t;

typedef uint32_t pcie_id_t;

/* Helper macro to exclude invalid PCIe identifiers. We should really only
 * need to look for PCIE_ID_NONE, but because of some broken PCI host controllers
 * we have try cases where both VID & DID are zero or just one of them is
 * zero (0x0000) and the other is all ones (0xFFFF).
 */
#define PCIE_ID_IS_VALID(id) ((id != PCIE_ID_NONE) && \
                              (id != PCIE_ID(0x0000, 0x0000)) && \
                              (id != PCIE_ID(0xFFFF, 0x0000)) && \
                              (id != PCIE_ID(0x0000, 0xFFFF)))

struct pcie_dev {
        pcie_bdf_t bdf;
        pcie_id_t  id;
        uint32_t   class_rev;
        uint32_t   class_rev_mask;
};

#define Z_DEVICE_PCIE_NAME(node_id) _CONCAT(pcie_dev_, DT_DEP_ORD(node_id))

#define PCIE_DT_ID(node_id) PCIE_ID(DT_PROP_OR(node_id, vendor_id, 0xffff), \
                                    DT_PROP_OR(node_id, device_id, 0xffff))

#define PCIE_DT_INST_ID(inst) PCIE_DT_ID(DT_DRV_INST(inst))

#define DEVICE_PCIE_DECLARE(node_id)                                        \
        STRUCT_SECTION_ITERABLE(pcie_dev, Z_DEVICE_PCIE_NAME(node_id)) = {  \
                .bdf = PCIE_BDF_NONE,                                       \
                .id = PCIE_DT_ID(node_id),                                  \
                .class_rev = DT_PROP_OR(node_id, class_rev, 0),             \
                .class_rev_mask = DT_PROP_OR(node_id, class_rev_mask, 0),   \
        }

#define DEVICE_PCIE_INST_DECLARE(inst) DEVICE_PCIE_DECLARE(DT_DRV_INST(inst))

#define DEVICE_PCIE_INIT(node_id, name) .name = &Z_DEVICE_PCIE_NAME(node_id)

#define DEVICE_PCIE_INST_INIT(inst, name) \
        DEVICE_PCIE_INIT(DT_DRV_INST(inst), name)

struct pcie_bar {
        uintptr_t phys_addr;
        size_t size;
};

/*
 * These functions are arch-, board-, or SoC-specific.
 */

extern uint32_t pcie_conf_read(pcie_bdf_t bdf, unsigned int reg);

extern void pcie_conf_write(pcie_bdf_t bdf, unsigned int reg, uint32_t data);

typedef bool (*pcie_scan_cb_t)(pcie_bdf_t bdf, pcie_id_t id, void *cb_data);

enum {
        PCIE_SCAN_RECURSIVE = BIT(0),
        PCIE_SCAN_CB_ALL = BIT(1),
};

struct pcie_scan_opt {
        uint8_t bus;

        pcie_scan_cb_t cb;

        void *cb_data;

        uint32_t flags;

        bool (*scan_masking_fn)(pcie_bdf_t bdf);
};

int pcie_scan(const struct pcie_scan_opt *opt);

extern bool pcie_get_mbar(pcie_bdf_t bdf,
                          unsigned int bar_index,
                          struct pcie_bar *mbar);

extern bool pcie_probe_mbar(pcie_bdf_t bdf,
                            unsigned int index,
                            struct pcie_bar *mbar);

extern bool pcie_get_iobar(pcie_bdf_t bdf,
                           unsigned int bar_index,
                           struct pcie_bar *iobar);

extern bool pcie_probe_iobar(pcie_bdf_t bdf,
                             unsigned int index,
                             struct pcie_bar *iobar);

extern void pcie_set_cmd(pcie_bdf_t bdf, uint32_t bits, bool on);

#ifndef CONFIG_PCIE_CONTROLLER
extern unsigned int pcie_alloc_irq(pcie_bdf_t bdf);
#endif /* CONFIG_PCIE_CONTROLLER */

extern unsigned int pcie_get_irq(pcie_bdf_t bdf);

extern void pcie_irq_enable(pcie_bdf_t bdf, unsigned int irq);

extern uint32_t pcie_get_cap(pcie_bdf_t bdf, uint32_t cap_id);

extern uint32_t pcie_get_ext_cap(pcie_bdf_t bdf, uint32_t cap_id);

extern bool pcie_connect_dynamic_irq(pcie_bdf_t bdf,
                                     unsigned int irq,
                                     unsigned int priority,
                                     void (*routine)(const void *parameter),
                                     const void *parameter,
                                     uint32_t flags);

#define PCIE_HOST_CONTROLLER(n) PCIE_BDF(0, 0, n)

/*
 * Configuration word 13 contains the head of the capabilities list.
 */

#define PCIE_CONF_CAPPTR        13U     /* capabilities pointer */
#define PCIE_CONF_CAPPTR_FIRST(w)       (((w) >> 2) & 0x3FU)

/*
 * The first word of every capability contains a capability identifier,
 * and a link to the next capability (or 0) in configuration space.
 */

#define PCIE_CONF_CAP_ID(w)             ((w) & 0xFFU)
#define PCIE_CONF_CAP_NEXT(w)           (((w) >> 10) & 0x3FU)

/*
 * The extended PCI Express capabilities lie at the end of the PCI configuration space
 */

#define PCIE_CONF_EXT_CAPPTR    64U

/*
 * The first word of every capability contains an extended capability identifier,
 * and a link to the next capability (or 0) in the extended configuration space.
 */

#define PCIE_CONF_EXT_CAP_ID(w)         ((w) & 0xFFFFU)
#define PCIE_CONF_EXT_CAP_VER(w)        (((w) >> 16) & 0xFU)
#define PCIE_CONF_EXT_CAP_NEXT(w)       (((w) >> 20) & 0xFFFU)

/*
 * Configuration word 0 aligns directly with pcie_id_t.
 */

#define PCIE_CONF_ID            0U

/*
 * Configuration word 1 contains command and status bits.
 */

#define PCIE_CONF_CMDSTAT       1U      /* command/status register */

#define PCIE_CONF_CMDSTAT_IO            0x00000001U  /* I/O access enable */
#define PCIE_CONF_CMDSTAT_MEM           0x00000002U  /* mem access enable */
#define PCIE_CONF_CMDSTAT_MASTER        0x00000004U  /* bus master enable */
#define PCIE_CONF_CMDSTAT_SERR          0x00000100U  /* SERR# enable */
#define PCIE_CONF_CMDSTAT_INTERRUPT     0x00080000U  /* interrupt status */
#define PCIE_CONF_CMDSTAT_CAPS          0x00100000U  /* capabilities list */

/*
 * Configuration word 2 has additional function identification that
 * we only care about for debug output (PCIe shell commands).
 */

#define PCIE_CONF_CLASSREV      2U      /* class/revision register */

#define PCIE_CONF_CLASSREV_CLASS(w)     (((w) >> 24) & 0xFFU)
#define PCIE_CONF_CLASSREV_SUBCLASS(w)  (((w) >> 16) & 0xFFU)
#define PCIE_CONF_CLASSREV_PROGIF(w)    (((w) >> 8) & 0xFFU)
#define PCIE_CONF_CLASSREV_REV(w)       ((w) & 0xFFU)

/*
 * The only part of configuration word 3 that is of interest to us is
 * the header type, as we use it to distinguish functional endpoints
 * from bridges (which are, for our purposes, transparent).
 */

#define PCIE_CONF_TYPE          3U

#define PCIE_CONF_MULTIFUNCTION(w)      (((w) & 0x00800000U) != 0U)
#define PCIE_CONF_TYPE_BRIDGE(w)        (((w) & 0x007F0000U) != 0U)
#define PCIE_CONF_TYPE_GET(w)           (((w) >> 16) & 0x7F)

#define PCIE_CONF_TYPE_STANDARD         0x0U
#define PCIE_CONF_TYPE_PCI_BRIDGE       0x1U
#define PCIE_CONF_TYPE_CARDBUS_BRIDGE   0x2U

/*
 * Words 4-9 are BARs are I/O or memory decoders. Memory decoders may
 * be 64-bit decoders, in which case the next configuration word holds
 * the high-order bits (and is, thus, not a BAR itself).
 */

#define PCIE_CONF_BAR0          4U
#define PCIE_CONF_BAR1          5U
#define PCIE_CONF_BAR2          6U
#define PCIE_CONF_BAR3          7U
#define PCIE_CONF_BAR4          8U
#define PCIE_CONF_BAR5          9U

#define PCIE_CONF_BAR_IO(w)             (((w) & 0x00000001U) == 0x00000001U)
#define PCIE_CONF_BAR_MEM(w)            (((w) & 0x00000001U) != 0x00000001U)
#define PCIE_CONF_BAR_64(w)             (((w) & 0x00000006U) == 0x00000004U)
#define PCIE_CONF_BAR_ADDR(w)           ((w) & ~0xfUL)
#define PCIE_CONF_BAR_IO_ADDR(w)        ((w) & ~0x3UL)
#define PCIE_CONF_BAR_FLAGS(w)          ((w) & 0xfUL)
#define PCIE_CONF_BAR_NONE              0U

#define PCIE_CONF_BAR_INVAL             0xFFFFFFF0U
#define PCIE_CONF_BAR_INVAL64           0xFFFFFFFFFFFFFFF0UL

#define PCIE_CONF_BAR_INVAL_FLAGS(w)                    \
        ((((w) & 0x00000006U) == 0x00000006U) ||        \
         (((w) & 0x00000006U) == 0x00000002U))

/*
 * Type 1 Header has files related to bus management
 */
#define PCIE_BUS_NUMBER         6U

#define PCIE_BUS_PRIMARY_NUMBER(w)      ((w) & 0xffUL)
#define PCIE_BUS_SECONDARY_NUMBER(w)    (((w) >> 8) & 0xffUL)
#define PCIE_BUS_SUBORDINATE_NUMBER(w)  (((w) >> 16) & 0xffUL)
#define PCIE_SECONDARY_LATENCY_TIMER(w) (((w) >> 24) & 0xffUL)

#define PCIE_BUS_NUMBER_VAL(prim, sec, sub, lat) \
        (((prim) & 0xffUL) |                     \
         (((sec) & 0xffUL) << 8) |               \
         (((sub) & 0xffUL) << 16) |              \
         (((lat) & 0xffUL) << 24))

/*
 * Type 1 words 7 to 12 setups Bridge Memory base and limits
 */
#define PCIE_IO_SEC_STATUS      7U

#define PCIE_IO_BASE(w)         ((w) & 0xffUL)
#define PCIE_IO_LIMIT(w)        (((w) >> 8) & 0xffUL)
#define PCIE_SEC_STATUS(w)      (((w) >> 16) & 0xffffUL)

#define PCIE_IO_SEC_STATUS_VAL(iob, iol, sec_status) \
        (((iob) & 0xffUL) |                          \
         (((iol) & 0xffUL) << 8) |                   \
         (((sec_status) & 0xffffUL) << 16))

#define PCIE_MEM_BASE_LIMIT     8U

#define PCIE_MEM_BASE(w)        ((w) & 0xffffUL)
#define PCIE_MEM_LIMIT(w)       (((w) >> 16) & 0xffffUL)

#define PCIE_MEM_BASE_LIMIT_VAL(memb, meml) \
        (((memb) & 0xffffUL) |              \
         (((meml) & 0xffffUL) << 16))

#define PCIE_PREFETCH_BASE_LIMIT        9U

#define PCIE_PREFETCH_BASE(w)   ((w) & 0xffffUL)
#define PCIE_PREFETCH_LIMIT(w)  (((w) >> 16) & 0xffffUL)

#define PCIE_PREFETCH_BASE_LIMIT_VAL(pmemb, pmeml) \
        (((pmemb) & 0xffffUL) |                    \
         (((pmeml) & 0xffffUL) << 16))

#define PCIE_PREFETCH_BASE_UPPER        10U

#define PCIE_PREFETCH_LIMIT_UPPER       11U

#define PCIE_IO_BASE_LIMIT_UPPER        12U

#define PCIE_IO_BASE_UPPER(w)   ((w) & 0xffffUL)
#define PCIE_IO_LIMIT_UPPER(w)  (((w) >> 16) & 0xffffUL)

#define PCIE_IO_BASE_LIMIT_UPPER_VAL(iobu, iolu) \
        (((iobu) & 0xffffUL) |                   \
         (((iolu) & 0xffffUL) << 16))

/*
 * Word 15 contains information related to interrupts.
 *
 * We're only interested in the low byte, which is [supposed to be] set by
 * the firmware to indicate which wire IRQ the device interrupt is routed to.
 */

#define PCIE_CONF_INTR          15U

#define PCIE_CONF_INTR_IRQ(w)   ((w) & 0xFFU)
#define PCIE_CONF_INTR_IRQ_NONE 0xFFU  /* no interrupt routed */

#define PCIE_MAX_BUS  (0xFFFFFFFFU & PCIE_BDF_BUS_MASK)
#define PCIE_MAX_DEV  (0xFFFFFFFFU & PCIE_BDF_DEV_MASK)
#define PCIE_MAX_FUNC (0xFFFFFFFFU & PCIE_BDF_FUNC_MASK)

#define PCIE_IRQ_CONNECT(bdf_p, irq_p, priority_p,                      \
                         isr_p, isr_param_p, flags_p)                   \
        ARCH_PCIE_IRQ_CONNECT(bdf_p, irq_p, priority_p,                 \
                              isr_p, isr_param_p, flags_p)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_PCIE_PCIE_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

排除无效 PCIe 标识符（Identifiers）的辅助宏。原本只需检查 `PCIE_ID_NONE`，但由于某些 PCI 主机控制器存在缺陷，还必须尝试 VID 和 DID 均为 0，以及其中一个为 `0x0000`、另一个为全 1（`0xFFFF`）的情况。

### 注释 3：原第 167 行

这些函数由体系结构（Architecture）、开发板（Board）或片上系统（SoC）专门实现。

### 注释 4：原第 317 行

条件编译配置（Configuration）标记：`CONFIG_PCIE_CONTROLLER`。

### 注释 5：原第 389 行

配置字（Configuration Word）13 包含能力链表（Capabilities List）的表头。

### 注释 6：原第 393 行

能力指针（Capabilities Pointer）。

### 注释 7：原第 396 行

每项能力（Capability）的第一个字包含能力标识符，以及配置空间（Configuration Space）中指向下一项能力的链接，或 0。

### 注释 8：原第 404 行

PCI Express 扩展能力（Extended Capabilities）位于 PCI 配置空间的末尾。

### 注释 9：原第 410 行

每项能力（Capability）的第一个字包含扩展能力标识符，以及扩展配置空间中指向下一项能力的链接，或 0。

### 注释 10：原第 419 行

配置字（Configuration Word）0 与 `pcie_id_t` 直接对应。

### 注释 11：原第 425 行

配置字（Configuration Word）1 包含命令位和状态位（Command and Status Bits）。

### 注释 12：原第 429 行

命令／状态寄存器（Command/Status Register）。

### 注释 13：原第 431 行

输入／输出访问使能（I/O Access Enable）。

### 注释 14：原第 432 行

内存访问使能（Memory Access Enable）。

### 注释 15：原第 433 行

总线主控使能（Bus Master Enable）。

### 注释 16：原第 434 行

系统错误信号 SERR# 使能（Enable）。

### 注释 17：原第 435 行

中断状态（Interrupt Status）。

### 注释 18：原第 436 行

能力链表（Capabilities List）。

### 注释 19：原第 438 行

配置字（Configuration Word）2 包含额外的功能标识信息，只在调试输出中使用，即 PCIe shell 命令。

### 注释 20：原第 443 行

类别／修订版本寄存器（Class/Revision Register）。

### 注释 21：原第 450 行

配置字（Configuration Word）3 中唯一需要关注的是头部类型（Header Type），用于区分功能端点（Functional Endpoints）与桥（Bridges）；在这里，桥被视为透明。

### 注释 22：原第 466 行

配置字 4–9 为基址寄存器（BAR），用于 I/O 或内存地址译码。内存译码器可能为 64 位，此时下一个配置字保存高位部分，因此它本身不再是独立的 BAR。

### 注释 23：原第 494 行

类型 1 头部（Type 1 Header）包含与总线管理相关的项目。

> 译注：原文使用 `files`，结合总线管理寄存器上下文，此处译为“项目”，未据此增加字段定义。

### 注释 24：原第 510 行

类型 1 的配置字 7–12 设置桥的内存基址和界限（Bridge Memory Base and Limits）。

### 注释 25：原第 555 行

配置字 15 包含中断相关信息。这里只关注低字节，它应当由固件设置，用于指示设备中断被路由到哪条有线中断请求线（Wire IRQ）。

### 注释 26：原第 565 行

未路由中断（No Interrupt Routed）。

### 注释 27：原第 598 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PCIE_PCIE_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/dt-bindings/pcie/pcie.h](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)
- [pcie_dev](../platform_security_model_reference/P028_pcie_dev_结构体.md)
- [bdf](../platform_security_model_reference/P028_pcie_dev_结构体.md#a7cc2f61e85b1d9c4985115b91fc6e832)
- [id](../platform_security_model_reference/P028_pcie_dev_结构体.md#a5709ef678d9e81d4d3a61f6c26371076)
- [class_rev](../platform_security_model_reference/P028_pcie_dev_结构体.md#abedf281cdce4961dd02abba849747f45)
- [class_rev_mask](../platform_security_model_reference/P028_pcie_dev_结构体.md#a798e25696997a74ed01f8df6cec64489)
- [pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [phys_addr](../platform_security_model_reference/P025_pcie_bar_结构体.md#a75ed340a7d80a6825f3c60469194dae8)
- [size](../platform_security_model_reference/P025_pcie_bar_结构体.md#ab68c921f2993c94d2ae65684568bf770)
- [pcie_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga10ecc667c564548e4ddf3ca4374242b5)
- [pcie_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga47a2e88935e04330d449db5463d9f21a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga922580e4fb6200ef75425bb54801ceda)
- [PCIE_SCAN_RECURSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PCIE_SCAN_CB_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072)
- [pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bus](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a036225c7a5730ba2040e03cab491b9da)
- [cb](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a28ad6c4993eed7bdf08ce682692bf306)
- [cb_data](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a11b39138d2a2b6b1e8e1bd80216a8da6)
- [flags](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a7e485fb824dea16f9d5fdcb7079ebb7e)
- [scan_masking_fn](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#af3b4de1e2cb9263ddcdc2849f5773be8)
- [pcie_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9a7b3c202f91d37fe8445d5016f4c6ab)
- [pcie_get_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gadeb891fbb5b900eb60de22d40afe355e)
- [pcie_probe_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad8463013e51c4ddcca7b5f805f918685)
- [pcie_get_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3523bbdfd67d4b56cf6cd86c98c830bf)
- [pcie_probe_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa81d98a9ee58062c02be576fb0dfefd9)
- [pcie_set_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3516fec89df75eb3d77f54193059fc5c)
- [pcie_alloc_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad69ae431e5f91992f071dee9d7fa9110)
- [pcie_get_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaed7fef462ba02a22b5875b1a2c0d965a)
- [pcie_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafb69216f9224a9040b1f0b58eb286196)
- [pcie_get_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga56e724c9bfd7f44c550ccff1b46978a8)
- [pcie_get_ext_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5db0d2a5946d20406070b47a1a7acf21)
- [pcie_connect_dynamic_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga14970194de1024a1a4669b69f932a4f5)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pcie.h](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [pcie_bar::phys_addr](../platform_security_model_reference/P025_pcie_bar_结构体.md#a75ed340a7d80a6825f3c60469194dae8)
- [pcie_bar::size](../platform_security_model_reference/P025_pcie_bar_结构体.md#ab68c921f2993c94d2ae65684568bf770)
- [pcie_dev::id](../platform_security_model_reference/P028_pcie_dev_结构体.md#a5709ef678d9e81d4d3a61f6c26371076)
- [pcie_dev::class_rev_mask](../platform_security_model_reference/P028_pcie_dev_结构体.md#a798e25696997a74ed01f8df6cec64489)
- [pcie_dev::bdf](../platform_security_model_reference/P028_pcie_dev_结构体.md#a7cc2f61e85b1d9c4985115b91fc6e832)
- [pcie_dev::class_rev](../platform_security_model_reference/P028_pcie_dev_结构体.md#abedf281cdce4961dd02abba849747f45)
- [pcie_scan_opt::bus](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a036225c7a5730ba2040e03cab491b9da)
- [pcie_scan_opt::cb_data](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a11b39138d2a2b6b1e8e1bd80216a8da6)
- [pcie_scan_opt::cb](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a28ad6c4993eed7bdf08ce682692bf306)
- [pcie_scan_opt::flags](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#a7e485fb824dea16f9d5fdcb7079ebb7e)
- [pcie_scan_opt::scan_masking_fn](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md#af3b4de1e2cb9263ddcdc2849f5773be8)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_em32f967-pinctrl.h_源码浏览.md)
