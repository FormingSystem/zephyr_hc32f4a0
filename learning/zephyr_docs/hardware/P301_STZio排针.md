---
id: learning.zephyr-docs.hardware.headers-10
title: STZio排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第301章\_STZio排针

原文：[group__st-zio-header](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 301.1\_接口与术语

本页定义ST Zio排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/st-zio-header.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

CN7、CN8、CN9、CN10是连接器位号；各自引脚位置与常量编码见表。引脚掩码（Pin Mask）为 `0xFF`，原文列出的编码范围为0—99。

## 301.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ST_ZIO_PIN_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gad4d1bc7decae866f25257df1b0c44740) | `0xFF` | ST Zio引脚掩码（0...99） | ST Zio pin mask (0...99). |
| [`ST_ZIO_CN7_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gadbcd033037d180bfd136f5162ba552c8) | `0` | CN7连接器引脚1 | CN7 pin 1. |
| [`ST_ZIO_CN7_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga597867e7fd732e780796b0a7667e72d3) | `1` | CN7连接器引脚2 | CN7 pin 2. |
| [`ST_ZIO_CN7_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaef044b2a00acdcad3ed211d8aa5d8c78) | `2` | CN7连接器引脚3 | CN7 pin 3. |
| [`ST_ZIO_CN7_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga75652958cda98557e4befd17d4d5f9c2) | `3` | CN7连接器引脚4 | CN7 pin 4. |
| [`ST_ZIO_CN7_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaf61395ec5405a6fd0e7b3b2840529790) | `4` | CN7连接器引脚5 | CN7 pin 5. |
| [`ST_ZIO_CN7_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaca6db74223fe3b523a6658c3f77b54e3) | `5` | CN7连接器引脚6 | CN7 pin 6. |
| [`ST_ZIO_CN7_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3cfa28b7a9ae3575717361adfd7c7028) | `6` | CN7连接器引脚7 | CN7 pin 7. |
| [`ST_ZIO_CN7_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga0db921acc74177838364f7e39cadb4c0) | `7` | CN7连接器引脚8 | CN7 pin 8. |
| [`ST_ZIO_CN7_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga8243be950c37f38d52df2df093787012) | `8` | CN7连接器引脚9 | CN7 pin 9. |
| [`ST_ZIO_CN7_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga68e14b0cb00a854472b6769d9238d2a4) | `9` | CN7连接器引脚10 | CN7 pin 10. |
| [`ST_ZIO_CN7_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gac399feb9acd8d52cb2b503bad929d8ac) | `10` | CN7连接器引脚11 | CN7 pin 11. |
| [`ST_ZIO_CN7_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gab420dccf1a347ad34f49696694b54065) | `11` | CN7连接器引脚12 | CN7 pin 12. |
| [`ST_ZIO_CN7_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9ec8a54a611cf9039fb16ebbc546b09d) | `12` | CN7连接器引脚13 | CN7 pin 13. |
| [`ST_ZIO_CN7_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga92fb202cee182167342a614e34fd6a84) | `13` | CN7连接器引脚14 | CN7 pin 14. |
| [`ST_ZIO_CN7_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gabe21ea69fd61f43111312098abb53eeb) | `14` | CN7连接器引脚15 | CN7 pin 15. |
| [`ST_ZIO_CN7_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga47fa1de811845bc6efbe005f39ddf51f) | `15` | CN7连接器引脚16 | CN7 pin 16. |
| [`ST_ZIO_CN7_17`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga577cb7caaa67f5696bdace56ac832599) | `16` | CN7连接器引脚17 | CN7 pin 17. |
| [`ST_ZIO_CN7_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaf3b08a8082476a2e87559cd423f1851b) | `17` | CN7连接器引脚18 | CN7 pin 18. |
| [`ST_ZIO_CN7_19`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaaacce2001e3fca4303724eaa75181f9a) | `18` | CN7连接器引脚19 | CN7 pin 19. |
| [`ST_ZIO_CN7_20`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga7f1353c09147b822c989800c59d433b8) | `19` | CN7连接器引脚20 | CN7 pin 20. |
| [`ST_ZIO_CN8_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3ef71b99b4cd078fb2088bdeafd5adf1) | `20` | CN8连接器引脚1 | CN8 pin 1. |
| [`ST_ZIO_CN8_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga8385db425b15ce0de126491b8a5a8b44) | `21` | CN8连接器引脚2 | CN8 pin 2. |
| [`ST_ZIO_CN8_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga949f402543c068ad45c4ce1c7b193ebd) | `22` | CN8连接器引脚3 | CN8 pin 3. |
| [`ST_ZIO_CN8_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga7e3bf7507c91f9cabbd28c1995ca2427) | `23` | CN8连接器引脚4 | CN8 pin 4. |
| [`ST_ZIO_CN8_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gae1466b40d042d734aa0c1caa93e9be4a) | `24` | CN8连接器引脚5 | CN8 pin 5. |
| [`ST_ZIO_CN8_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3e72d192d6365d378759b50d34d46458) | `25` | CN8连接器引脚6 | CN8 pin 6. |
| [`ST_ZIO_CN8_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga890c69ac97341d32cd4b071a140340f6) | `26` | CN8连接器引脚7 | CN8 pin 7. |
| [`ST_ZIO_CN8_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaae7ffeaaeb4031f72657cf59525ec9fe) | `27` | CN8连接器引脚8 | CN8 pin 8. |
| [`ST_ZIO_CN8_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga85bd8c77b4a520989355ed2aa4bca0db) | `28` | CN8连接器引脚9 | CN8 pin 9. |
| [`ST_ZIO_CN8_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga5cac4b18bf1db010e8224c042e1c7331) | `29` | CN8连接器引脚10 | CN8 pin 10. |
| [`ST_ZIO_CN8_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gadf688b00457b5499f5d36a3e51bdb5de) | `30` | CN8连接器引脚11 | CN8 pin 11. |
| [`ST_ZIO_CN8_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaf060022f2961771ecd57812b9b85dc6e) | `31` | CN8连接器引脚12 | CN8 pin 12. |
| [`ST_ZIO_CN8_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga77477a254f8a6f66d7671ce2285173a4) | `32` | CN8连接器引脚13 | CN8 pin 13. |
| [`ST_ZIO_CN8_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga4a5754bce438e7c8ab48157cb0186dbf) | `33` | CN8连接器引脚14 | CN8 pin 14. |
| [`ST_ZIO_CN8_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaa20b0eb01f07318ad1ffa0b1f2b70ba3) | `34` | CN8连接器引脚15 | CN8 pin 15. |
| [`ST_ZIO_CN8_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga8333913161e0bb6c3b733784fb79e853) | `35` | CN8连接器引脚16 | CN8 pin 16. |
| [`ST_ZIO_CN9_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaf44cb4ff6060d34fad2003215c358267) | `36` | CN9连接器引脚1 | CN9 pin 1. |
| [`ST_ZIO_CN9_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga4e18adf1367741ee66ee1a9d241fe584) | `37` | CN9连接器引脚2 | CN9 pin 2. |
| [`ST_ZIO_CN9_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga6b28c3f9976758818df6f38ddd0b870e) | `38` | CN9连接器引脚3 | CN9 pin 3. |
| [`ST_ZIO_CN9_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gace4bf4d61c8a3b3346afe61917c79337) | `39` | CN9连接器引脚4 | CN9 pin 4. |
| [`ST_ZIO_CN9_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9e6440e9b80ade2d090a542a7c778790) | `40` | CN9连接器引脚5 | CN9 pin 5. |
| [`ST_ZIO_CN9_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gae6591640dbf465b6423d35bb14d7014c) | `41` | CN9连接器引脚6 | CN9 pin 6. |
| [`ST_ZIO_CN9_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaf6336773b30ef0571e35ccee5718e3ad) | `42` | CN9连接器引脚7 | CN9 pin 7. |
| [`ST_ZIO_CN9_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga2dd01a129ae0fc3d4d33575b3e1b5148) | `43` | CN9连接器引脚8 | CN9 pin 8. |
| [`ST_ZIO_CN9_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3938122a39f8339503fedb5637ddd490) | `44` | CN9连接器引脚9 | CN9 pin 9. |
| [`ST_ZIO_CN9_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gac569d3ae6e513dc609900233e767dc12) | `45` | CN9连接器引脚10 | CN9 pin 10. |
| [`ST_ZIO_CN9_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaad9e0923c452606cadbe479d2c908cfa) | `46` | CN9连接器引脚11 | CN9 pin 11. |
| [`ST_ZIO_CN9_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga532479db64b79ae4b0f7bce9ced64b64) | `47` | CN9连接器引脚12 | CN9 pin 12. |
| [`ST_ZIO_CN9_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaa600717495f5e590b3d0650bee9c091c) | `48` | CN9连接器引脚13 | CN9 pin 13. |
| [`ST_ZIO_CN9_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga1ef722f0a3753953257a8d6c8bd18f5d) | `49` | CN9连接器引脚14 | CN9 pin 14. |
| [`ST_ZIO_CN9_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga11639818f8727b54558d2e37626d81b5) | `50` | CN9连接器引脚15 | CN9 pin 15. |
| [`ST_ZIO_CN9_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga2da955d2c2dfef10fe28196a3a96e37c) | `51` | CN9连接器引脚16 | CN9 pin 16. |
| [`ST_ZIO_CN9_17`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga1625094faf7b808a44ecc49a0806ac99) | `52` | CN9连接器引脚17 | CN9 pin 17. |
| [`ST_ZIO_CN9_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga2c92853771acb4f0bbde467711ab98a1) | `53` | CN9连接器引脚18 | CN9 pin 18. |
| [`ST_ZIO_CN9_19`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gac673e729514a0c1a082d1dd9289cc38b) | `54` | CN9连接器引脚19 | CN9 pin 19. |
| [`ST_ZIO_CN9_20`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga5426cb91c7985cef893904dc1751ec41) | `55` | CN9连接器引脚20 | CN9 pin 20. |
| [`ST_ZIO_CN9_21`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga5e1e5dfbe77596ca5202e718b605cb6c) | `56` | CN9连接器引脚21 | CN9 pin 21. |
| [`ST_ZIO_CN9_22`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga0378b2b48834ded034dacc1959c08511) | `57` | CN9连接器引脚22 | CN9 pin 22. |
| [`ST_ZIO_CN9_23`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga26dde7463033c3a45432cbb98ed41fdb) | `58` | CN9连接器引脚23 | CN9 pin 23. |
| [`ST_ZIO_CN9_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga10df12ab8e43e8596ad131c47eb0c0a1) | `59` | CN9连接器引脚24 | CN9 pin 24. |
| [`ST_ZIO_CN9_25`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga45c67ea7efa506deb40519f94780ec02) | `60` | CN9连接器引脚25 | CN9 pin 25. |
| [`ST_ZIO_CN9_26`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga136a729d57535c4f28661e6f8a4a5fe3) | `61` | CN9连接器引脚26 | CN9 pin 26. |
| [`ST_ZIO_CN9_27`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga4b9f3f884e94385aa130adb760f10213) | `62` | CN9连接器引脚27 | CN9 pin 27. |
| [`ST_ZIO_CN9_28`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gabc84c7ed9ca462d8f9691f6b656efbf3) | `63` | CN9连接器引脚28 | CN9 pin 28. |
| [`ST_ZIO_CN9_29`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gab8e0fbc38831b619a645171e924c18f6) | `64` | CN9连接器引脚29 | CN9 pin 29. |
| [`ST_ZIO_CN9_30`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga74febeb34eae26fe4526608c90b68b62) | `65` | CN9连接器引脚30 | CN9 pin 30. |
| [`ST_ZIO_CN10_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga60f8ef2c774eb75d33b642e17ff9d795) | `66` | CN10连接器引脚1 | CN10 pin 1. |
| [`ST_ZIO_CN10_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gae0651ba458feda6cacf7f9f4e4427186) | `67` | CN10连接器引脚2 | CN10 pin 2. |
| [`ST_ZIO_CN10_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaa95dd697ae5d98c150de2b7e0fb110e3) | `68` | CN10连接器引脚3 | CN10 pin 3. |
| [`ST_ZIO_CN10_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga1a0b5a5381084670735e8dfba5e4941d) | `69` | CN10连接器引脚4 | CN10 pin 4. |
| [`ST_ZIO_CN10_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9b7bcacfa5e20ea53adad5d3e8ee3ecd) | `70` | CN10连接器引脚5 | CN10 pin 5. |
| [`ST_ZIO_CN10_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga862b2361f8257270ae3e76f8cccc7d51) | `71` | CN10连接器引脚6 | CN10 pin 6. |
| [`ST_ZIO_CN10_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga660ab1612f214c8d4a5ee1da484f26dc) | `72` | CN10连接器引脚7 | CN10 pin 7. |
| [`ST_ZIO_CN10_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga5e9fe1730fe655b1d58d755f05eedd26) | `73` | CN10连接器引脚8 | CN10 pin 8. |
| [`ST_ZIO_CN10_9`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga362d7abc8471aa011e225d9c223b931b) | `74` | CN10连接器引脚9 | CN10 pin 9. |
| [`ST_ZIO_CN10_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga4e4f8e67ccceaafc6c2549e571dda56c) | `75` | CN10连接器引脚10 | CN10 pin 10. |
| [`ST_ZIO_CN10_11`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gac4dc23535f937d76780028c32a7f7b6a) | `76` | CN10连接器引脚11 | CN10 pin 11. |
| [`ST_ZIO_CN10_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga34b0c8a0442ba436c1f9f8daa98a815c) | `77` | CN10连接器引脚12 | CN10 pin 12. |
| [`ST_ZIO_CN10_13`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga6189579ce57cd113cce833914bf7fb94) | `78` | CN10连接器引脚13 | CN10 pin 13. |
| [`ST_ZIO_CN10_14`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaafb0a2e8591b370aa460d4950ad3de35) | `79` | CN10连接器引脚14 | CN10 pin 14. |
| [`ST_ZIO_CN10_15`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga485abb90a2f8d8ee444458be5bdbf4bd) | `80` | CN10连接器引脚15 | CN10 pin 15. |
| [`ST_ZIO_CN10_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga400934b493fc2193eb69e0fa5e7fa870) | `81` | CN10连接器引脚16 | CN10 pin 16. |
| [`ST_ZIO_CN10_17`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga2dca2015dd3f17e952739a5a88c166c3) | `82` | CN10连接器引脚17 | CN10 pin 17. |
| [`ST_ZIO_CN10_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga1d30f0e71fcfc1a5bb33f1620bae31f4) | `83` | CN10连接器引脚18 | CN10 pin 18. |
| [`ST_ZIO_CN10_19`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3ff206d2840c6370599c0fb9a048c7c5) | `84` | CN10连接器引脚19 | CN10 pin 19. |
| [`ST_ZIO_CN10_20`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga60c5714640bc232b301a45e0ab157533) | `85` | CN10连接器引脚20 | CN10 pin 20. |
| [`ST_ZIO_CN10_21`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga2b56f0a5177f7849dcc30bdb533d81b3) | `86` | CN10连接器引脚21 | CN10 pin 21. |
| [`ST_ZIO_CN10_22`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gaa005539806407b53b8ed3bf7a39cde59) | `87` | CN10连接器引脚22 | CN10 pin 22. |
| [`ST_ZIO_CN10_23`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga3582e64686c66c68118c16b61ee9677b) | `88` | CN10连接器引脚23 | CN10 pin 23. |
| [`ST_ZIO_CN10_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga522930389b061b2dec743a18a2d07861) | `89` | CN10连接器引脚24 | CN10 pin 24. |
| [`ST_ZIO_CN10_25`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9b94baa9f2748cf379b34051c1e22644) | `90` | CN10连接器引脚25 | CN10 pin 25. |
| [`ST_ZIO_CN10_26`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gabebdeb11b9e37bb51c1c068c512206f1) | `91` | CN10连接器引脚26 | CN10 pin 26. |
| [`ST_ZIO_CN10_27`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gad35a3ffc7a93d1f1e66fc06df6eb6550) | `92` | CN10连接器引脚27 | CN10 pin 27. |
| [`ST_ZIO_CN10_28`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga0de4c10ac938277625f824ce7e4fb904) | `93` | CN10连接器引脚28 | CN10 pin 28. |
| [`ST_ZIO_CN10_29`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9564d1a52c6690e2644492fe4a31a458) | `94` | CN10连接器引脚29 | CN10 pin 29. |
| [`ST_ZIO_CN10_30`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#gabe171255b7cf0d95a193db19c74f4556) | `95` | CN10连接器引脚30 | CN10 pin 30. |
| [`ST_ZIO_CN10_31`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga36dd3412d3a604434f3c4a79616b428c) | `96` | CN10连接器引脚31 | CN10 pin 31. |
| [`ST_ZIO_CN10_32`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga8be5efd33580ca4ca1354b7ed633b9e2) | `97` | CN10连接器引脚32 | CN10 pin 32. |
| [`ST_ZIO_CN10_33`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga9ed5b485ec4e43a5fd3d9034150a6c6f) | `98` | CN10连接器引脚33 | CN10 pin 33. |
| [`ST_ZIO_CN10_34`](https://docs.zephyrproject.org/latest/doxygen/html/group__st-zio-header.html#ga867959655c166ac0f35c887a302915b9) | `99` | CN10连接器引脚34 | CN10 pin 34. |

---

[上一章：STMorpho排针](P300_STMorpho排针.md) · [下一章：STModPlus连接器](P302_STModPlus连接器.md) · [返回大纲](大纲.md)
