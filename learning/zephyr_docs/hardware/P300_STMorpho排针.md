---
id: learning.zephyr-docs.hardware.headers-9
title: STMorpho排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第300章\_STMorpho排针

原文：[group__st-morpho-header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 300.1\_接口与术语

本页定义ST Morpho排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/st-morpho-header.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

左侧（Left，L）和右侧（Right，R）各列出72个位置，原常量值分别为0—71与72—143。引脚掩码（Pin Mask）保留为 `0xFF`；“0...143”是原文列出的引脚编码范围。

## 300.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ST_MORPHO_PIN_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf4c4ac0e90f06a1c438e83e86e43efc4) | `0xFF` | ST Morpho引脚掩码（0...143） | ST Morpho pin mask (0...143). |
| [`ST_MORPHO_L_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaec4c885872fcd25043c88cc7880d1bdf) | `0` | 左侧引脚1 | Left pin 1. |
| [`ST_MORPHO_L_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga744eb2f0189e6b835089f326ebca37ae) | `1` | 左侧引脚2 | Left pin 2. |
| [`ST_MORPHO_L_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf15169af46408875b02a910a7d05b7cf) | `2` | 左侧引脚3 | Left pin 3. |
| [`ST_MORPHO_L_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga71bb4a5d49826e7344f8273abbf6f1ff) | `3` | 左侧引脚4 | Left pin 4. |
| [`ST_MORPHO_L_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga79601a70183288c3596590db02dfc917) | `4` | 左侧引脚5 | Left pin 5. |
| [`ST_MORPHO_L_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga3927476a33f62b76929d2f3a81f3fc51) | `5` | 左侧引脚6 | Left pin 6. |
| [`ST_MORPHO_L_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf98087926d93feb66169d2caf3da9783) | `6` | 左侧引脚7 | Left pin 7. |
| [`ST_MORPHO_L_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8f6b6a3768553753297cd9c9486f81a4) | `7` | 左侧引脚8 | Left pin 8. |
| [`ST_MORPHO_L_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga9a48e48a738a741a88016bba35c7db1d) | `8` | 左侧引脚9 | Left pin 9. |
| [`ST_MORPHO_L_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga39612dc32c4583b7809e415256e4f2f7) | `9` | 左侧引脚10 | Left pin 10. |
| [`ST_MORPHO_L_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5c118461a72ed3af45f0b6a9dd100ec2) | `10` | 左侧引脚11 | Left pin 11. |
| [`ST_MORPHO_L_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2e35b0d8cff585595670787bc7e5fcc8) | `11` | 左侧引脚12 | Left pin 12. |
| [`ST_MORPHO_L_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga019a15fb232bb2c90f0cf5250b47a760) | `12` | 左侧引脚13 | Left pin 13. |
| [`ST_MORPHO_L_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa10fb53090b113f8b895d5c175ab7d3e) | `13` | 左侧引脚14 | Left pin 14. |
| [`ST_MORPHO_L_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga6b1b1cc46ff81837cbd10d8affd25759) | `14` | 左侧引脚15 | Left pin 15. |
| [`ST_MORPHO_L_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2e947a6508d8aded395f124f236833ce) | `15` | 左侧引脚16 | Left pin 16. |
| [`ST_MORPHO_L_17`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga126800c0af4e120058aa29374c32dfca) | `16` | 左侧引脚17 | Left pin 17. |
| [`ST_MORPHO_L_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga360ad282e32c2db75df167a5429b1c8e) | `17` | 左侧引脚18 | Left pin 18. |
| [`ST_MORPHO_L_19`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga743a3ab1466157e594f1f1df20078add) | `18` | 左侧引脚19 | Left pin 19. |
| [`ST_MORPHO_L_20`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga599429ea62f56ce446a34471a2820ec1) | `19` | 左侧引脚20 | Left pin 20. |
| [`ST_MORPHO_L_21`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa8f7f6e01bf12283e62524b857ab157c) | `20` | 左侧引脚21 | Left pin 21. |
| [`ST_MORPHO_L_22`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaaa1e799292c758f4d49a3b1e15320fb1) | `21` | 左侧引脚22 | Left pin 22. |
| [`ST_MORPHO_L_23`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8fba61554ce080c859f0fcc1b8dc6ba4) | `22` | 左侧引脚23 | Left pin 23. |
| [`ST_MORPHO_L_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga86c15c33304c5d9cf6780e0fb0f1f5c8) | `23` | 左侧引脚24 | Left pin 24. |
| [`ST_MORPHO_L_25`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gad8a92064e906d255260739a870049d62) | `24` | 左侧引脚25 | Left pin 25. |
| [`ST_MORPHO_L_26`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaab2a3b7a8debcf2201a5eb1dd187276c) | `25` | 左侧引脚26 | Left pin 26. |
| [`ST_MORPHO_L_27`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gabcc82dfc6bcf802d46526f6027e3fd7e) | `26` | 左侧引脚27 | Left pin 27. |
| [`ST_MORPHO_L_28`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga305100e4f83503828b13a9db76caf47e) | `27` | 左侧引脚28 | Left pin 28. |
| [`ST_MORPHO_L_29`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga232e94783d5d74c6c18c63d478f46504) | `28` | 左侧引脚29 | Left pin 29. |
| [`ST_MORPHO_L_30`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga3c6efb4ed29be7549fae5e3b0401da3c) | `29` | 左侧引脚30 | Left pin 30. |
| [`ST_MORPHO_L_31`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga209fa960d432c550c89a05c0daa89929) | `30` | 左侧引脚31 | Left pin 31. |
| [`ST_MORPHO_L_32`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7e87747ad400cb40869223cae73cf96f) | `31` | 左侧引脚32 | Left pin 32. |
| [`ST_MORPHO_L_33`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gab77d4422d229ea432ead96b191bcd461) | `32` | 左侧引脚33 | Left pin 33. |
| [`ST_MORPHO_L_34`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga94f53e50d3e3ee717a01e2b23a676f8e) | `33` | 左侧引脚34 | Left pin 34. |
| [`ST_MORPHO_L_35`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5b1712c33edd7f4182e0bf6a990d2447) | `34` | 左侧引脚35 | Left pin 35. |
| [`ST_MORPHO_L_36`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7174f33cbd854f975d151671ff114e95) | `35` | 左侧引脚36 | Left pin 36. |
| [`ST_MORPHO_L_37`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf852fbedd3fae06a78273d20c97ba926) | `36` | 左侧引脚37 | Left pin 37. |
| [`ST_MORPHO_L_38`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga17f2c83b1ee5a57f7f9f4b8e2622646d) | `37` | 左侧引脚38 | Left pin 38. |
| [`ST_MORPHO_L_39`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga205493fab8c1104868c254eabcb0d8ba) | `38` | 左侧引脚39 | Left pin 39. |
| [`ST_MORPHO_L_40`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gac52077e3239059f4288cfc20fc33e1ae) | `39` | 左侧引脚40 | Left pin 40. |
| [`ST_MORPHO_L_41`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga761d8234bd114f08dc6c3a609a9ddf04) | `40` | 左侧引脚41 | Left pin 41. |
| [`ST_MORPHO_L_42`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gae8faa1b2ad722276597937019572769e) | `41` | 左侧引脚42 | Left pin 42. |
| [`ST_MORPHO_L_43`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8affcfac10cabeaee42bc4a62c66c743) | `42` | 左侧引脚43 | Left pin 43. |
| [`ST_MORPHO_L_44`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gab14501c9564b5135fe0abead9c92f209) | `43` | 左侧引脚44 | Left pin 44. |
| [`ST_MORPHO_L_45`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga85c37a3426ed1439fa84949d291918d5) | `44` | 左侧引脚45 | Left pin 45. |
| [`ST_MORPHO_L_46`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7c976f185048f0dfacdc79a12d64f83f) | `45` | 左侧引脚46 | Left pin 46. |
| [`ST_MORPHO_L_47`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gababefc6821f097c4bf54eef8c0c9c3b7) | `46` | 左侧引脚47 | Left pin 47. |
| [`ST_MORPHO_L_48`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7130f3da9bd79ffcf3f781e18adef198) | `47` | 左侧引脚48 | Left pin 48. |
| [`ST_MORPHO_L_49`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5084b520b02dbd827a72a1202f92f3e1) | `48` | 左侧引脚49 | Left pin 49. |
| [`ST_MORPHO_L_50`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaab51e14dc3e206f23eaa178c14e80855) | `49` | 左侧引脚50 | Left pin 50. |
| [`ST_MORPHO_L_51`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga740fe6c42be92a0e5702871978f6ffea) | `50` | 左侧引脚51 | Left pin 51. |
| [`ST_MORPHO_L_52`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga9bab7d6685c0065f21d33595be581013) | `51` | 左侧引脚52 | Left pin 52. |
| [`ST_MORPHO_L_53`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gabcf2825b9c4daf7c39cf51524efdc6dd) | `52` | 左侧引脚53 | Left pin 53. |
| [`ST_MORPHO_L_54`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gac237ca25c10e7128f95be26ddb2f5662) | `53` | 左侧引脚54 | Left pin 54. |
| [`ST_MORPHO_L_55`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga93a21e7d82a23d22c9ec6342fb35801b) | `54` | 左侧引脚55 | Left pin 55. |
| [`ST_MORPHO_L_56`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gada243e09f6bc8d762a121f509d7f35d0) | `55` | 左侧引脚56 | Left pin 56. |
| [`ST_MORPHO_L_57`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga1a598452f0e651c3e48e383b67f78334) | `56` | 左侧引脚57 | Left pin 57. |
| [`ST_MORPHO_L_58`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga968bb384a0c59ad4c12623fedbe9f5e6) | `57` | 左侧引脚58 | Left pin 58. |
| [`ST_MORPHO_L_59`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf6652e7124d7ae5b7eae21b0e294497a) | `58` | 左侧引脚59 | Left pin 59. |
| [`ST_MORPHO_L_60`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga40b94b970bffc5400e55eaf2b9afb790) | `59` | 左侧引脚60 | Left pin 60. |
| [`ST_MORPHO_L_61`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa5aef00f15902f08e837f70d210e9755) | `60` | 左侧引脚61 | Left pin 61. |
| [`ST_MORPHO_L_62`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga32169b2ba9944d32b7920a820db6dd31) | `61` | 左侧引脚62 | Left pin 62. |
| [`ST_MORPHO_L_63`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2ef43eee84c2caa9f9562733fda5be51) | `62` | 左侧引脚63 | Left pin 63. |
| [`ST_MORPHO_L_64`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga591518b39ddb0fcc779118491acf0417) | `63` | 左侧引脚64 | Left pin 64. |
| [`ST_MORPHO_L_65`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4a22e7be98eccbf0c34bbde2f9bc8f61) | `64` | 左侧引脚65 | Left pin 65. |
| [`ST_MORPHO_L_66`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaacdb9fc891e6f8bc7cf4a8fc029b905d) | `65` | 左侧引脚66 | Left pin 66. |
| [`ST_MORPHO_L_67`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8c8f46bcae0509cb1845b5b0d5bf4f35) | `66` | 左侧引脚67 | Left pin 67. |
| [`ST_MORPHO_L_68`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga3b8db2b96e9872545928810f93f8138d) | `67` | 左侧引脚68 | Left pin 68. |
| [`ST_MORPHO_L_69`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga16e300411c5b1a31a9dfa4dc2c3c1e7f) | `68` | 左侧引脚69 | Left pin 69. |
| [`ST_MORPHO_L_70`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga55eecbccfc14ff0324d0561488715d84) | `69` | 左侧引脚70 | Left pin 70. |
| [`ST_MORPHO_L_71`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga832b5cf86625834cffadcee7e9746d24) | `70` | 左侧引脚71 | Left pin 71. |
| [`ST_MORPHO_L_72`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gafa49104ced2509cc6db39ff37ffe6310) | `71` | 左侧引脚72 | Left pin 72. |
| [`ST_MORPHO_R_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga76a61933e0c61591ea986414b375e7ed) | `72` | 右侧引脚1 | Right pin 1. |
| [`ST_MORPHO_R_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gab13b526b90284fe6fc3584caafe40617) | `73` | 右侧引脚2 | Right pin 2. |
| [`ST_MORPHO_R_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gae7a0c2084b7eed22a91bc5e4b802eb27) | `74` | 右侧引脚3 | Right pin 3. |
| [`ST_MORPHO_R_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7689fb0c9a49ebb263287ab298568307) | `75` | 右侧引脚4 | Right pin 4. |
| [`ST_MORPHO_R_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga03df1fe95b3813709754016f9a9bf0c6) | `76` | 右侧引脚5 | Right pin 5. |
| [`ST_MORPHO_R_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga6a4a173191015a23a4cce6616d8c3140) | `77` | 右侧引脚6 | Right pin 6. |
| [`ST_MORPHO_R_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf6c9b8afc7bb91a08e8f0518777f5cd5) | `78` | 右侧引脚7 | Right pin 7. |
| [`ST_MORPHO_R_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gabf653c8e66e8fe76dc0559e05c8518f5) | `79` | 右侧引脚8 | Right pin 8. |
| [`ST_MORPHO_R_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8967a7092dc10042460e0a5e51c2aa92) | `80` | 右侧引脚9 | Right pin 9. |
| [`ST_MORPHO_R_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga98aa9aeb1af8cfb41c1640dfea0f2753) | `81` | 右侧引脚10 | Right pin 10. |
| [`ST_MORPHO_R_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga13b40b7b33fa8aec73add3b3d2cb70e9) | `82` | 右侧引脚11 | Right pin 11. |
| [`ST_MORPHO_R_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga245a95538f671247b09f41feaeeed011) | `83` | 右侧引脚12 | Right pin 12. |
| [`ST_MORPHO_R_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga0cf8ed73dbb537a4b747f25cb5be956a) | `84` | 右侧引脚13 | Right pin 13. |
| [`ST_MORPHO_R_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa724314fa7e256a31e6ccf5833cf82e7) | `85` | 右侧引脚14 | Right pin 14. |
| [`ST_MORPHO_R_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga907bcc3df218c720c94d0bb9116c08ef) | `86` | 右侧引脚15 | Right pin 15. |
| [`ST_MORPHO_R_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga6b13b2ccaba49026b3ed2b7fc63722bd) | `87` | 右侧引脚16 | Right pin 16. |
| [`ST_MORPHO_R_17`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga889f48e62a128fa0f1f1609e22edee53) | `88` | 右侧引脚17 | Right pin 17. |
| [`ST_MORPHO_R_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5fed472e2d14d506cf69db1b6c9ddd4b) | `89` | 右侧引脚18 | Right pin 18. |
| [`ST_MORPHO_R_19`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2d751789b4dedf7821a4cb7ae9f7204c) | `90` | 右侧引脚19 | Right pin 19. |
| [`ST_MORPHO_R_20`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaff35032167dfb9c5705001b0c9cc9182) | `91` | 右侧引脚20 | Right pin 20. |
| [`ST_MORPHO_R_21`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga164c35d72e884c81aa07a0a9fd5880cf) | `92` | 右侧引脚21 | Right pin 21. |
| [`ST_MORPHO_R_22`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga767e261fd1e6265681da6d457a6e7264) | `93` | 右侧引脚22 | Right pin 22. |
| [`ST_MORPHO_R_23`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga46de2c38e92e0e45e6b389370640bfc2) | `94` | 右侧引脚23 | Right pin 23. |
| [`ST_MORPHO_R_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga66a7780ea324e56a080b2750f7897094) | `95` | 右侧引脚24 | Right pin 24. |
| [`ST_MORPHO_R_25`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gac052ae1a9d4de25e070ead9d4a41df78) | `96` | 右侧引脚25 | Right pin 25. |
| [`ST_MORPHO_R_26`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gabe6184b84c4ce46303bc321252849fba) | `97` | 右侧引脚26 | Right pin 26. |
| [`ST_MORPHO_R_27`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gabad9b23cc8b9f163b66f7e08e63ae82e) | `98` | 右侧引脚27 | Right pin 27. |
| [`ST_MORPHO_R_28`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gae83add66ebc6bef0d288bfca06002b2c) | `99` | 右侧引脚28 | Right pin 28. |
| [`ST_MORPHO_R_29`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga1ffe7134a54899ccfc2f9dd914034eb7) | `100` | 右侧引脚29 | Right pin 29. |
| [`ST_MORPHO_R_30`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga9e728ff30ee7a0b84d383e45d167992a) | `101` | 右侧引脚30 | Right pin 30. |
| [`ST_MORPHO_R_31`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga550ebeb4af3791a2adbf898a13778ce8) | `102` | 右侧引脚31 | Right pin 31. |
| [`ST_MORPHO_R_32`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaea3f7ef4f1269ed91642e42b1596c3a2) | `103` | 右侧引脚32 | Right pin 32. |
| [`ST_MORPHO_R_33`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gafc9ed3f5d65f09a7efe7fca0fb0a0b2c) | `104` | 右侧引脚33 | Right pin 33. |
| [`ST_MORPHO_R_34`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga9d4e1df66ece78e6a6953c8ecbaeb73b) | `105` | 右侧引脚34 | Right pin 34. |
| [`ST_MORPHO_R_35`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaf5f9d64a8b569f85e7f19ed522ac8a57) | `106` | 右侧引脚35 | Right pin 35. |
| [`ST_MORPHO_R_36`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa650fe5fb805bccad6139ed4f4256817) | `107` | 右侧引脚36 | Right pin 36. |
| [`ST_MORPHO_R_37`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gafbd5b257426c7dbfce5df4200552b1bc) | `108` | 右侧引脚37 | Right pin 37. |
| [`ST_MORPHO_R_38`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa52b614c36d9a26e064448c2385c95ce) | `109` | 右侧引脚38 | Right pin 38. |
| [`ST_MORPHO_R_39`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4b484d69c4b39ba48adaadc019036afb) | `110` | 右侧引脚39 | Right pin 39. |
| [`ST_MORPHO_R_40`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4f0b3e2c43ba27be4a1f4e5d62c97e9c) | `111` | 右侧引脚40 | Right pin 40. |
| [`ST_MORPHO_R_41`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga7c46de2186397370df9c42801faee380) | `112` | 右侧引脚41 | Right pin 41. |
| [`ST_MORPHO_R_42`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga38e3185f00a2d25f50be7babad5d8c0e) | `113` | 右侧引脚42 | Right pin 42. |
| [`ST_MORPHO_R_43`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaaea5071983ac3c4e1e0a424711082e41) | `114` | 右侧引脚43 | Right pin 43. |
| [`ST_MORPHO_R_44`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gad29c759f058a7604043cc542ac7d921d) | `115` | 右侧引脚44 | Right pin 44. |
| [`ST_MORPHO_R_45`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga629e7111e1885641529c5b8123e5da45) | `116` | 右侧引脚45 | Right pin 45. |
| [`ST_MORPHO_R_46`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gac3b90147b88cdf4a5ae2b037505d3ad5) | `117` | 右侧引脚46 | Right pin 46. |
| [`ST_MORPHO_R_47`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5768774a3ab39e23abe93b3beec2a9be) | `118` | 右侧引脚47 | Right pin 47. |
| [`ST_MORPHO_R_48`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga70091a75ae5adf9d9a2e86ec717c0c50) | `119` | 右侧引脚48 | Right pin 48. |
| [`ST_MORPHO_R_49`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2281027b9062bd8ddf8a96928f01c8a5) | `120` | 右侧引脚49 | Right pin 49. |
| [`ST_MORPHO_R_50`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5fb68c2e113bae39328de4564fbebb4b) | `121` | 右侧引脚50 | Right pin 50. |
| [`ST_MORPHO_R_51`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga632a699ac0be5e03b7106b451943d911) | `122` | 右侧引脚51 | Right pin 51. |
| [`ST_MORPHO_R_52`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga91bf844a770fea58dce4a435289e2ebc) | `123` | 右侧引脚52 | Right pin 52. |
| [`ST_MORPHO_R_53`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gab3e6858cdd5f31c236464181ded221ef) | `124` | 右侧引脚53 | Right pin 53. |
| [`ST_MORPHO_R_54`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4c82ed1fab2e1976469ddb9a636f2aac) | `125` | 右侧引脚54 | Right pin 54. |
| [`ST_MORPHO_R_55`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga9c2d0adff9b3046d6d1aea46dec6bef2) | `126` | 右侧引脚55 | Right pin 55. |
| [`ST_MORPHO_R_56`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga3e83a14566b122d9a41295c11b90eca6) | `127` | 右侧引脚56 | Right pin 56. |
| [`ST_MORPHO_R_57`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4fae4ca54188e42f096c8d36b1cc60df) | `128` | 右侧引脚57 | Right pin 57. |
| [`ST_MORPHO_R_58`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gad9d6dedab1420cfde4cb899d99182028) | `129` | 右侧引脚58 | Right pin 58. |
| [`ST_MORPHO_R_59`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaccfb22345c4491c61857d6e06be16d58) | `130` | 右侧引脚59 | Right pin 59. |
| [`ST_MORPHO_R_60`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga51069c38405f7ae9a8c54919137a2dd8) | `131` | 右侧引脚60 | Right pin 60. |
| [`ST_MORPHO_R_61`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaac0ba09c411ce7c44552dca49241b70a) | `132` | 右侧引脚61 | Right pin 61. |
| [`ST_MORPHO_R_62`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gab15f6b8145acea22d7239ae42287551e) | `133` | 右侧引脚62 | Right pin 62. |
| [`ST_MORPHO_R_63`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga2d07c9984a89ffc7f693729a08c64c1b) | `134` | 右侧引脚63 | Right pin 63. |
| [`ST_MORPHO_R_64`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga307834d865d27c972c61e4bc33a82a00) | `135` | 右侧引脚64 | Right pin 64. |
| [`ST_MORPHO_R_65`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga8a724f2b528cbbea81e48ec88acc8834) | `136` | 右侧引脚65 | Right pin 65. |
| [`ST_MORPHO_R_66`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga4064509127251858aec848f383bcc42c) | `137` | 右侧引脚66 | Right pin 66. |
| [`ST_MORPHO_R_67`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga359c31a08c1c746b6e1368a117961442) | `138` | 右侧引脚67 | Right pin 67. |
| [`ST_MORPHO_R_68`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga5f00cada04ccd2f91e82d01a93deb6f1) | `139` | 右侧引脚68 | Right pin 68. |
| [`ST_MORPHO_R_69`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga3c6da64bf8795a14149093a88d1cbaa2) | `140` | 右侧引脚69 | Right pin 69. |
| [`ST_MORPHO_R_70`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#ga14074f7cacd85dcfdf0ca2134e2d32e9) | `141` | 右侧引脚70 | Right pin 70. |
| [`ST_MORPHO_R_71`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gaa778cef9b49e70713643784c83d52256) | `142` | 右侧引脚71 | Right pin 71. |
| [`ST_MORPHO_R_72`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-morpho-header.html#gae0ec7e049c1c9104cf18d88b4cf4bada) | `143` | 右侧引脚72 | Right pin 72. |

---

[上一章：树莓派CSI连接器](P299_树莓派CSI连接器.md) · [下一章：STZio排针](P301_STZio排针.md) · [返回大纲](大纲.md)
