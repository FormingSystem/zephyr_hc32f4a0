---
id: learning.zephyr-docs.api-file-runtime-reference.page-56
title: zephyr__dt-bindings__clock__renesas_rzg_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rzg__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_zephyr\_\_dt-bindings\_\_clock\_\_renesas\_rzg\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rzg__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 56.1\_宏定义（Macros）

<a id="r_af22fb58317528ced8ad8cdfc399ad2ac"></a>

```c
#define RZ_IP_MASK 0xFF000000UL
```

相关声明：[RZ_IP_MASK](#af22fb58317528ced8ad8cdfc399ad2ac)。

RZ 时钟配置值（Clock Configuration Values）。

<a id="r_a0bfeafa5676753c0e6750a9c3c2f18f1"></a>

```c
#define RZ_IP_SHIFT 24UL
```

相关声明：[RZ_IP_SHIFT](#a0bfeafa5676753c0e6750a9c3c2f18f1)。

<a id="r_a73baaadd858826d7b7e613120a9e4509"></a>

```c
#define RZ_IP_CH_MASK 0xFF0000UL
```

相关声明：[RZ_IP_CH_MASK](#a73baaadd858826d7b7e613120a9e4509)。

<a id="r_a4854f76eb8144726dcc49da30bb49494"></a>

```c
#define RZ_IP_CH_SHIFT 16UL
```

相关声明：[RZ_IP_CH_SHIFT](#a4854f76eb8144726dcc49da30bb49494)。

<a id="r_a9712059a7005130fbeb48f2ce7f45f66"></a>

```c
#define RZ_CLOCK_MASK 0xFF00UL
```

相关声明：[RZ_CLOCK_MASK](#a9712059a7005130fbeb48f2ce7f45f66)。

<a id="r_a0f4444cd8f843699d43be43968a76f60"></a>

```c
#define RZ_CLOCK_SHIFT 8UL
```

相关声明：[RZ_CLOCK_SHIFT](#a0f4444cd8f843699d43be43968a76f60)。

<a id="r_a68e6f2ee01f4ba23c076f5a0c3574ec3"></a>

```c
#define RZ_CLOCK_DIV_MASK 0xFFUL
```

相关声明：[RZ_CLOCK_DIV_MASK](#a68e6f2ee01f4ba23c076f5a0c3574ec3)。

<a id="r_a2a394bb9c50b68c2c0b4250d529e96fa"></a>

```c
#define RZ_CLOCK_DIV_SHIFT 0UL
```

相关声明：[RZ_CLOCK_DIV_SHIFT](#a2a394bb9c50b68c2c0b4250d529e96fa)。

<a id="r_a85c1cd03e46043357e15c2020cf8db25"></a>

```c
#define RZ_IP_GTM 0UL /* General Timer */
```

相关声明：[RZ_IP_GTM](#a85c1cd03e46043357e15c2020cf8db25)。

<a id="r_a258d150ad8458cb580f823296dd4b863"></a>

```c
#define RZ_IP_GPT 1UL /* General PWM Timer */
```

相关声明：[RZ_IP_GPT](#a258d150ad8458cb580f823296dd4b863)。

<a id="r_a55ab8413b73bfe6a7de0b5eef4c9575f"></a>

```c
#define RZ_IP_SCI 2UL /* Serial Communications Interface */
```

相关声明：[RZ_IP_SCI](#a55ab8413b73bfe6a7de0b5eef4c9575f)。

<a id="r_a4d01bb6e25a7d8f0cc520efd1693f6b0"></a>

```c
#define RZ_IP_SCIF 3UL /* Serial Communications Interface with FIFO */
```

相关声明：[RZ_IP_SCIF](#a4d01bb6e25a7d8f0cc520efd1693f6b0)。

<a id="r_a20be7b897467fae2e11d31b9404db77e"></a>

```c
#define RZ_IP_RIIC 4UL /* I2C Bus Interface */
```

相关声明：[RZ_IP_RIIC](#a20be7b897467fae2e11d31b9404db77e)。

<a id="r_abe3258c6780f7e818d6a0bfa621c0c39"></a>

```c
#define RZ_IP_RSPI 5UL /* Renesas Serial Peripheral Interface */
```

相关声明：[RZ_IP_RSPI](#abe3258c6780f7e818d6a0bfa621c0c39)。

<a id="r_a545f1dab775039d3e00320f4c2fa2266"></a>

```c
#define RZ_IP_MHU 6UL /* Message Handling Unit */
```

相关声明：[RZ_IP_MHU](#a545f1dab775039d3e00320f4c2fa2266)。

<a id="r_a6fb0a952bce1f87fdc485e3407885aab"></a>

```c
#define RZ_IP_DMAC 7UL /* Direct Memory Access Controller */
```

相关声明：[RZ_IP_DMAC](#a6fb0a952bce1f87fdc485e3407885aab)。

<a id="r_a2a5b46c7954d9931d05ba9b78b6bfa92"></a>

```c
#define RZ_IP_CANFD 8UL /* CANFD Interface (RS-CANFD) */
```

相关声明：[RZ_IP_CANFD](#a2a5b46c7954d9931d05ba9b78b6bfa92)。

<a id="r_ad6e07b47929a05a957f6685c8207a0d4"></a>

```c
#define RZ_IP_ADC 9UL /* A/D Converter */
```

相关声明：[RZ_IP_ADC](#ad6e07b47929a05a957f6685c8207a0d4)。

<a id="r_ab878f4db036145eb3c62d9e2c55d0167"></a>

```c
#define RZ_IP_WDT 10UL /* Watchdog Timer */
```

相关声明：[RZ_IP_WDT](#ab878f4db036145eb3c62d9e2c55d0167)。

<a id="r_a244252c9570d2ce5142a1dacb71aca93"></a>

```c
#define RZ_CLOCK_ICLK 0UL /* Cortex-A55 Clock */
```

相关声明：[RZ_CLOCK_ICLK](#a244252c9570d2ce5142a1dacb71aca93)。

<a id="r_a9970fbd46cf921c331ad693053100e6f"></a>

```c
#define RZ_CLOCK_I2CLK 1UL /* Cortex-M33 Clock */
```

相关声明：[RZ_CLOCK_I2CLK](#a9970fbd46cf921c331ad693053100e6f)。

<a id="r_a19ef59ea7eadc3ef12705e6bcd650cfc"></a>

```c
#define RZ_CLOCK_I3CLK 2UL /* Cortex-M33 FPU Clock */
```

相关声明：[RZ_CLOCK_I3CLK](#a19ef59ea7eadc3ef12705e6bcd650cfc)。

<a id="r_af7ba3a355a4c56b7c2700d4179bece3f"></a>

```c
#define RZ_CLOCK_S0CLK 3UL /* DDR-PHY Clock */
```

相关声明：[RZ_CLOCK_S0CLK](#af7ba3a355a4c56b7c2700d4179bece3f)。

<a id="r_a8558bb747c644c3ba838d0b564fef57b"></a>

```c
#define RZ_CLOCK_OC0CLK 4UL /* OCTA0 Clock */
```

相关声明：[RZ_CLOCK_OC0CLK](#a8558bb747c644c3ba838d0b564fef57b)。

<a id="r_abe1148e7058c4e6997c83e86470e1784"></a>

```c
#define RZ_CLOCK_OC1CLK 5UL /* OCTA1 Clock */
```

相关声明：[RZ_CLOCK_OC1CLK](#abe1148e7058c4e6997c83e86470e1784)。

<a id="r_ab4e5d3a27f25df5591d3170f2e944e0f"></a>

```c
#define RZ_CLOCK_SPI0CLK 6UL /* SPI0 Clock */
```

相关声明：[RZ_CLOCK_SPI0CLK](#ab4e5d3a27f25df5591d3170f2e944e0f)。

<a id="r_ab02c603153146d64db7a98b4f332a7d5"></a>

```c
#define RZ_CLOCK_SPI1CLK 7UL /* SPI1 Clock */
```

相关声明：[RZ_CLOCK_SPI1CLK](#ab02c603153146d64db7a98b4f332a7d5)。

<a id="r_af49247c2ed779dc006ce90a7cdf3a8c1"></a>

```c
#define RZ_CLOCK_SD0CLK 8UL /* SDH0 Clock */
```

相关声明：[RZ_CLOCK_SD0CLK](#af49247c2ed779dc006ce90a7cdf3a8c1)。

<a id="r_a17b5762dca74eb50645508737085f6c1"></a>

```c
#define RZ_CLOCK_SD1CLK 9UL /* SDH1 Clock */
```

相关声明：[RZ_CLOCK_SD1CLK](#a17b5762dca74eb50645508737085f6c1)。

<a id="r_a9b9efa69cb954f3bd2e590974f2f5b68"></a>

```c
#define RZ_CLOCK_SD2CLK 10UL /* SDH2 Clock */
```

相关声明：[RZ_CLOCK_SD2CLK](#a9b9efa69cb954f3bd2e590974f2f5b68)。

<a id="r_ab42089566bde80f80a5a672c39f5f4a9"></a>

```c
#define RZ_CLOCK_M0CLK 11UL /* VCP LCDC Clock */
```

相关声明：[RZ_CLOCK_M0CLK](#ab42089566bde80f80a5a672c39f5f4a9)。

<a id="r_a357ba27e1964a6f63d756d957213a94d"></a>

```c
#define RZ_CLOCK_HPCLK 12UL /* Ethernet Clock */
```

相关声明：[RZ_CLOCK_HPCLK](#a357ba27e1964a6f63d756d957213a94d)。

<a id="r_a622f3e70a5fe08a61474322492130319"></a>

```c
#define RZ_CLOCK_TSUCLK 13UL /* TSU Clock */
```

相关声明：[RZ_CLOCK_TSUCLK](#a622f3e70a5fe08a61474322492130319)。

<a id="r_a67327a7c0fcff2dc0374a0fbde6422c6"></a>

```c
#define RZ_CLOCK_ZTCLK 14UL /* JAUTH Clock */
```

相关声明：[RZ_CLOCK_ZTCLK](#a67327a7c0fcff2dc0374a0fbde6422c6)。

<a id="r_a43f77faab57d93e59c93956572ed73a5"></a>

```c
#define RZ_CLOCK_P0CLK 15UL /* APB-BUS Clock */
```

相关声明：[RZ_CLOCK_P0CLK](#a43f77faab57d93e59c93956572ed73a5)。

<a id="r_a960f074fd0a8e9ea8c5b02a4d6d977c9"></a>

```c
#define RZ_CLOCK_P1CLK 16UL /* AXI-BUS Clock */
```

相关声明：[RZ_CLOCK_P1CLK](#a960f074fd0a8e9ea8c5b02a4d6d977c9)。

<a id="r_a794d8d5f1cb8a2df70ca2ab4caf2b049"></a>

```c
#define RZ_CLOCK_P2CLK 17UL /* P2CLK */
```

相关声明：[RZ_CLOCK_P2CLK](#a794d8d5f1cb8a2df70ca2ab4caf2b049)。

<a id="r_a2dbb22921c00fb5398666f595da080d9"></a>

```c
#define RZ_CLOCK_P3CLK 18UL /* P3CLK */
```

相关声明：[RZ_CLOCK_P3CLK](#a2dbb22921c00fb5398666f595da080d9)。

<a id="r_a3e09739b70bf6fbcd7cb3a72002c0339"></a>

```c
#define RZ_CLOCK_P4CLK 19UL /* P4CLK */
```

相关声明：[RZ_CLOCK_P4CLK](#a3e09739b70bf6fbcd7cb3a72002c0339)。

<a id="r_a764d5d9af4b6ef76a903f93f15f53b74"></a>

```c
#define RZ_CLOCK_P5CLK 20UL /* P5CLK */
```

相关声明：[RZ_CLOCK_P5CLK](#a764d5d9af4b6ef76a903f93f15f53b74)。

<a id="r_a7b51d8e0e38165e26975696bf90d834b"></a>

```c
#define RZ_CLOCK_ATCLK 21UL /* ATCLK */
```

相关声明：[RZ_CLOCK_ATCLK](#a7b51d8e0e38165e26975696bf90d834b)。

<a id="r_a800d72bacbe85d766ed0e027b28b36c8"></a>

```c
#define RZ_CLOCK_OSCCLK 22UL /* OSC Clock */
```

相关声明：[RZ_CLOCK_OSCCLK](#a800d72bacbe85d766ed0e027b28b36c8)。

<a id="r_a4811a342819ebdb27d9ad77aa3bfc48e"></a>

```c
#define RZ_CLOCK_OSCCLK2 23UL /* OSC2 Clock */
```

相关声明：[RZ_CLOCK_OSCCLK2](#a4811a342819ebdb27d9ad77aa3bfc48e)。

<a id="r_af2b6678567dacec847501d2a634b7773"></a>

```c
#define RZ_CLOCK(IP, ch, clk, div)
```

相关声明：[RZ_CLOCK](#af2b6678567dacec847501d2a634b7773)。

<a id="r_ab5ba6102fd209a05b2a5cce69874594a"></a>

```c
#define RZ_CLOCK_SCIF(ch)
```

相关声明：[RZ_CLOCK_SCIF](#ab5ba6102fd209a05b2a5cce69874594a)。

将时钟配置（Clock Configurations）打包为 32 位值，符合 Renesas RZ/G 设备树（Devicetree）`clocks` 属性的要求。

<a id="r_adda08ff063353c356bae99dada0352c8"></a>

```c
#define RZ_CLOCK_GPT(ch)
```

相关声明：[RZ_CLOCK_GPT](#adda08ff063353c356bae99dada0352c8)。

<a id="r_ab7297a9bbf3181ab73f1ea0e2c67decd"></a>

```c
#define RZ_CLOCK_MHU(ch)
```

相关声明：[RZ_CLOCK_MHU](#ab7297a9bbf3181ab73f1ea0e2c67decd)。

<a id="r_aabe15d33711286e3c8a9a99774afffc4"></a>

```c
#define RZ_CLOCK_ADC(ch)
```

相关声明：[RZ_CLOCK_ADC](#aabe15d33711286e3c8a9a99774afffc4)。

<a id="r_ae138403b21ab0a308312072d1ffa06f1"></a>

```c
#define RZ_CLOCK_RIIC(ch)
```

相关声明：[RZ_CLOCK_RIIC](#ae138403b21ab0a308312072d1ffa06f1)。

<a id="r_a435c6e38774d8d95067cb4e7513dd74d"></a>

```c
#define RZ_CLOCK_GTM(ch)
```

相关声明：[RZ_CLOCK_GTM](#a435c6e38774d8d95067cb4e7513dd74d)。

<a id="r_a637295af9157f6757bed145911ca2a3a"></a>

```c
#define RZ_CLOCK_CANFD(ch)
```

相关声明：[RZ_CLOCK_CANFD](#a637295af9157f6757bed145911ca2a3a)。

<a id="r_a566a4e447745ff7d5ed3b4d0dd0fa666"></a>

```c
#define RZ_CLOCK_RSPI(ch)
```

相关声明：[RZ_CLOCK_RSPI](#a566a4e447745ff7d5ed3b4d0dd0fa666)。

<a id="r_a3a3baef1dbd6eae8f7d54a0610521aa0"></a>

```c
#define RZ_CLOCK_DMAC(ch)
```

相关声明：[RZ_CLOCK_DMAC](#a3a3baef1dbd6eae8f7d54a0610521aa0)。

<a id="r_a477c2bd85544839e9d884a9c85c2e4a0"></a>

```c
#define RZ_CLOCK_SCI(ch)
```

相关声明：[RZ_CLOCK_SCI](#a477c2bd85544839e9d884a9c85c2e4a0)。

<a id="r_a92f53013086d2defebaf0f7157450c31"></a>

```c
#define RZ_CLOCK_WDT(ch)
```

相关声明：[RZ_CLOCK_WDT](#a92f53013086d2defebaf0f7157450c31)。

## 56.2\_详细说明（Detailed Documentation）

<a id="af2b6678567dacec847501d2a634b7773"></a>

### `RZ_CLOCK`

```c
#define RZ_CLOCK ( IP, ch, clk, div )
```

展开值（Value）：

```c
((RZ_IP_##IP << RZ_IP_SHIFT) | ((ch) << RZ_IP_CH_SHIFT) | ((clk) << RZ_CLOCK_SHIFT) |      \
 ((div) << RZ_CLOCK_DIV_SHIFT))
```

<a id="aabe15d33711286e3c8a9a99774afffc4"></a>

### `RZ_CLOCK_ADC`

```c
#define RZ_CLOCK_ADC ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(ADC, ch, RZ_CLOCK_TSUCLK, 1)
```

<a id="a7b51d8e0e38165e26975696bf90d834b"></a>

### `RZ_CLOCK_ATCLK`

```c
#define RZ_CLOCK_ATCLK 21UL /* ATCLK */
```

<a id="a637295af9157f6757bed145911ca2a3a"></a>

### `RZ_CLOCK_CANFD`

```c
#define RZ_CLOCK_CANFD ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(CANFD, ch, RZ_CLOCK_P4CLK, 2)
```

<a id="a68e6f2ee01f4ba23c076f5a0c3574ec3"></a>

### `RZ_CLOCK_DIV_MASK`

```c
#define RZ_CLOCK_DIV_MASK 0xFFUL
```

<a id="a2a394bb9c50b68c2c0b4250d529e96fa"></a>

### `RZ_CLOCK_DIV_SHIFT`

```c
#define RZ_CLOCK_DIV_SHIFT 0UL
```

<a id="a3a3baef1dbd6eae8f7d54a0610521aa0"></a>

### `RZ_CLOCK_DMAC`

```c
#define RZ_CLOCK_DMAC ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(DMAC, ch, RZ_CLOCK_P3CLK, 1)
```

<a id="adda08ff063353c356bae99dada0352c8"></a>

### `RZ_CLOCK_GPT`

```c
#define RZ_CLOCK_GPT ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(GPT, ch, RZ_CLOCK_P0CLK, 1)
```

<a id="a435c6e38774d8d95067cb4e7513dd74d"></a>

### `RZ_CLOCK_GTM`

```c
#define RZ_CLOCK_GTM ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(GTM, ch, RZ_CLOCK_P0CLK, 1)
```

<a id="a357ba27e1964a6f63d756d957213a94d"></a>

### `RZ_CLOCK_HPCLK`

```c
#define RZ_CLOCK_HPCLK 12UL /* Ethernet Clock */
```

<a id="a9970fbd46cf921c331ad693053100e6f"></a>

### `RZ_CLOCK_I2CLK`

```c
#define RZ_CLOCK_I2CLK 1UL /* Cortex-M33 Clock */
```

<a id="a19ef59ea7eadc3ef12705e6bcd650cfc"></a>

### `RZ_CLOCK_I3CLK`

```c
#define RZ_CLOCK_I3CLK 2UL /* Cortex-M33 FPU Clock */
```

<a id="a244252c9570d2ce5142a1dacb71aca93"></a>

### `RZ_CLOCK_ICLK`

```c
#define RZ_CLOCK_ICLK 0UL /* Cortex-A55 Clock */
```

<a id="ab42089566bde80f80a5a672c39f5f4a9"></a>

### `RZ_CLOCK_M0CLK`

```c
#define RZ_CLOCK_M0CLK 11UL /* VCP LCDC Clock */
```

<a id="a9712059a7005130fbeb48f2ce7f45f66"></a>

### `RZ_CLOCK_MASK`

```c
#define RZ_CLOCK_MASK 0xFF00UL
```

<a id="ab7297a9bbf3181ab73f1ea0e2c67decd"></a>

### `RZ_CLOCK_MHU`

```c
#define RZ_CLOCK_MHU ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(MHU, ch, RZ_CLOCK_P1CLK, 2)
```

<a id="a8558bb747c644c3ba838d0b564fef57b"></a>

### `RZ_CLOCK_OC0CLK`

```c
#define RZ_CLOCK_OC0CLK 4UL /* OCTA0 Clock */
```

<a id="abe1148e7058c4e6997c83e86470e1784"></a>

### `RZ_CLOCK_OC1CLK`

```c
#define RZ_CLOCK_OC1CLK 5UL /* OCTA1 Clock */
```

<a id="a800d72bacbe85d766ed0e027b28b36c8"></a>

### `RZ_CLOCK_OSCCLK`

```c
#define RZ_CLOCK_OSCCLK 22UL /* OSC Clock */
```

<a id="a4811a342819ebdb27d9ad77aa3bfc48e"></a>

### `RZ_CLOCK_OSCCLK2`

```c
#define RZ_CLOCK_OSCCLK2 23UL /* OSC2 Clock */
```

<a id="a43f77faab57d93e59c93956572ed73a5"></a>

### `RZ_CLOCK_P0CLK`

```c
#define RZ_CLOCK_P0CLK 15UL /* APB-BUS Clock */
```

<a id="a960f074fd0a8e9ea8c5b02a4d6d977c9"></a>

### `RZ_CLOCK_P1CLK`

```c
#define RZ_CLOCK_P1CLK 16UL /* AXI-BUS Clock */
```

<a id="a794d8d5f1cb8a2df70ca2ab4caf2b049"></a>

### `RZ_CLOCK_P2CLK`

```c
#define RZ_CLOCK_P2CLK 17UL /* P2CLK */
```

<a id="a2dbb22921c00fb5398666f595da080d9"></a>

### `RZ_CLOCK_P3CLK`

```c
#define RZ_CLOCK_P3CLK 18UL /* P3CLK */
```

<a id="a3e09739b70bf6fbcd7cb3a72002c0339"></a>

### `RZ_CLOCK_P4CLK`

```c
#define RZ_CLOCK_P4CLK 19UL /* P4CLK */
```

<a id="a764d5d9af4b6ef76a903f93f15f53b74"></a>

### `RZ_CLOCK_P5CLK`

```c
#define RZ_CLOCK_P5CLK 20UL /* P5CLK */
```

<a id="ae138403b21ab0a308312072d1ffa06f1"></a>

### `RZ_CLOCK_RIIC`

```c
#define RZ_CLOCK_RIIC ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(RIIC, ch, RZ_CLOCK_P0CLK, 1)
```

<a id="a566a4e447745ff7d5ed3b4d0dd0fa666"></a>

### `RZ_CLOCK_RSPI`

```c
#define RZ_CLOCK_RSPI ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(RSPI, ch, RZ_CLOCK_P0CLK, 1)
```

<a id="af7ba3a355a4c56b7c2700d4179bece3f"></a>

### `RZ_CLOCK_S0CLK`

```c
#define RZ_CLOCK_S0CLK 3UL /* DDR-PHY Clock */
```

<a id="a477c2bd85544839e9d884a9c85c2e4a0"></a>

### `RZ_CLOCK_SCI`

```c
#define RZ_CLOCK_SCI ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(SCI, ch, RZ_CLOCK_P0CLK, 1)
```

<a id="ab5ba6102fd209a05b2a5cce69874594a"></a>

### `RZ_CLOCK_SCIF`

```c
#define RZ_CLOCK_SCIF ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(SCIF, ch, RZ_CLOCK_P0CLK, 1)
```

将时钟配置（Clock Configurations）打包为 32 位值，符合 Renesas RZ/G 设备树（Devicetree）`clocks` 属性的要求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ch` | 外设通道／单元（Peripheral Channel / Unit）。 |

<a id="af49247c2ed779dc006ce90a7cdf3a8c1"></a>

### `RZ_CLOCK_SD0CLK`

```c
#define RZ_CLOCK_SD0CLK 8UL /* SDH0 Clock */
```

<a id="a17b5762dca74eb50645508737085f6c1"></a>

### `RZ_CLOCK_SD1CLK`

```c
#define RZ_CLOCK_SD1CLK 9UL /* SDH1 Clock */
```

<a id="a9b9efa69cb954f3bd2e590974f2f5b68"></a>

### `RZ_CLOCK_SD2CLK`

```c
#define RZ_CLOCK_SD2CLK 10UL /* SDH2 Clock */
```

<a id="a0f4444cd8f843699d43be43968a76f60"></a>

### `RZ_CLOCK_SHIFT`

```c
#define RZ_CLOCK_SHIFT 8UL
```

<a id="ab4e5d3a27f25df5591d3170f2e944e0f"></a>

### `RZ_CLOCK_SPI0CLK`

```c
#define RZ_CLOCK_SPI0CLK 6UL /* SPI0 Clock */
```

<a id="ab02c603153146d64db7a98b4f332a7d5"></a>

### `RZ_CLOCK_SPI1CLK`

```c
#define RZ_CLOCK_SPI1CLK 7UL /* SPI1 Clock */
```

<a id="a622f3e70a5fe08a61474322492130319"></a>

### `RZ_CLOCK_TSUCLK`

```c
#define RZ_CLOCK_TSUCLK 13UL /* TSU Clock */
```

<a id="a92f53013086d2defebaf0f7157450c31"></a>

### `RZ_CLOCK_WDT`

```c
#define RZ_CLOCK_WDT ( ch)
```

展开值（Value）：

```c
RZ_CLOCK(WDT, ch, RZ_CLOCK_OSCCLK, 1)
```

<a id="a67327a7c0fcff2dc0374a0fbde6422c6"></a>

### `RZ_CLOCK_ZTCLK`

```c
#define RZ_CLOCK_ZTCLK 14UL /* JAUTH Clock */
```

<a id="ad6e07b47929a05a957f6685c8207a0d4"></a>

### `RZ_IP_ADC`

```c
#define RZ_IP_ADC 9UL /* A/D Converter */
```

<a id="a2a5b46c7954d9931d05ba9b78b6bfa92"></a>

### `RZ_IP_CANFD`

```c
#define RZ_IP_CANFD 8UL /* CANFD Interface (RS-CANFD) */
```

<a id="a73baaadd858826d7b7e613120a9e4509"></a>

### `RZ_IP_CH_MASK`

```c
#define RZ_IP_CH_MASK 0xFF0000UL
```

<a id="a4854f76eb8144726dcc49da30bb49494"></a>

### `RZ_IP_CH_SHIFT`

```c
#define RZ_IP_CH_SHIFT 16UL
```

<a id="a6fb0a952bce1f87fdc485e3407885aab"></a>

### `RZ_IP_DMAC`

```c
#define RZ_IP_DMAC 7UL /* Direct Memory Access Controller */
```

<a id="a258d150ad8458cb580f823296dd4b863"></a>

### `RZ_IP_GPT`

```c
#define RZ_IP_GPT 1UL /* General PWM Timer */
```

<a id="a85c1cd03e46043357e15c2020cf8db25"></a>

### `RZ_IP_GTM`

```c
#define RZ_IP_GTM 0UL /* General Timer */
```

<a id="af22fb58317528ced8ad8cdfc399ad2ac"></a>

### `RZ_IP_MASK`

```c
#define RZ_IP_MASK 0xFF000000UL
```

RZ 时钟配置值（Clock Configuration Values）。

<a id="a545f1dab775039d3e00320f4c2fa2266"></a>

### `RZ_IP_MHU`

```c
#define RZ_IP_MHU 6UL /* Message Handling Unit */
```

<a id="a20be7b897467fae2e11d31b9404db77e"></a>

### `RZ_IP_RIIC`

```c
#define RZ_IP_RIIC 4UL /* I2C Bus Interface */
```

<a id="abe3258c6780f7e818d6a0bfa621c0c39"></a>

### `RZ_IP_RSPI`

```c
#define RZ_IP_RSPI 5UL /* Renesas Serial Peripheral Interface */
```

<a id="a55ab8413b73bfe6a7de0b5eef4c9575f"></a>

### `RZ_IP_SCI`

```c
#define RZ_IP_SCI 2UL /* Serial Communications Interface */
```

<a id="a4d01bb6e25a7d8f0cc520efd1693f6b0"></a>

### `RZ_IP_SCIF`

```c
#define RZ_IP_SCIF 3UL /* Serial Communications Interface with FIFO */
```

<a id="a0bfeafa5676753c0e6750a9c3c2f18f1"></a>

### `RZ_IP_SHIFT`

```c
#define RZ_IP_SHIFT 24UL
```

<a id="ab878f4db036145eb3c62d9e2c55d0167"></a>

### `RZ_IP_WDT`

```c
#define RZ_IP_WDT 10UL /* Watchdog Timer */
```


## 56.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rzg__clock_8h_source.html)
- [RZ_IP_SHIFT](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a0bfeafa5676753c0e6750a9c3c2f18f1)
- [RZ_IP_CH_SHIFT](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a4854f76eb8144726dcc49da30bb49494)
- [RZ_CLOCK_SHIFT](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a0f4444cd8f843699d43be43968a76f60)
- [RZ_CLOCK_DIV_SHIFT](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a2a394bb9c50b68c2c0b4250d529e96fa)
- [RZ_CLOCK](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#af2b6678567dacec847501d2a634b7773)
- [RZ_CLOCK_TSUCLK](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a622f3e70a5fe08a61474322492130319)
- [RZ_CLOCK_P0CLK](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a43f77faab57d93e59c93956572ed73a5)
- [RZ_CLOCK_P1CLK](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a960f074fd0a8e9ea8c5b02a4d6d977c9)
- [RZ_CLOCK_OSCCLK](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md#a800d72bacbe85d766ed0e027b28b36c8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arenesas__rza__clock_8h_html_a0bfeafa5676753c0e6750a9c3c2f18f1"></a>
<a id="arenesas__rza__clock_8h_html_a0f4444cd8f843699d43be43968a76f60"></a>
<a id="arenesas__rza__clock_8h_html_a2a394bb9c50b68c2c0b4250d529e96fa"></a>
<a id="arenesas__rza__clock_8h_html_a4854f76eb8144726dcc49da30bb49494"></a>
<a id="arenesas__rza__clock_8h_html_a622f3e70a5fe08a61474322492130319"></a>
<a id="arenesas__rza__clock_8h_html_af2b6678567dacec847501d2a634b7773"></a>
<a id="arenesas__rzg__clock_8h_html_a3e09739b70bf6fbcd7cb3a72002c0339"></a>
<a id="arenesas__rzg__clock_8h_html_a2dbb22921c00fb5398666f595da080d9"></a>
<a id="arenesas__rza__clock_8h_html_a43f77faab57d93e59c93956572ed73a5"></a>
<a id="arenesas__rza__clock_8h_html_a960f074fd0a8e9ea8c5b02a4d6d977c9"></a>
<a id="arenesas__rza__clock_8h_html_a800d72bacbe85d766ed0e027b28b36c8"></a>

---

[上一章](P055_zephyr__drivers__clock_control__renesas_rcar_generic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P057_zephyr__bluetooth__mesh__rpr.h_文件参考.md)
