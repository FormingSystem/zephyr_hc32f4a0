---
id: learning.zephyr-docs.api-source-register-time-reference.page-6
title: mdio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_mdio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="agroup__ethernet__mdio_html_ga304f668820ee91a63512c174e405b492"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371"></a>
<a id="agroup__ethernet__mdio_html_gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MDIO_H_
#define ZEPHYR_INCLUDE_NET_MDIO_H_


#ifdef __cplusplus
extern "C" {
#endif

enum mdio_opcode {
        MDIO_OP_C22_WRITE = 1,

        MDIO_OP_C22_READ = 2,

        MDIO_OP_C45_ADDRESS = 0,

        MDIO_OP_C45_WRITE = 1,

        MDIO_OP_C45_READ_INC = 2,

        MDIO_OP_C45_READ = 3
};

/* MDIO Manageable Device addresses */
#define MDIO_MMD_PMAPMD                 0x01U
#define MDIO_MMD_WIS                    0x02U
#define MDIO_MMD_PCS                    0x03U
#define MDIO_MMD_PHYXS                  0x04U
#define MDIO_MMD_DTEXS                  0x05U
#define MDIO_MMD_TC                     0x06U
#define MDIO_MMD_AN                     0x07U
#define MDIO_MMD_SEPARATED_PMA1         0x08U
#define MDIO_MMD_SEPARATED_PMA2         0x09U
#define MDIO_MMD_SEPARATED_PMA3         0x0AU
#define MDIO_MMD_SEPARATED_PMA4         0x0BU
#define MDIO_MMD_C22EXT                 0x1DU
#define MDIO_MMD_VENDOR_SPECIFIC1       0x1EU
#define MDIO_MMD_VENDOR_SPECIFIC2       0x1FU

/* MDIO generic registers */
#define MDIO_CTRL1                      0x0000U
#define MDIO_STAT1                      0x0001U
#define MDIO_DEVID1                     0x0002U
#define MDIO_DEVID2                     0x0003U
#define MDIO_SPEED                      0x0004U
#define MDIO_DEVS1                      0x0005U
#define MDIO_DEVS2                      0x0006U
#define MDIO_CTRL2                      0x0007U
#define MDIO_STAT2                      0x0008U
#define MDIO_PKGID1                     0x000EU
#define MDIO_PKGID2                     0x000FU
/* PCS Register: EEE capability Register */
#define MDIO_PCS_EEE_CAP                0x0014U
/* Auto-negotiation Register: EEE advertisement Register */
#define MDIO_AN_EEE_ADV                 0x003CU


/* BASE-T1 registers */
#define MDIO_AN_T1_CTRL                 0x0200U
#define MDIO_AN_T1_STAT                 0x0201U
#define MDIO_AN_T1_ADV_L                0x0202U
#define MDIO_AN_T1_ADV_M                0x0203U
#define MDIO_AN_T1_ADV_H                0x0204U
#define MDIO_AN_T1_LP_ADV_L             0x0205U
#define MDIO_AN_T1_LP_ADV_M             0x0206U
#define MDIO_AN_T1_LP_ADV_H             0x0207U

#define MDIO_PMA_PMD_BT1_CTRL           0x0834U

/* BASE-T1 Auto-negotiation Control register */
#define MDIO_AN_T1_CTRL_RESTART         BIT(9)
#define MDIO_AN_T1_CTRL_EN              BIT(12)

/* BASE-T1 Auto-negotiation Status register */
#define MDIO_AN_T1_STAT_LINK_STATUS     BIT(2)
#define MDIO_AN_T1_STAT_ABLE            BIT(3)
#define MDIO_AN_T1_STAT_REMOTE_FAULT    BIT(4)
#define MDIO_AN_T1_STAT_COMPLETE        BIT(5)
#define MDIO_AN_T1_STAT_PAGE_RX         BIT(6)

/* BASE-T1 Auto-negotiation Advertisement register [15:0] */
#define MDIO_AN_T1_ADV_L_PAUSE_CAP      BIT(10)
#define MDIO_AN_T1_ADV_L_PAUSE_ASYM     BIT(11)
#define MDIO_AN_T1_ADV_L_FORCE_MS       BIT(12)
#define MDIO_AN_T1_ADV_L_REMOTE_FAULT   BIT(13)
#define MDIO_AN_T1_ADV_L_ACK            BIT(14)
#define MDIO_AN_T1_ADV_L_NEXT_PAGE_REQ  BIT(15)

/* BASE-T1 Auto-negotiation Advertisement register [31:16] */
#define MDIO_AN_T1_ADV_M_B10L           BIT(14)
#define MDIO_AN_T1_ADV_M_MST            BIT(4)

/* BASE-T1 Auto-negotiation Advertisement register [47:32] */
#define MDIO_AN_T1_ADV_H_10L_TX_HI_REQ  BIT(12)
#define MDIO_AN_T1_ADV_H_10L_TX_HI      BIT(13)
#define MDIO_AN_T1_ADV_H_10L_EEE        BIT(14)

/* BASE-T1 PMA/PMD control register */
#define MDIO_PMA_PMD_BT1_CTRL_CFG_MST   BIT(14)


/* 10BASE-T1L registers */
#define MDIO_PMA_B10L_CTRL              0x08F6U
#define MDIO_PMA_B10L_STAT              0x08F7U
#define MDIO_PMA_B10L_TEST_CTRL         0x08F8U
#define MDIO_PMA_B10L_LINK_STAT         0x8302U
#define MDIO_PCS_B10L_CTRL              0x08E6U
#define MDIO_PCS_B10L_STAT              0x08E7U

/* 10BASE-T1L PMA control register */
#define MDIO_PMA_B10L_CTRL_TX_DIS_MODE_EN               BIT(14)
#define MDIO_PMA_B10L_CTRL_TX_LVL_HI                    BIT(12)
#define MDIO_PMA_B10L_CTRL_EEE                          BIT(10)
#define MDIO_PMA_B10L_CTRL_LB_PMA_LOC_EN                BIT(0)

/* 10BASE-T1L PMA status register */
#define MDIO_PMA_B10L_STAT_LINK                         BIT(0)
#define MDIO_PMA_B10L_STAT_FAULT                        BIT(1)
#define MDIO_PMA_B10L_STAT_POLARITY                     BIT(2)
#define MDIO_PMA_B10L_STAT_RECV_FAULT                   BIT(9)
#define MDIO_PMA_B10L_STAT_EEE                          BIT(10)
#define MDIO_PMA_B10L_STAT_LOW_POWER                    BIT(11)
#define MDIO_PMA_B10L_STAT_2V4_ABLE                     BIT(12)
#define MDIO_PMA_B10L_STAT_LB_ABLE                      BIT(13)

/* 10BASE-T1L test mode control register */
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_MASK          GENMASK(15, 13)
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_1             BIT(13)
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_2             BIT(14)
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_3             (BIT(13) | BIT(14))

/* 10BASE-T1L PMA link status*/
#define MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK_LL     BIT(9)
#define MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK        BIT(8)
#define MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK_LL     BIT(7)
#define MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK        BIT(6)
#define MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK_LL         BIT(5)
#define MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK            BIT(4)
#define MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK_LL         BIT(1)
#define MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK            BIT(0)

/* 10BASE-T1L PCS control */
#define MDIO_PCS_B10L_CTRL_LB_PCS_EN                    BIT(14)

/* 10BASE-T1L PCS status */
#define MDIO_PCS_B10L_STAT_DSCR_STAT_OK_LL              BIT(2)

/* Auto-negotiation Register: EEE advertisement Register */
#define MDIO_AN_EEE_ADV_1000T                           BIT(2)
#define MDIO_AN_EEE_ADV_100TX                           BIT(1)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_MDIO_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

管理数据输入／输出（MDIO）可管理设备地址。

### 注释 3：原第 79 行

MDIO 通用寄存器（generic registers）。

### 注释 4：原第 102 行

物理编码子层（PCS）寄存器：节能以太网（EEE）能力寄存器。

### 注释 5：原第 104 行

自动协商（Auto-negotiation）寄存器：EEE 通告寄存器（advertisement register）。

### 注释 6：原第 108 行

BASE-T1 寄存器。

### 注释 7：原第 129 行

BASE-T1 自动协商控制寄存器（Control register）。

### 注释 8：原第 135 行

BASE-T1 自动协商状态寄存器（Status register）。

### 注释 9：原第 147 行

BASE-T1 自动协商通告寄存器（Advertisement register），位 `[15:0]`。

### 注释 10：原第 161 行

BASE-T1 自动协商通告寄存器，位 `[31:16]`。

### 注释 11：原第 167 行

BASE-T1 自动协商通告寄存器，位 `[47:32]`。

### 注释 12：原第 175 行

BASE-T1 物理介质连接／物理介质相关子层（PMA/PMD）控制寄存器。

### 注释 13：原第 180 行

10BASE-T1L 寄存器。

### 注释 14：原第 194 行

10BASE-T1L 物理介质连接子层（PMA）控制寄存器。

### 注释 15：原第 204 行

10BASE-T1L PMA 状态寄存器。

### 注释 16：原第 222 行

10BASE-T1L 测试模式控制寄存器（test mode control register）。

### 注释 17：原第 232 行

10BASE-T1L PMA 链路状态（link status）。

### 注释 18：原第 250 行

10BASE-T1L 物理编码子层（PCS）控制。

### 注释 19：原第 254 行

10BASE-T1L PCS 状态。

### 注释 20：原第 258 行

自动协商（Auto-negotiation）寄存器：EEE 通告寄存器（advertisement register）。

### 注释 21：原第 272 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MDIO_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h.html)
- [mdio_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga304f668820ee91a63512c174e405b492)
- [MDIO_OP_C22_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d)
- [MDIO_OP_C22_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46)
- [MDIO_OP_C45_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371)
- [MDIO_OP_C45_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f)
- [MDIO_OP_C45_READ_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd)
- [MDIO_OP_C45_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1)

---

[上一章](P005_msi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_numaker_m46x_clock.h_源码浏览.md)
