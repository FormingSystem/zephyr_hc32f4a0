---
id: learning.zephyr-docs.can-driver-reference.page-2
title: CAN驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2can_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CAN驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2can_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_CAN驱动头文件参考.md)和[公共API](../hardware/P362_CAN控制器接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00127"></a>
<a id="foldopen00169"></a>
<a id="foldopen00215"></a>
<a id="foldopen00229"></a>
<a id="foldopen00268"></a>
<a id="foldopen00342"></a>
<a id="foldopen00367"></a>
<a id="foldopen00377"></a>
<a id="foldopen00403"></a>
<a id="foldopen00424"></a>
<a id="foldopen00433"></a>
<a id="foldopen00566"></a>
<a id="foldopen00682"></a>
<a id="foldopen00717"></a>
<a id="foldopen00733"></a>
<a id="foldopen00752"></a>
<a id="foldopen00768"></a>
<a id="foldopen00781"></a>
<a id="foldopen00794"></a>
<a id="foldopen00807"></a>
<a id="foldopen00821"></a>
<a id="foldopen00834"></a>
<a id="foldopen00934"></a>
<a id="foldopen01448"></a>
<a id="foldopen01624"></a>
<a id="foldopen01855"></a>
<a id="foldopen01870"></a>
<a id="foldopen01889"></a>
<a id="acanbus_8h_html"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__can__controller__backend_html_ga01a5f028d947582dd4195b467dae8b94"></a>
<a id="agroup__can__controller__backend_html_ga14210ea7870ef23072cd61c10043540f"></a>
<a id="agroup__can__controller__backend_html_ga1ab69e7991b8492e36c4b3f359db1961"></a>
<a id="agroup__can__controller__backend_html_ga20ee94c5122acb6fd7fe5939a20ba748"></a>
<a id="agroup__can__controller__backend_html_ga231b61f4d1413e0d28dd5a8bc25a89b3"></a>
<a id="agroup__can__controller__backend_html_ga2fd489217c19977d239d51f0b3fcfc19"></a>
<a id="agroup__can__controller__backend_html_ga3bc249502cb65bf89bce2ca87535ac6b"></a>
<a id="agroup__can__controller__backend_html_ga4d44354cda4cfe0af5262189549d6523"></a>
<a id="agroup__can__controller__backend_html_ga7be2d21503b59cde52369d589ccff80f"></a>
<a id="agroup__can__controller__backend_html_ga80424a027933c3bc0d973f37333d2618"></a>
<a id="agroup__can__controller__backend_html_ga89108f1d99fa1ba784808f1e99763a58"></a>
<a id="agroup__can__controller__backend_html_ga8bcafa14e23f2ba70e17c1432449d744"></a>
<a id="agroup__can__controller__backend_html_ga946dd40c12eba40c34afa7572d61456c"></a>
<a id="agroup__can__controller__backend_html_gaba24cc4eb2fa759ff8394dd096021982"></a>
<a id="agroup__can__controller__backend_html_gaecca113e6b8cc7caba3d19fdd104aaa7"></a>
<a id="agroup__can__controller_html_ga002ff7ba1f5be374510a902459dd9d3d"></a>
<a id="agroup__can__controller_html_ga0685ebfacfb79d33131167ac3aaa6f9b"></a>
<a id="agroup__can__controller_html_ga0afd2c446fc5e685370641a1678f87b7"></a>
<a id="agroup__can__controller_html_ga0b2a1456e66f4522a30cf1400fdfced7"></a>
<a id="agroup__can__controller_html_ga162fde4e622fb06dcbbcf2f31bb35d38"></a>
<a id="agroup__can__controller_html_ga1b0ac9185341cb0bde85ec64e4c490a5"></a>
<a id="agroup__can__controller_html_ga1b134af5d6286ea0fee130b6da5217da"></a>
<a id="agroup__can__controller_html_ga1dc18f69fe06a1d919b13f929100fa85"></a>
<a id="agroup__can__controller_html_ga1e6dc8026e4d922bce4d398d9f32a457"></a>
<a id="agroup__can__controller_html_ga27b277f3b5146590f159171f602904db"></a>
<a id="agroup__can__controller_html_ga31692aef7962172532f8200fed7aecd2"></a>
<a id="agroup__can__controller_html_ga343456749eec6144a91bacae0d94b114"></a>
<a id="agroup__can__controller_html_ga358cd73ed59c2099f4b2c6ceb397ca11"></a>
<a id="agroup__can__controller_html_ga446ee31913699de3c80be05d837b5fd5"></a>
<a id="agroup__can__controller_html_ga47a2f6d6b42121b390aa92160c833b80"></a>
<a id="agroup__can__controller_html_ga4af6d0d9ab72b195909f511ac65cb8fa"></a>
<a id="agroup__can__controller_html_ga4afd7776c5039dec8acb089499dc1168"></a>
<a id="agroup__can__controller_html_ga4c7d40951a2ae6eaa72e5d1f7a26ac75"></a>
<a id="agroup__can__controller_html_ga4f8414d64b75d4d1ffb7a0feff36f698"></a>
<a id="agroup__can__controller_html_ga526c08539094486f07dc52aad8ed0dcc"></a>
<a id="agroup__can__controller_html_ga5a57627de4764f0bd3b4bafe07f56e6f"></a>
<a id="agroup__can__controller_html_ga5c1c7633e020aec2936a6ce3ba68b256"></a>
<a id="agroup__can__controller_html_ga606cf9fda4c66a0f4abf74e1d357eac2"></a>
<a id="agroup__can__controller_html_ga6399ef0cefdab3da738136f8a5c59c2f"></a>
<a id="agroup__can__controller_html_ga7c380f6c4a529e5b5e6010ab4e6c7680"></a>
<a id="agroup__can__controller_html_ga822aa3142ea01582d5cfb8b478fb2847"></a>
<a id="agroup__can__controller_html_ga8314716fe2b66d567b3fd377b8ee9dc3"></a>
<a id="agroup__can__controller_html_ga8664fbaa13f4bb89540493264d2a041d"></a>
<a id="agroup__can__controller_html_ga9ed5a06a97db2c955a7db4b6e386d5e3"></a>
<a id="agroup__can__controller_html_gaa1d866167c0c23f8d5c0c15385589601"></a>
<a id="agroup__can__controller_html_gaaac20a068b7f32d2f38d1601d588b35c"></a>
<a id="agroup__can__controller_html_gaab9525fafab78c0da0a78a2dae39bd6f"></a>
<a id="agroup__can__controller_html_gaafc54ac799e3a3a098a9f6941d7f2ea8"></a>
<a id="agroup__can__controller_html_gab3675297d3e528bf19e2072f6a84bfca"></a>
<a id="agroup__can__controller_html_gab98c121578c8349d9dfb41d60f356857"></a>
<a id="agroup__can__controller_html_gabd201b5b1fca54048985a8a24dd51e55"></a>
<a id="agroup__can__controller_html_gabe385d0f003b1e990c78ef7a2a3f9616"></a>
<a id="agroup__can__controller_html_gabf813d9f21982f674b213708adee9e96"></a>
<a id="agroup__can__controller_html_gabf9ce221f4f6a8dbaafcff9b7a5c5a10"></a>
<a id="agroup__can__controller_html_gac27fe64142603f0d32d422594356b2d7"></a>
<a id="agroup__can__controller_html_gac474e56a50685736a1c25dca277aab5e"></a>
<a id="agroup__can__controller_html_gac7ec472c26c564dd7067c49f67c8d2f7"></a>
<a id="agroup__can__controller_html_gacda2bc21fa0cbd7b3406dd096827923c"></a>
<a id="agroup__can__controller_html_gace0dd2797a133bd293d34a9ac5348e2a"></a>
<a id="agroup__can__controller_html_gae012d26711c2a7ce1419d21c38cae63a"></a>
<a id="agroup__can__controller_html_gae04c3c884b3ed26dfea4745b7dff2c5f"></a>
<a id="agroup__can__controller_html_gae48dfa8bc5b52f233b9b1a08aac2675a"></a>
<a id="agroup__can__controller_html_gae9dd69a13b960f773ab07bb0bb13b5e9"></a>
<a id="agroup__can__controller_html_gafa40c165d016955ec0c856a7fd53168f"></a>
<a id="agroup__can__controller_html_ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c"></a>
<a id="agroup__can__controller_html_ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff"></a>
<a id="agroup__can__controller_html_ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8"></a>
<a id="agroup__can__controller_html_ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959"></a>
<a id="agroup__can__controller_html_ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__stats__apis_html_ga4124f8c0a9ffb78d8be608a780676785"></a>
<a id="agroup__stats__apis_html_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>
<a id="agroup__stats__apis_html_ga592329613cc77cfa5dee3e1d3b16dd93"></a>
<a id="agroup__stats__apis_html_ga5fba46e743c05b4f36df91a86c37e30d"></a>
<a id="agroup__stats__apis_html_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>
<a id="agroup__stats__apis_html_gae8e85c3ce2d901f4668d7237b19999fe"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astats_2stats_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astructcan__bus__err__cnt_html"></a>
<a id="astructcan__bus__err__cnt_html_a01bb2cb16656d0fd4f99cfbfa1f30e98"></a>
<a id="astructcan__bus__err__cnt_html_a6be6ce6b592641ba0dce36fe1cd8902a"></a>
<a id="astructcan__device__state_html"></a>
<a id="astructcan__device__state_html_a28061ff1193176dd01b7bb9a88f402ec"></a>
<a id="astructcan__device__state_html_ae05c85eae4f6bee075ffdc4f0ab56f47"></a>
<a id="astructcan__driver__api_html"></a>
<a id="astructcan__driver__api_html_a11d2ff416d459faf84905e7ffdc1a536"></a>
<a id="astructcan__driver__api_html_a1951bfc3135824e364d5f18aa9b15d09"></a>
<a id="astructcan__driver__api_html_a24a90bc4d49818985479bfe101cc21d4"></a>
<a id="astructcan__driver__api_html_a356b3761926c2a5a85fcc80b2e8a4643"></a>
<a id="astructcan__driver__api_html_a3ca1cb8bcd6713bfdf20f76cee3bc3a4"></a>
<a id="astructcan__driver__api_html_a56225a8cb458baa0d1745ff5e9202ae6"></a>
<a id="astructcan__driver__api_html_a5ad424b27606f9de8f37524594d396dc"></a>
<a id="astructcan__driver__api_html_a90547b28015e2b7eea6a548b0ab2b576"></a>
<a id="astructcan__driver__api_html_a90dca9dd3baef96c4d3849be367129b5"></a>
<a id="astructcan__driver__api_html_a9b5ec5c71a126798c24a19d1c91f879b"></a>
<a id="astructcan__driver__api_html_aa6b8b2b7c544cf78930b45cab1e6dbb4"></a>
<a id="astructcan__driver__api_html_aba563aff4e114b7956bb824efdebb0c6"></a>
<a id="astructcan__driver__api_html_ac07eeec7b96543b19041a28d70e19a97"></a>
<a id="astructcan__driver__api_html_ac264f4d66a29a5f42aaf2b6c9665f8f3"></a>
<a id="astructcan__driver__api_html_ac42f6d438d3e88f0db8e64c236621f8a"></a>
<a id="astructcan__driver__api_html_accfe8e3e40e5bae33b8c31b1af55c644"></a>
<a id="astructcan__driver__api_html_ae969c18839dc5f1cb4356df6d1ee1e20"></a>
<a id="astructcan__driver__api_html_aeaa8022843f787bddbb18aa407d340a5"></a>
<a id="astructcan__driver__config_html"></a>
<a id="astructcan__driver__config_html_a2cd7693cd9acc0537a085cdc85688a96"></a>
<a id="astructcan__driver__config_html_a420d9f8762ae332d4d78084dd74afa6e"></a>
<a id="astructcan__driver__config_html_a6f4f050b5aeb8cd466a12d70c53e8423"></a>
<a id="astructcan__driver__config_html_a8e9f0ec132daf25a2e947478c0b952a3"></a>
<a id="astructcan__driver__config_html_accc9f1b6202b2b30b60bbc890190d3c3"></a>
<a id="astructcan__driver__config_html_afa6cd8cb79ccad28ca86caec4d92cd85"></a>
<a id="astructcan__driver__config_html_afd7a831b33b059f47dd867726e31e69b"></a>
<a id="astructcan__driver__data_html"></a>
<a id="astructcan__driver__data_html_a1f01de3a78be9193263a47acf4181b93"></a>
<a id="astructcan__driver__data_html_a281054c5102f22c362691b81efbb8162"></a>
<a id="astructcan__driver__data_html_a5b3983ca54213c84f8278ec36f0fb0ce"></a>
<a id="astructcan__driver__data_html_a5b8a964383a759a0144a1b72bb8835cc"></a>
<a id="astructcan__driver__data_html_a646e5422136017bed629e5a0f80d4824"></a>
<a id="astructcan__driver__data_html_af6a94bfe3b21502dc70548b470f732b4"></a>
<a id="astructcan__driver__data_html_afce7bbd484eea2660fe71f0322103265"></a>
<a id="astructcan__filter_html"></a>
<a id="astructcan__filter_html_a15632117f3f031fbbeb28ef562f9ac94"></a>
<a id="astructcan__filter_html_a7616e21f33be5fb43094d44530a1c5de"></a>
<a id="astructcan__filter_html_adf2b18eab11d360780707478a1f624b9"></a>
<a id="astructcan__frame_html"></a>
<a id="astructcan__frame_html_a014c42277e886906e6c761bc6f21fb47"></a>
<a id="astructcan__frame_html_a1e71125342a01a6e5a68a14cb075ce7c"></a>
<a id="astructcan__frame_html_a7ad0d8d62322affafbfd23839ee81d5d"></a>
<a id="astructcan__frame_html_ac4b43443b2a338d35f0e1d3ef8355960"></a>
<a id="astructcan__frame_html_ad88af93a2171e4c9d617b91b403d842a"></a>
<a id="astructcan__frame_html_ae46f8b0821c638517959274bbbda5932"></a>
<a id="astructcan__state__change__callback_html"></a>
<a id="astructcan__state__change__callback_html_a20e10ceff66aefd6e77340687cab3f40"></a>
<a id="astructcan__state__change__callback_html_a3bf66a334174307bde9c0fe12939a503"></a>
<a id="astructcan__timing_html"></a>
<a id="astructcan__timing_html_a5af76a4ee9c741642ec19265a47fceb5"></a>
<a id="astructcan__timing_html_a6ca0caf618d28a761c3c8859ed3a68d6"></a>
<a id="astructcan__timing_html_a74fb8341cbb6d97721c9d0afbc7e1f3a"></a>
<a id="astructcan__timing_html_a9941688e79fa4ce01c4b498433319089"></a>
<a id="astructcan__timing_html_ac009d40fee9788b663963978498b2ee9"></a>
<a id="astructdevice__state_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="asys_2util_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2021-2026 Vestas Wind Systems A/S
<a id="l00003"></a> * Copyright (c) 2018 Karsten Koenig
<a id="l00004"></a> * Copyright (c) 2018 Alexander Wachter
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_CAN_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_DRIVERS_CAN_H_
<a id="l00017"></a>
<a id="l00018"></a>#include &lt;errno.h&gt;
<a id="l00019"></a>
<a id="l00020"></a>#include &lt;zephyr/types.h&gt;
<a id="l00021"></a>#include &lt;zephyr/device.h&gt;
<a id="l00022"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00023"></a>#include &lt;string.h&gt;
<a id="l00024"></a>#include &lt;zephyr/sys/clock.h&gt;
<a id="l00025"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00026"></a>
<a id="l00027"></a>#ifdef __cplusplus
<a id="l00028"></a>extern "C" {
<a id="l00029"></a>#endif
<a id="l00030"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00053"></a>#define CAN_STD_ID_MASK 0x7FFU
<a id="l00054"></a>
<a id="l00058"></a>#define CAN_EXT_ID_MASK 0x1FFFFFFFU
<a id="l00059"></a>
<a id="l00063"></a>#define CAN_MAX_DLC     8U
<a id="l00064"></a>
<a id="l00068"></a>#define CANFD_MAX_DLC   15U
<a id="l00069"></a>
<a id="l00074"></a>#ifndef CONFIG_CAN_FD_MODE
<a id="l00075"></a>#define CAN_MAX_DLEN    8U
<a id="l00076"></a>#else
<a id="l00077"></a>#define CAN_MAX_DLEN    64U
<a id="l00078"></a>#endif /* CONFIG_CAN_FD_MODE */
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00090"></a>
<a id="l00092"></a>#define CAN_MODE_NORMAL     0
<a id="l00093"></a>
<a id="l00095"></a>#define CAN_MODE_LOOPBACK        BIT(0)
<a id="l00096"></a>
<a id="l00098"></a>#define CAN_MODE_LISTENONLY      BIT(1)
<a id="l00099"></a>
<a id="l00101"></a>#define CAN_MODE_FD              BIT(2)
<a id="l00102"></a>
<a id="l00104"></a>#define CAN_MODE_ONE_SHOT        BIT(3)
<a id="l00105"></a>
<a id="l00107"></a>#define CAN_MODE_3_SAMPLES       BIT(4)
<a id="l00108"></a>
<a id="l00110"></a>#define CAN_MODE_MANUAL_RECOVERY BIT(5)
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00122"></a>typedef uint32_t can_mode_t;
<a id="l00123"></a>
<a id="l00127"></a>enum can_state {
<a id="l00129"></a>        CAN_STATE_ERROR_ACTIVE,
<a id="l00131"></a>        CAN_STATE_ERROR_WARNING,
<a id="l00133"></a>        CAN_STATE_ERROR_PASSIVE,
<a id="l00135"></a>        CAN_STATE_BUS_OFF,
<a id="l00137"></a>        CAN_STATE_STOPPED,
<a id="l00138"></a>};
<a id="l00139"></a>
<a id="l00146"></a>
<a id="l00148"></a>#define CAN_FRAME_IDE BIT(0)
<a id="l00149"></a>
<a id="l00151"></a>#define CAN_FRAME_RTR BIT(1)
<a id="l00152"></a>
<a id="l00154"></a>#define CAN_FRAME_FDF BIT(2)
<a id="l00155"></a>
<a id="l00157"></a>#define CAN_FRAME_BRS BIT(3)
<a id="l00158"></a>
<a id="l00162"></a>#define CAN_FRAME_ESI BIT(4)
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00169"></a>struct can_frame {
<a id="l00171"></a>        uint32_t id;
<a id="l00173"></a>        uint8_t dlc;
<a id="l00175"></a>        uint8_t flags;
<a id="l00176"></a>#if defined(CONFIG_CAN_RX_TIMESTAMP) || defined(__DOXYGEN__)
<a id="l00184"></a>        uint16_t timestamp;
<a id="l00185"></a>#else
<a id="l00188"></a>        uint16_t reserved;
<a id="l00190"></a>#endif
<a id="l00192"></a>        union {
<a id="l00194"></a>                uint8_t data[CAN_MAX_DLEN];
<a id="l00196"></a>                uint32_t data_32[DIV_ROUND_UP(CAN_MAX_DLEN, sizeof(uint32_t))];
<a id="l00197"></a>        };
<a id="l00198"></a>};
<a id="l00199"></a>
<a id="l00206"></a>
<a id="l00208"></a>#define CAN_FILTER_IDE  BIT(0)
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00215"></a>struct can_filter {
<a id="l00217"></a>        uint32_t id;
<a id="l00221"></a>        uint32_t mask;
<a id="l00223"></a>        uint8_t flags;
<a id="l00224"></a>};
<a id="l00225"></a>
<a id="l00229"></a>struct can_bus_err_cnt {
<a id="l00231"></a>        uint8_t tx_err_cnt;
<a id="l00233"></a>        uint8_t rx_err_cnt;
<a id="l00234"></a>};
<a id="l00235"></a>
<a id="l00268"></a>struct can_timing {
<a id="l00270"></a>        uint16_t sjw;
<a id="l00272"></a>        uint16_t prop_seg;
<a id="l00274"></a>        uint16_t phase_seg1;
<a id="l00276"></a>        uint16_t phase_seg2;
<a id="l00278"></a>        uint16_t prescaler;
<a id="l00279"></a>};
<a id="l00280"></a>
<a id="l00289"></a>typedef void (*can_tx_callback_t)(const struct device *dev, int error, void *user_data);
<a id="l00290"></a>
<a id="l00298"></a>typedef void (*can_rx_callback_t)(const struct device *dev, struct can_frame *frame,
<a id="l00299"></a>                                  void *user_data);
<a id="l00300"></a>
<a id="l00309"></a>typedef void (*can_state_change_callback_t)(const struct device *dev,
<a id="l00310"></a>                                            enum can_state state,
<a id="l00311"></a>                                            struct can_bus_err_cnt err_cnt,
<a id="l00312"></a>                                            void *user_data);
<a id="l00313"></a>
<a id="l00314"></a>struct can_state_change_callback;
<a id="l00315"></a>
<a id="l00324"></a>typedef void (*can_state_change_callback_handler_t)(const struct device *dev,
<a id="l00325"></a>                                                    struct can_state_change_callback *callback,
<a id="l00326"></a>                                                    enum can_state state,
<a id="l00327"></a>                                                    struct can_bus_err_cnt err_cnt);
<a id="l00342"></a>struct can_state_change_callback {
<a id="l00344"></a>        sys_snode_t node;
<a id="l00346"></a>        can_state_change_callback_handler_t handler;
<a id="l00347"></a>};
<a id="l00348"></a>
<a id="l00353"></a>
<a id="l00367"></a>#define CAN_CALC_TDCO(_timing_data, _tdco_min, _tdco_max)                                          \
<a id="l00368"></a>        CLAMP((1U + _timing_data-&gt;prop_seg + _timing_data-&gt;phase_seg1) * _timing_data-&gt;prescaler,  \
<a id="l00369"></a>              _tdco_min, _tdco_max)
<a id="l00370"></a>
<a id="l00377"></a>struct can_driver_config {
<a id="l00379"></a>        const struct device *phy;
<a id="l00381"></a>        uint32_t min_bitrate;
<a id="l00383"></a>        uint32_t max_bitrate;
<a id="l00385"></a>        uint32_t bitrate;
<a id="l00387"></a>        uint16_t sample_point;
<a id="l00388"></a>#if defined(CONFIG_CAN_FD_MODE) || defined(__DOXYGEN__)
<a id="l00390"></a>        uint16_t sample_point_data;
<a id="l00392"></a>        uint32_t bitrate_data;
<a id="l00393"></a>#endif /* CONFIG_CAN_FD_MODE */
<a id="l00394"></a>};
<a id="l00395"></a>
<a id="l00403"></a>#define CAN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)                           \
<a id="l00404"></a>        {                                                                                       \
<a id="l00405"></a>                .phy = DEVICE_DT_GET_OR_NULL(DT_PHANDLE(node_id, phys)),                        \
<a id="l00406"></a>                .min_bitrate = DT_CAN_TRANSCEIVER_MIN_BITRATE(node_id, _min_bitrate),           \
<a id="l00407"></a>                .max_bitrate = DT_CAN_TRANSCEIVER_MAX_BITRATE(node_id, _max_bitrate),           \
<a id="l00408"></a>                .bitrate = DT_PROP_OR(node_id, bitrate, CONFIG_CAN_DEFAULT_BITRATE),            \
<a id="l00409"></a>                .sample_point = DT_PROP_OR(node_id, sample_point, 0),                           \
<a id="l00410"></a>                IF_ENABLED(CONFIG_CAN_FD_MODE,                                                  \
<a id="l00411"></a>                        (.bitrate_data = DT_PROP_OR(node_id, bitrate_data,                      \
<a id="l00412"></a>                                                    CONFIG_CAN_DEFAULT_BITRATE_DATA),           \
<a id="l00413"></a>                         .sample_point_data = DT_PROP_OR(node_id, sample_point_data, 0),))      \
<a id="l00414"></a>        }
<a id="l00415"></a>
<a id="l00424"></a>#define CAN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)                         \
<a id="l00425"></a>        CAN_DT_DRIVER_CONFIG_GET(DT_DRV_INST(inst), _min_bitrate, _max_bitrate)
<a id="l00426"></a>
<a id="l00433"></a>struct can_driver_data {
<a id="l00435"></a>        can_mode_t mode;
<a id="l00437"></a>        bool started;
<a id="l00439"></a>        struct can_state_change_callback legacy_state_change_cb;
<a id="l00441"></a>        can_state_change_callback_t legacy_state_change_cb_handler;
<a id="l00443"></a>        void *legacy_state_change_cb_user_data;
<a id="l00445"></a>        struct k_spinlock state_change_callback_lock;
<a id="l00447"></a>        sys_slist_t state_change_callbacks;
<a id="l00448"></a>};
<a id="l00449"></a>
<a id="l00454"></a>typedef int (*can_set_timing_t)(const struct device *dev,
<a id="l00455"></a>                                const struct can_timing *timing);
<a id="l00456"></a>
<a id="l00461"></a>typedef int (*can_set_timing_data_t)(const struct device *dev,
<a id="l00462"></a>                                     const struct can_timing *timing_data);
<a id="l00463"></a>
<a id="l00468"></a>typedef int (*can_get_capabilities_t)(const struct device *dev, can_mode_t *cap);
<a id="l00469"></a>
<a id="l00474"></a>typedef int (*can_start_t)(const struct device *dev);
<a id="l00475"></a>
<a id="l00480"></a>typedef int (*can_stop_t)(const struct device *dev);
<a id="l00481"></a>
<a id="l00486"></a>typedef int (*can_set_mode_t)(const struct device *dev, can_mode_t mode);
<a id="l00487"></a>
<a id="l00495"></a>typedef int (*can_send_t)(const struct device *dev,
<a id="l00496"></a>                          const struct can_frame *frame,
<a id="l00497"></a>                          k_timeout_t timeout, can_tx_callback_t callback,
<a id="l00498"></a>                          void *user_data);
<a id="l00499"></a>
<a id="l00504"></a>typedef int (*can_add_rx_filter_t)(const struct device *dev,
<a id="l00505"></a>                                   can_rx_callback_t callback,
<a id="l00506"></a>                                   void *user_data,
<a id="l00507"></a>                                   const struct can_filter *filter);
<a id="l00508"></a>
<a id="l00513"></a>typedef void (*can_remove_rx_filter_t)(const struct device *dev, int filter_id);
<a id="l00514"></a>
<a id="l00519"></a>typedef int (*can_recover_t)(const struct device *dev, k_timeout_t timeout);
<a id="l00520"></a>
<a id="l00525"></a>typedef int (*can_get_state_t)(const struct device *dev, enum can_state *state,
<a id="l00526"></a>                               struct can_bus_err_cnt *err_cnt);
<a id="l00527"></a>
<a id="l00532"></a>typedef int (*can_get_core_clock_t)(const struct device *dev, uint32_t *rate);
<a id="l00533"></a>
<a id="l00538"></a>typedef int (*can_get_max_filters_t)(const struct device *dev, bool ide);
<a id="l00539"></a>
<a id="l00551"></a>typedef int (*can_state_change_callbacks_enabled_t)(const struct device *dev, bool enabled);
<a id="l00552"></a>
<a id="l00560"></a>void can_fire_state_change_callbacks(const struct device *dev, enum can_state state,
<a id="l00561"></a>                                     struct can_bus_err_cnt err_cnt);
<a id="l00562"></a>
<a id="l00566"></a>__subsystem struct can_driver_api {
<a id="l00570"></a>        can_get_capabilities_t get_capabilities;
<a id="l00574"></a>        can_start_t start;
<a id="l00578"></a>        can_stop_t stop;
<a id="l00582"></a>        can_set_mode_t set_mode;
<a id="l00586"></a>        can_set_timing_t set_timing;
<a id="l00590"></a>        can_send_t send;
<a id="l00594"></a>        can_add_rx_filter_t add_rx_filter;
<a id="l00598"></a>        can_remove_rx_filter_t remove_rx_filter;
<a id="l00599"></a>#if defined(CONFIG_CAN_MANUAL_RECOVERY_MODE) || defined(__DOXYGEN__)
<a id="l00604"></a>        can_recover_t recover;
<a id="l00605"></a>#endif /* CONFIG_CAN_MANUAL_RECOVERY_MODE */
<a id="l00609"></a>        can_get_state_t get_state;
<a id="l00613"></a>        can_state_change_callbacks_enabled_t state_change_callbacks_enabled;
<a id="l00617"></a>        can_get_core_clock_t get_core_clock;
<a id="l00621"></a>        can_get_max_filters_t get_max_filters;
<a id="l00623"></a>        struct can_timing timing_min;
<a id="l00625"></a>        struct can_timing timing_max;
<a id="l00626"></a>#if defined(CONFIG_CAN_FD_MODE) || defined(__DOXYGEN__)
<a id="l00631"></a>        can_set_timing_data_t set_timing_data;
<a id="l00635"></a>        struct can_timing timing_data_min;
<a id="l00639"></a>        struct can_timing timing_data_max;
<a id="l00640"></a>#endif /* CONFIG_CAN_FD_MODE */
<a id="l00641"></a>};
<a id="l00642"></a>
<a id="l00645"></a>
<a id="l00646"></a>#if defined(CONFIG_CAN_STATS) || defined(__DOXYGEN__)
<a id="l00647"></a>
<a id="l00648"></a>#include &lt;zephyr/stats/stats.h&gt;
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00652"></a>STATS_SECT_START(can)
<a id="l00653"></a>STATS_SECT_ENTRY32(bit_error)
<a id="l00654"></a>STATS_SECT_ENTRY32(bit0_error)
<a id="l00655"></a>STATS_SECT_ENTRY32(bit1_error)
<a id="l00656"></a>STATS_SECT_ENTRY32(stuff_error)
<a id="l00657"></a>STATS_SECT_ENTRY32(crc_error)
<a id="l00658"></a>STATS_SECT_ENTRY32(form_error)
<a id="l00659"></a>STATS_SECT_ENTRY32(ack_error)
<a id="l00660"></a>STATS_SECT_ENTRY32(rx_overrun)
<a id="l00661"></a>STATS_SECT_END;
<a id="l00662"></a>
<a id="l00663"></a>STATS_NAME_START(can)
<a id="l00664"></a>STATS_NAME(can, bit_error)
<a id="l00665"></a>STATS_NAME(can, bit0_error)
<a id="l00666"></a>STATS_NAME(can, bit1_error)
<a id="l00667"></a>STATS_NAME(can, stuff_error)
<a id="l00668"></a>STATS_NAME(can, crc_error)
<a id="l00669"></a>STATS_NAME(can, form_error)
<a id="l00670"></a>STATS_NAME(can, ack_error)
<a id="l00671"></a>STATS_NAME(can, rx_overrun)
<a id="l00672"></a>STATS_NAME_END(can);
<a id="l00673"></a>
<a id="l00675"></a>
<a id="l00682"></a>struct can_device_state {
<a id="l00684"></a>        struct device_state devstate;
<a id="l00686"></a>        struct stats_can stats;
<a id="l00687"></a>};
<a id="l00688"></a>
<a id="l00690"></a>
<a id="l00694"></a>#define Z_CAN_GET_STATS(dev_)                           \
<a id="l00695"></a>        CONTAINER_OF(dev_-&gt;state, struct can_device_state, devstate)-&gt;stats
<a id="l00696"></a>
<a id="l00698"></a>
<a id="l00717"></a>#define CAN_STATS_BIT_ERROR_INC(dev_)                  \
<a id="l00718"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), bit_error)
<a id="l00719"></a>
<a id="l00733"></a>#define CAN_STATS_BIT0_ERROR_INC(dev_)                          \
<a id="l00734"></a>        do {                                                    \
<a id="l00735"></a>                STATS_INC(Z_CAN_GET_STATS(dev_), bit0_error);   \
<a id="l00736"></a>                CAN_STATS_BIT_ERROR_INC(dev_);                  \
<a id="l00737"></a>        } while (0)
<a id="l00738"></a>
<a id="l00752"></a>#define CAN_STATS_BIT1_ERROR_INC(dev_)                          \
<a id="l00753"></a>        do {                                                    \
<a id="l00754"></a>                STATS_INC(Z_CAN_GET_STATS(dev_), bit1_error);   \
<a id="l00755"></a>                CAN_STATS_BIT_ERROR_INC(dev_);                  \
<a id="l00756"></a>        } while (0)
<a id="l00757"></a>
<a id="l00768"></a>#define CAN_STATS_STUFF_ERROR_INC(dev_)                 \
<a id="l00769"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), stuff_error)
<a id="l00770"></a>
<a id="l00781"></a>#define CAN_STATS_CRC_ERROR_INC(dev_)                   \
<a id="l00782"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), crc_error)
<a id="l00783"></a>
<a id="l00794"></a>#define CAN_STATS_FORM_ERROR_INC(dev_)                  \
<a id="l00795"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), form_error)
<a id="l00796"></a>
<a id="l00807"></a>#define CAN_STATS_ACK_ERROR_INC(dev_)                   \
<a id="l00808"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), ack_error)
<a id="l00809"></a>
<a id="l00821"></a>#define CAN_STATS_RX_OVERRUN_INC(dev_)                  \
<a id="l00822"></a>        STATS_INC(Z_CAN_GET_STATS(dev_), rx_overrun)
<a id="l00823"></a>
<a id="l00834"></a>#define CAN_STATS_RESET(dev_)                           \
<a id="l00835"></a>        stats_reset(&amp;(Z_CAN_GET_STATS(dev_).s_hdr))
<a id="l00836"></a>
<a id="l00838"></a>
<a id="l00844"></a>#define Z_CAN_DEVICE_STATE_DEFINE(dev_id)                               \
<a id="l00845"></a>        static struct can_device_state Z_DEVICE_STATE_NAME(dev_id)      \
<a id="l00846"></a>        __attribute__((__section__(".z_devstate")))
<a id="l00847"></a>
<a id="l00856"></a>#define Z_CAN_INIT_FN(dev_id, init_fn)                                  \
<a id="l00857"></a>        static inline int UTIL_CAT(dev_id, _init)(const struct device *dev) \
<a id="l00858"></a>        {                                                               \
<a id="l00859"></a>                struct can_device_state *state =                        \
<a id="l00860"></a>                        CONTAINER_OF(dev-&gt;state, struct can_device_state, devstate); \
<a id="l00861"></a>                stats_init(&amp;state-&gt;stats.s_hdr, STATS_SIZE_32, 8,       \
<a id="l00862"></a>                           STATS_NAME_INIT_PARMS(can));                 \
<a id="l00863"></a>                stats_register(dev-&gt;name, &amp;(state-&gt;stats.s_hdr));       \
<a id="l00864"></a>                if (!is_null_no_warn(init_fn)) {                        \
<a id="l00865"></a>                        return init_fn(dev);                            \
<a id="l00866"></a>                }                                                       \
<a id="l00867"></a>                                                                        \
<a id="l00868"></a>                return 0;                                               \
<a id="l00869"></a>        }
<a id="l00870"></a>
<a id="l00872"></a>
<a id="l00894"></a>#define CAN_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, \
<a id="l00895"></a>                             prio, api, ...)                            \
<a id="l00896"></a>        IF_ENABLED(CONFIG_NET_CANBUS, (Z_NET_CANBUS_DEVICE_DT_DEFINE(node_id))) \
<a id="l00897"></a>        Z_CAN_DEVICE_STATE_DEFINE(Z_DEVICE_DT_DEV_ID(node_id));         \
<a id="l00898"></a>        Z_CAN_INIT_FN(Z_DEVICE_DT_DEV_ID(node_id), init_fn)             \
<a id="l00899"></a>        Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id),           \
<a id="l00900"></a>                        DEVICE_DT_NAME(node_id),                        \
<a id="l00901"></a>                        &amp;UTIL_CAT(Z_DEVICE_DT_DEV_ID(node_id), _init),  \
<a id="l00902"></a>                        NULL, Z_DEVICE_DT_FLAGS(node_id), pm, data,     \
<a id="l00903"></a>                        config, level, prio, api,                       \
<a id="l00904"></a>                        &amp;(Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_ID(node_id)).devstate), \
<a id="l00905"></a>                        __VA_ARGS__)
<a id="l00906"></a>
<a id="l00907"></a>#else /* CONFIG_CAN_STATS */
<a id="l00908"></a>
<a id="l00909"></a>#define CAN_STATS_BIT_ERROR_INC(dev_)
<a id="l00910"></a>#define CAN_STATS_BIT0_ERROR_INC(dev_)
<a id="l00911"></a>#define CAN_STATS_BIT1_ERROR_INC(dev_)
<a id="l00912"></a>#define CAN_STATS_STUFF_ERROR_INC(dev_)
<a id="l00913"></a>#define CAN_STATS_CRC_ERROR_INC(dev_)
<a id="l00914"></a>#define CAN_STATS_FORM_ERROR_INC(dev_)
<a id="l00915"></a>#define CAN_STATS_ACK_ERROR_INC(dev_)
<a id="l00916"></a>#define CAN_STATS_RX_OVERRUN_INC(dev_)
<a id="l00917"></a>#define CAN_STATS_RESET(dev_)
<a id="l00918"></a>
<a id="l00919"></a>#define CAN_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, \
<a id="l00920"></a>                             prio, api, ...)                            \
<a id="l00921"></a>        IF_ENABLED(CONFIG_NET_CANBUS, (Z_NET_CANBUS_DEVICE_DT_DEFINE(node_id))) \
<a id="l00922"></a>        DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level,     \
<a id="l00923"></a>                         prio, api, __VA_ARGS__)
<a id="l00924"></a>
<a id="l00925"></a>#endif /* CONFIG_CAN_STATS */
<a id="l00926"></a>
<a id="l00934"></a>#define CAN_DEVICE_DT_INST_DEFINE(inst, ...)                    \
<a id="l00935"></a>        CAN_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
<a id="l00936"></a>
<a id="l00942"></a>
<a id="l00955"></a>__syscall int can_get_core_clock(const struct device *dev, uint32_t *rate);
<a id="l00956"></a>
<a id="l00957"></a>static inline int z_impl_can_get_core_clock(const struct device *dev, uint32_t *rate)
<a id="l00958"></a>{
<a id="l00959"></a>        return DEVICE_API_GET(can, dev)-&gt;get_core_clock(dev, rate);
<a id="l00960"></a>}
<a id="l00961"></a>
<a id="l00978"></a>__syscall uint32_t can_get_bitrate_min(const struct device *dev);
<a id="l00979"></a>
<a id="l00980"></a>static inline uint32_t z_impl_can_get_bitrate_min(const struct device *dev)
<a id="l00981"></a>{
<a id="l00982"></a>        const struct can_driver_config *common = (const struct can_driver_config *)dev-&gt;config;
<a id="l00983"></a>
<a id="l00984"></a>        return common-&gt;min_bitrate;
<a id="l00985"></a>}
<a id="l00986"></a>
<a id="l01003"></a>__syscall uint32_t can_get_bitrate_max(const struct device *dev);
<a id="l01004"></a>
<a id="l01005"></a>static inline uint32_t z_impl_can_get_bitrate_max(const struct device *dev)
<a id="l01006"></a>{
<a id="l01007"></a>        const struct can_driver_config *common = (const struct can_driver_config *)dev-&gt;config;
<a id="l01008"></a>
<a id="l01009"></a>        return common-&gt;max_bitrate;
<a id="l01010"></a>}
<a id="l01011"></a>
<a id="l01019"></a>__syscall const struct can_timing *can_get_timing_min(const struct device *dev);
<a id="l01020"></a>
<a id="l01021"></a>static inline const struct can_timing *z_impl_can_get_timing_min(const struct device *dev)
<a id="l01022"></a>{
<a id="l01023"></a>        return &amp;DEVICE_API_GET(can, dev)-&gt;timing_min;
<a id="l01024"></a>}
<a id="l01025"></a>
<a id="l01033"></a>__syscall const struct can_timing *can_get_timing_max(const struct device *dev);
<a id="l01034"></a>
<a id="l01035"></a>static inline const struct can_timing *z_impl_can_get_timing_max(const struct device *dev)
<a id="l01036"></a>{
<a id="l01037"></a>        return &amp;DEVICE_API_GET(can, dev)-&gt;timing_max;
<a id="l01038"></a>}
<a id="l01039"></a>
<a id="l01066"></a>__syscall int can_calc_timing(const struct device *dev, struct can_timing *res,
<a id="l01067"></a>                              uint32_t bitrate, uint16_t sample_pnt);
<a id="l01068"></a>
<a id="l01082"></a>__syscall const struct can_timing *can_get_timing_data_min(const struct device *dev);
<a id="l01083"></a>
<a id="l01084"></a>#ifdef CONFIG_CAN_FD_MODE
<a id="l01085"></a>static inline const struct can_timing *z_impl_can_get_timing_data_min(const struct device *dev)
<a id="l01086"></a>{
<a id="l01087"></a>        return &amp;DEVICE_API_GET(can, dev)-&gt;timing_data_min;
<a id="l01088"></a>}
<a id="l01089"></a>#endif /* CONFIG_CAN_FD_MODE */
<a id="l01090"></a>
<a id="l01104"></a>__syscall const struct can_timing *can_get_timing_data_max(const struct device *dev);
<a id="l01105"></a>
<a id="l01106"></a>#ifdef CONFIG_CAN_FD_MODE
<a id="l01107"></a>static inline const struct can_timing *z_impl_can_get_timing_data_max(const struct device *dev)
<a id="l01108"></a>{
<a id="l01109"></a>        return &amp;DEVICE_API_GET(can, dev)-&gt;timing_data_max;
<a id="l01110"></a>}
<a id="l01111"></a>#endif /* CONFIG_CAN_FD_MODE */
<a id="l01112"></a>
<a id="l01133"></a>__syscall int can_calc_timing_data(const struct device *dev, struct can_timing *res,
<a id="l01134"></a>                                   uint32_t bitrate, uint16_t sample_pnt);
<a id="l01135"></a>
<a id="l01153"></a>__syscall int can_set_timing_data(const struct device *dev,
<a id="l01154"></a>                                  const struct can_timing *timing_data);
<a id="l01155"></a>
<a id="l01184"></a>__syscall int can_set_bitrate_data(const struct device *dev, uint32_t bitrate_data);
<a id="l01185"></a>
<a id="l01199"></a>__syscall int can_set_timing(const struct device *dev,
<a id="l01200"></a>                             const struct can_timing *timing);
<a id="l01201"></a>
<a id="l01215"></a>__syscall int can_get_capabilities(const struct device *dev, can_mode_t *cap);
<a id="l01216"></a>
<a id="l01217"></a>static inline int z_impl_can_get_capabilities(const struct device *dev, can_mode_t *cap)
<a id="l01218"></a>{
<a id="l01219"></a>        return DEVICE_API_GET(can, dev)-&gt;get_capabilities(dev, cap);
<a id="l01220"></a>}
<a id="l01221"></a>
<a id="l01231"></a>__syscall const struct device *can_get_transceiver(const struct device *dev);
<a id="l01232"></a>
<a id="l01233"></a>static const struct device *z_impl_can_get_transceiver(const struct device *dev)
<a id="l01234"></a>{
<a id="l01235"></a>        const struct can_driver_config *common = (const struct can_driver_config *)dev-&gt;config;
<a id="l01236"></a>
<a id="l01237"></a>        return common-&gt;phy;
<a id="l01238"></a>}
<a id="l01239"></a>
<a id="l01257"></a>__syscall int can_start(const struct device *dev);
<a id="l01258"></a>
<a id="l01259"></a>static inline int z_impl_can_start(const struct device *dev)
<a id="l01260"></a>{
<a id="l01261"></a>        return DEVICE_API_GET(can, dev)-&gt;start(dev);
<a id="l01262"></a>}
<a id="l01263"></a>
<a id="l01279"></a>__syscall int can_stop(const struct device *dev);
<a id="l01280"></a>
<a id="l01281"></a>static inline int z_impl_can_stop(const struct device *dev)
<a id="l01282"></a>{
<a id="l01283"></a>        return DEVICE_API_GET(can, dev)-&gt;stop(dev);
<a id="l01284"></a>}
<a id="l01285"></a>
<a id="l01297"></a>__syscall int can_set_mode(const struct device *dev, can_mode_t mode);
<a id="l01298"></a>
<a id="l01299"></a>static inline int z_impl_can_set_mode(const struct device *dev, can_mode_t mode)
<a id="l01300"></a>{
<a id="l01301"></a>        return DEVICE_API_GET(can, dev)-&gt;set_mode(dev, mode);
<a id="l01302"></a>}
<a id="l01303"></a>
<a id="l01311"></a>__syscall can_mode_t can_get_mode(const struct device *dev);
<a id="l01312"></a>
<a id="l01313"></a>static inline can_mode_t z_impl_can_get_mode(const struct device *dev)
<a id="l01314"></a>{
<a id="l01315"></a>        const struct can_driver_data *common = (const struct can_driver_data *)dev-&gt;data;
<a id="l01316"></a>
<a id="l01317"></a>        return common-&gt;mode;
<a id="l01318"></a>}
<a id="l01319"></a>
<a id="l01345"></a>__syscall int can_set_bitrate(const struct device *dev, uint32_t bitrate);
<a id="l01346"></a>
<a id="l01348"></a>
<a id="l01354"></a>
<a id="l01399"></a>__syscall int can_send(const struct device *dev, const struct can_frame *frame,
<a id="l01400"></a>                       k_timeout_t timeout, can_tx_callback_t callback,
<a id="l01401"></a>                       void *user_data);
<a id="l01402"></a>
<a id="l01404"></a>
<a id="l01410"></a>
<a id="l01435"></a>int can_add_rx_filter(const struct device *dev, can_rx_callback_t callback,
<a id="l01436"></a>                      void *user_data, const struct can_filter *filter);
<a id="l01437"></a>
<a id="l01448"></a>#define CAN_MSGQ_DEFINE(name, max_frames) \
<a id="l01449"></a>        K_MSGQ_DEFINE_TYPE(name, struct can_frame, max_frames)
<a id="l01450"></a>
<a id="l01491"></a>__syscall int can_add_rx_filter_msgq(const struct device *dev, struct k_msgq *msgq,
<a id="l01492"></a>                                     const struct can_filter *filter);
<a id="l01493"></a>
<a id="l01503"></a>__syscall void can_remove_rx_filter(const struct device *dev, int filter_id);
<a id="l01504"></a>
<a id="l01505"></a>static inline void z_impl_can_remove_rx_filter(const struct device *dev, int filter_id)
<a id="l01506"></a>{
<a id="l01507"></a>        DEVICE_API_GET(can, dev)-&gt;remove_rx_filter(dev, filter_id);
<a id="l01508"></a>}
<a id="l01509"></a>
<a id="l01523"></a>__syscall int can_get_max_filters(const struct device *dev, bool ide);
<a id="l01524"></a>
<a id="l01525"></a>static inline int z_impl_can_get_max_filters(const struct device *dev, bool ide)
<a id="l01526"></a>{
<a id="l01527"></a>        const struct can_driver_api *api = DEVICE_API_GET(can, dev);
<a id="l01528"></a>
<a id="l01529"></a>        if (api-&gt;get_max_filters == NULL) {
<a id="l01530"></a>                return -ENOSYS;
<a id="l01531"></a>        }
<a id="l01532"></a>
<a id="l01533"></a>        return api-&gt;get_max_filters(dev, ide);
<a id="l01534"></a>}
<a id="l01535"></a>
<a id="l01537"></a>
<a id="l01543"></a>
<a id="l01557"></a>__syscall int can_get_state(const struct device *dev, enum can_state *state,
<a id="l01558"></a>                            struct can_bus_err_cnt *err_cnt);
<a id="l01559"></a>
<a id="l01560"></a>static inline int z_impl_can_get_state(const struct device *dev, enum can_state *state,
<a id="l01561"></a>                                       struct can_bus_err_cnt *err_cnt)
<a id="l01562"></a>{
<a id="l01563"></a>        return DEVICE_API_GET(can, dev)-&gt;get_state(dev, state, err_cnt);
<a id="l01564"></a>}
<a id="l01565"></a>
<a id="l01584"></a>__syscall int can_recover(const struct device *dev, k_timeout_t timeout);
<a id="l01585"></a>
<a id="l01586"></a>#ifdef CONFIG_CAN_MANUAL_RECOVERY_MODE
<a id="l01587"></a>static inline int z_impl_can_recover(const struct device *dev, k_timeout_t timeout)
<a id="l01588"></a>{
<a id="l01589"></a>        const struct can_driver_api *api = DEVICE_API_GET(can, dev);
<a id="l01590"></a>
<a id="l01591"></a>        if (api-&gt;recover == NULL) {
<a id="l01592"></a>                return -ENOSYS;
<a id="l01593"></a>        }
<a id="l01594"></a>
<a id="l01595"></a>        return api-&gt;recover(dev, timeout);
<a id="l01596"></a>}
<a id="l01597"></a>#endif /* CONFIG_CAN_MANUAL_RECOVERY_MODE */
<a id="l01598"></a>
<a id="l01614"></a>__deprecated void can_set_state_change_callback(const struct device *dev,
<a id="l01615"></a>                                                can_state_change_callback_t callback,
<a id="l01616"></a>                                                void *user_data);
<a id="l01617"></a>
<a id="l01624"></a>static inline void can_init_state_change_callback(struct can_state_change_callback *callback,
<a id="l01625"></a>                                                  can_state_change_callback_handler_t handler)
<a id="l01626"></a>{
<a id="l01627"></a>        __ASSERT_NO_MSG(callback != NULL);
<a id="l01628"></a>        __ASSERT_NO_MSG(handler != NULL);
<a id="l01629"></a>
<a id="l01630"></a>        callback-&gt;handler = handler;
<a id="l01631"></a>}
<a id="l01632"></a>
<a id="l01643"></a>int can_add_state_change_callback(const struct device *dev,
<a id="l01644"></a>                                  struct can_state_change_callback *callback);
<a id="l01645"></a>
<a id="l01656"></a>int can_remove_state_change_callback(const struct device *dev,
<a id="l01657"></a>                                     struct can_state_change_callback *callback);
<a id="l01658"></a>
<a id="l01660"></a>
<a id="l01666"></a>
<a id="l01679"></a>__syscall uint32_t can_stats_get_bit_errors(const struct device *dev);
<a id="l01680"></a>
<a id="l01681"></a>#ifdef CONFIG_CAN_STATS
<a id="l01682"></a>static inline uint32_t z_impl_can_stats_get_bit_errors(const struct device *dev)
<a id="l01683"></a>{
<a id="l01684"></a>        return Z_CAN_GET_STATS(dev).bit_error;
<a id="l01685"></a>}
<a id="l01686"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01687"></a>
<a id="l01702"></a>__syscall uint32_t can_stats_get_bit0_errors(const struct device *dev);
<a id="l01703"></a>
<a id="l01704"></a>#ifdef CONFIG_CAN_STATS
<a id="l01705"></a>static inline uint32_t z_impl_can_stats_get_bit0_errors(const struct device *dev)
<a id="l01706"></a>{
<a id="l01707"></a>        return Z_CAN_GET_STATS(dev).bit0_error;
<a id="l01708"></a>}
<a id="l01709"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01710"></a>
<a id="l01725"></a>__syscall uint32_t can_stats_get_bit1_errors(const struct device *dev);
<a id="l01726"></a>
<a id="l01727"></a>#ifdef CONFIG_CAN_STATS
<a id="l01728"></a>static inline uint32_t z_impl_can_stats_get_bit1_errors(const struct device *dev)
<a id="l01729"></a>{
<a id="l01730"></a>        return Z_CAN_GET_STATS(dev).bit1_error;
<a id="l01731"></a>}
<a id="l01732"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01733"></a>
<a id="l01746"></a>__syscall uint32_t can_stats_get_stuff_errors(const struct device *dev);
<a id="l01747"></a>
<a id="l01748"></a>#ifdef CONFIG_CAN_STATS
<a id="l01749"></a>static inline uint32_t z_impl_can_stats_get_stuff_errors(const struct device *dev)
<a id="l01750"></a>{
<a id="l01751"></a>        return Z_CAN_GET_STATS(dev).stuff_error;
<a id="l01752"></a>}
<a id="l01753"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01754"></a>
<a id="l01767"></a>__syscall uint32_t can_stats_get_crc_errors(const struct device *dev);
<a id="l01768"></a>
<a id="l01769"></a>#ifdef CONFIG_CAN_STATS
<a id="l01770"></a>static inline uint32_t z_impl_can_stats_get_crc_errors(const struct device *dev)
<a id="l01771"></a>{
<a id="l01772"></a>        return Z_CAN_GET_STATS(dev).crc_error;
<a id="l01773"></a>}
<a id="l01774"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01775"></a>
<a id="l01788"></a>__syscall uint32_t can_stats_get_form_errors(const struct device *dev);
<a id="l01789"></a>
<a id="l01790"></a>#ifdef CONFIG_CAN_STATS
<a id="l01791"></a>static inline uint32_t z_impl_can_stats_get_form_errors(const struct device *dev)
<a id="l01792"></a>{
<a id="l01793"></a>        return Z_CAN_GET_STATS(dev).form_error;
<a id="l01794"></a>}
<a id="l01795"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01796"></a>
<a id="l01809"></a>__syscall uint32_t can_stats_get_ack_errors(const struct device *dev);
<a id="l01810"></a>
<a id="l01811"></a>#ifdef CONFIG_CAN_STATS
<a id="l01812"></a>static inline uint32_t z_impl_can_stats_get_ack_errors(const struct device *dev)
<a id="l01813"></a>{
<a id="l01814"></a>        return Z_CAN_GET_STATS(dev).ack_error;
<a id="l01815"></a>}
<a id="l01816"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01817"></a>
<a id="l01831"></a>__syscall uint32_t can_stats_get_rx_overruns(const struct device *dev);
<a id="l01832"></a>
<a id="l01833"></a>#ifdef CONFIG_CAN_STATS
<a id="l01834"></a>static inline uint32_t z_impl_can_stats_get_rx_overruns(const struct device *dev)
<a id="l01835"></a>{
<a id="l01836"></a>        return Z_CAN_GET_STATS(dev).rx_overrun;
<a id="l01837"></a>}
<a id="l01838"></a>#endif /* CONFIG_CAN_STATS */
<a id="l01839"></a>
<a id="l01841"></a>
<a id="l01847"></a>
<a id="l01855"></a>static inline uint8_t can_dlc_to_bytes(uint8_t dlc)
<a id="l01856"></a>{
<a id="l01857"></a>        static const uint8_t dlc_table[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12,
<a id="l01858"></a>                                            16, 20, 24, 32, 48, 64};
<a id="l01859"></a>
<a id="l01860"></a>        return dlc_table[MIN(dlc, ARRAY_SIZE(dlc_table) - 1)];
<a id="l01861"></a>}
<a id="l01862"></a>
<a id="l01870"></a>static inline uint8_t can_bytes_to_dlc(uint8_t num_bytes)
<a id="l01871"></a>{
<a id="l01872"></a>        return num_bytes &lt;= 8  ? num_bytes :
<a id="l01873"></a>               num_bytes &lt;= 12 ? 9 :
<a id="l01874"></a>               num_bytes &lt;= 16 ? 10 :
<a id="l01875"></a>               num_bytes &lt;= 20 ? 11 :
<a id="l01876"></a>               num_bytes &lt;= 24 ? 12 :
<a id="l01877"></a>               num_bytes &lt;= 32 ? 13 :
<a id="l01878"></a>               num_bytes &lt;= 48 ? 14 :
<a id="l01879"></a>               15;
<a id="l01880"></a>}
<a id="l01881"></a>
<a id="l01889"></a>static inline bool can_frame_matches_filter(const struct can_frame *frame,
<a id="l01890"></a>                                            const struct can_filter *filter)
<a id="l01891"></a>{
<a id="l01892"></a>        if ((frame-&gt;flags &amp; CAN_FRAME_IDE) != 0 &amp;&amp; (filter-&gt;flags &amp; CAN_FILTER_IDE) == 0) {
<a id="l01893"></a>                /* Extended (29-bit) ID frame, standard (11-bit) filter */
<a id="l01894"></a>                return false;
<a id="l01895"></a>        }
<a id="l01896"></a>
<a id="l01897"></a>        if ((frame-&gt;flags &amp; CAN_FRAME_IDE) == 0 &amp;&amp; (filter-&gt;flags &amp; CAN_FILTER_IDE) != 0) {
<a id="l01898"></a>                /* Standard (11-bit) ID frame, extended (29-bit) filter */
<a id="l01899"></a>                return false;
<a id="l01900"></a>        }
<a id="l01901"></a>
<a id="l01902"></a>        if ((frame-&gt;id ^ filter-&gt;id) &amp; filter-&gt;mask) {
<a id="l01903"></a>                /* Masked ID mismatch */
<a id="l01904"></a>                return false;
<a id="l01905"></a>        }
<a id="l01906"></a>
<a id="l01907"></a>        return true;
<a id="l01908"></a>}
<a id="l01909"></a>
<a id="l01911"></a>
<a id="l01915"></a>
<a id="l01916"></a>#ifdef __cplusplus
<a id="l01917"></a>}
<a id="l01918"></a>#endif
<a id="l01919"></a>
<a id="l01920"></a>#include &lt;zephyr/syscalls/can.h&gt;
<a id="l01921"></a>
<a id="l01922"></a>#if defined(CONFIG_NET_CANBUS)
<a id="l01923"></a>/* Provides Z_NET_CANBUS_DEVICE_DT_DEFINE() for CAN_DEVICE_DT_DEFINE() */
<a id="l01924"></a>#include &lt;zephyr/net/canbus.h&gt;
<a id="l01925"></a>#endif
<a id="l01926"></a>
<a id="l01927"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_CAN_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2021-2026 Vestas Wind Systems A/S；Copyright (c) 2018 Karsten Koenig；Copyright (c) 2018 Alexander Wachter；Apache-2.0许可证原文保留。

2. 结束CONFIG_CAN_FD_MODE控制的帧载荷容量选择。

3. 结束CONFIG_CAN_FD_MODE相关数据阶段配置字段。

4. 结束CONFIG_CAN_MANUAL_RECOVERY_MODE相关手动恢复操作成员。

5. 结束CONFIG_CAN_FD_MODE相关数据阶段驱动操作与时序字段。

6. 进入未启用CONFIG_CAN_STATS时的替代分支。

7. 结束CONFIG_CAN_STATS相关统计与设备定义分支。

8. 结束CONFIG_CAN_FD_MODE相关数据阶段最小时序查询实现。

9. 结束CONFIG_CAN_FD_MODE相关数据阶段最大时序查询实现。

10. 结束CONFIG_CAN_MANUAL_RECOVERY_MODE相关恢复实现。

11. 结束CONFIG_CAN_STATS相关位错误统计查询实现。

12. 结束CONFIG_CAN_STATS相关位0错误统计查询实现。

13. 结束CONFIG_CAN_STATS相关位1错误统计查询实现。

14. 结束CONFIG_CAN_STATS相关位填充错误统计查询实现。

15. 结束CONFIG_CAN_STATS相关CRC错误统计查询实现。

16. 结束CONFIG_CAN_STATS相关格式错误统计查询实现。

17. 结束CONFIG_CAN_STATS相关应答错误统计查询实现。

18. 结束CONFIG_CAN_STATS相关接收溢出统计查询实现。

19. 帧使用扩展29位ID，而过滤器使用标准11位ID。

20. 帧使用标准11位ID，而过滤器使用扩展29位ID。

21. 施加掩码之后的ID不匹配。

22. 为CAN_DEVICE_DT_DEFINE()提供Z_NET_CANBUS_DEVICE_DT_DEFINE()。

23. 结束CAN驱动头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_CAN_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

### `canbus.h`

CAN总线套接字（Socket）API定义。

符号定位：[canbus.h](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html)。

### `clock.h`

系统时钟API（System Clock APIs）。

符号定位：[clock.h](../timer_reference/P090_系统时钟头文件参考.md)。

### `device.h`

Zephyr设备模型（Device Model）的API与宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `DEVICE_API_GET`

```c
#define DEVICE_API_GET(_class, _dev)
```

展开为指定设备类别的设备API指针。

定义位置（Definition）：device.h:1486。

符号定位：[DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)。

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `can_set_timing_t`

```c
int(* can_set_timing_t)(const struct device *dev, const struct can_timing *timing)
```

设置CAN总线时序时调用的回调API；参数说明见can_set_timing()。

定义位置（Definition）：can.h:454。

符号定位：[can_set_timing_t](../hardware/P369_CAN控制器后端接口.md#ga01a5f028d947582dd4195b467dae8b94)。

### `can_get_state_t`

```c
int(* can_get_state_t)(const struct device *dev, enum can_state *state, struct can_bus_err_cnt *err_cnt)
```

取得CAN控制器状态时调用的回调API；参数说明见can_get_state()。

定义位置（Definition）：can.h:525。

符号定位：[can_get_state_t](../hardware/P369_CAN控制器后端接口.md#ga14210ea7870ef23072cd61c10043540f)。

### `can_stop_t`

```c
int(* can_stop_t)(const struct device *dev)
```

停止CAN控制器时调用的回调API；参数说明见can_stop()。

定义位置（Definition）：can.h:480。

符号定位：[can_stop_t](../hardware/P369_CAN控制器后端接口.md#ga1ab69e7991b8492e36c4b3f359db1961)。

### `can_remove_rx_filter_t`

```c
void(* can_remove_rx_filter_t)(const struct device *dev, int filter_id)
```

移除接收过滤器时调用的回调API；参数说明见can_remove_rx_filter()。

定义位置（Definition）：can.h:513。

符号定位：[can_remove_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga20ee94c5122acb6fd7fe5939a20ba748)。

### `can_set_mode_t`

```c
int(* can_set_mode_t)(const struct device *dev, can_mode_t mode)
```

设置CAN控制器模式时调用的回调API；参数说明见can_set_mode()。

定义位置（Definition）：can.h:486。

符号定位：[can_set_mode_t](../hardware/P369_CAN控制器后端接口.md#ga231b61f4d1413e0d28dd5a8bc25a89b3)。

### `can_get_capabilities_t`

```c
int(* can_get_capabilities_t)(const struct device *dev, can_mode_t *cap)
```

取得CAN控制器能力时调用的回调API；参数说明见can_get_capabilities()……（原符号提示在此截断）。

定义位置（Definition）：can.h:468。

符号定位：[can_get_capabilities_t](../hardware/P369_CAN控制器后端接口.md#ga2fd489217c19977d239d51f0b3fcfc19)。

### `can_add_rx_filter_t`

```c
int(* can_add_rx_filter_t)(const struct device *dev, can_rx_callback_t callback, void *user_data, const struct can_filter *filter)
```

添加接收过滤器（RX Filter）时调用的回调API；参数说明见can_add_rx_filter()。

定义位置（Definition）：can.h:504。

符号定位：[can_add_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga3bc249502cb65bf89bce2ca87535ac6b)。

### `can_get_core_clock_t`

```c
int(* can_get_core_clock_t)(const struct device *dev, uint32_t *rate)
```

取得CAN核心时钟频率（Core Clock Rate）时调用的回调API；参数说明见can_get_core_clock()。

定义位置（Definition）：can.h:532。

符号定位：[can_get_core_clock_t](../hardware/P369_CAN控制器后端接口.md#ga4d44354cda4cfe0af5262189549d6523)。

### `can_set_timing_data_t`

```c
int(* can_set_timing_data_t)(const struct device *dev, const struct can_timing *timing_data)
```

设置CAN FD数据阶段总线时序时调用的可选回调API（Optional Callback API）。

定义位置（Definition）：can.h:461。

符号定位：[can_set_timing_data_t](../hardware/P369_CAN控制器后端接口.md#ga7be2d21503b59cde52369d589ccff80f)。

### `can_state_change_callbacks_enabled_t`

```c
int(* can_state_change_callbacks_enabled_t)(const struct device *dev, bool enabled)
```

用于通知状态变化回调何时启用的可选回调API。

定义位置（Definition）：can.h:551。

符号定位：[can_state_change_callbacks_enabled_t](../hardware/P369_CAN控制器后端接口.md#ga80424a027933c3bc0d973f37333d2618)。

### `can_send_t`

```c
int(* can_send_t)(const struct device *dev, const struct can_frame *frame, k_timeout_t timeout, can_tx_callback_t callback, void *user_data)
```

发送CAN帧时调用的回调API；参数说明见can_send()。

定义位置（Definition）：can.h:495。

符号定位：[can_send_t](../hardware/P369_CAN控制器后端接口.md#ga89108f1d99fa1ba784808f1e99763a58)。

### `can_recover_t`

```c
int(* can_recover_t)(const struct device *dev, k_timeout_t timeout)
```

手动将CAN控制器从总线关闭状态恢复时调用的可选回调API；参见can_recover……（原符号提示在此截断）。

定义位置（Definition）：can.h:519。

符号定位：[can_recover_t](../hardware/P369_CAN控制器后端接口.md#ga8bcafa14e23f2ba70e17c1432449d744)。

### `can_get_max_filters_t`

```c
int(* can_get_max_filters_t)(const struct device *dev, bool ide)
```

取得可同时使用的CAN接收过滤器最大数量时调用的可选回调API；参见can_get_max_fi……（原符号提示在此截断）。

定义位置（Definition）：can.h:538。

符号定位：[can_get_max_filters_t](../hardware/P369_CAN控制器后端接口.md#ga946dd40c12eba40c34afa7572d61456c)。

### `can_fire_state_change_callbacks`

```c
void can_fire_state_change_callbacks(const struct device *dev, enum can_state state, struct can_bus_err_cnt err_cnt)
```

触发已注册的CAN状态变化处理回调。

符号定位：[can_fire_state_change_callbacks](../hardware/P369_CAN控制器后端接口.md#gaba24cc4eb2fa759ff8394dd096021982)。

### `can_start_t`

```c
int(* can_start_t)(const struct device *dev)
```

启动CAN控制器时调用的回调API；参数说明见can_start()。

定义位置（Definition）：can.h:474。

符号定位：[can_start_t](../hardware/P369_CAN控制器后端接口.md#gaecca113e6b8cc7caba3d19fdd104aaa7)。

### `can_state_change_callback_t`

```c
void(* can_state_change_callback_t)(const struct device *dev, enum can_state state, struct can_bus_err_cnt err_cnt, void *user_data)
```

定义状态变化回调处理函数的签名。

定义位置（Definition）：can.h:309。

符号定位：[can_state_change_callback_t](../hardware/P362_CAN控制器接口.md#ga002ff7ba1f5be374510a902459dd9d3d)。

### `can_set_bitrate`

```c
int can_set_bitrate(const struct device *dev, uint32_t bitrate)
```

设置CAN控制器的比特率。

符号定位：[can_set_bitrate](../hardware/P362_CAN控制器接口.md#ga0685ebfacfb79d33131167ac3aaa6f9b)。

### `can_set_bitrate_data`

```c
int can_set_bitrate_data(const struct device *dev, uint32_t bitrate_data)
```

设置CAN FD控制器数据阶段的比特率。

符号定位：[can_set_bitrate_data](../hardware/P362_CAN控制器接口.md#ga0afd2c446fc5e685370641a1678f87b7)。

### `can_mode_t`

```c
uint32_t can_mode_t
```

提供用于保存CAN控制器配置标志的类型。

定义位置（Definition）：can.h:122。

符号定位：[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

### `can_stats_get_stuff_errors`

```c
uint32_t can_stats_get_stuff_errors(const struct device *dev)
```

取得CAN设备的位填充错误计数器值。

符号定位：[can_stats_get_stuff_errors](../hardware/P362_CAN控制器接口.md#ga162fde4e622fb06dcbbcf2f31bb35d38)。

### `can_stop`

```c
int can_stop(const struct device *dev)
```

停止CAN控制器。

符号定位：[can_stop](../hardware/P362_CAN控制器接口.md#ga1b0ac9185341cb0bde85ec64e4c490a5)。

### `can_set_timing`

```c
int can_set_timing(const struct device *dev, const struct can_timing *timing)
```

配置CAN控制器的总线时序。

符号定位：[can_set_timing](../hardware/P362_CAN控制器接口.md#ga1b134af5d6286ea0fee130b6da5217da)。

### `can_state_change_callback_handler_t`

```c
void(* can_state_change_callback_handler_t)(const struct device *dev, struct can_state_change_callback *callback, enum can_state state, struct can_bus_err_cnt err_cnt)
```

定义状态变化回调处理函数的签名。

定义位置（Definition）：can.h:324。

符号定位：[can_state_change_callback_handler_t](../hardware/P362_CAN控制器接口.md#ga1dc18f69fe06a1d919b13f929100fa85)。

### `can_get_bitrate_max`

```c
uint32_t can_get_bitrate_max(const struct device *dev)
```

取得支持的最高比特率（Maximum Bitrate）。

符号定位：[can_get_bitrate_max](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)。

### `can_stats_get_bit_errors`

```c
uint32_t can_stats_get_bit_errors(const struct device *dev)
```

取得CAN设备的位错误计数器值。

符号定位：[can_stats_get_bit_errors](../hardware/P362_CAN控制器接口.md#ga27b277f3b5146590f159171f602904db)。

### `can_stats_get_crc_errors`

```c
uint32_t can_stats_get_crc_errors(const struct device *dev)
```

取得CAN设备的CRC错误计数器值。

符号定位：[can_stats_get_crc_errors](../hardware/P362_CAN控制器接口.md#ga31692aef7962172532f8200fed7aecd2)。

### `can_get_bitrate_min`

```c
uint32_t can_get_bitrate_min(const struct device *dev)
```

取得支持的最低比特率（Minimum Bitrate）。

符号定位：[can_get_bitrate_min](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)。

### `can_calc_timing_data`

```c
int can_calc_timing_data(const struct device *dev, struct can_timing *res, uint32_t bitrate, uint16_t sample_pnt)
```

计算数据阶段的时序参数。

符号定位：[can_calc_timing_data](../hardware/P362_CAN控制器接口.md#ga358cd73ed59c2099f4b2c6ceb397ca11)。

### `can_send`

```c
int can_send(const struct device *dev, const struct can_frame *frame, k_timeout_t timeout, can_tx_callback_t callback, void *user_data)
```

将CAN帧加入队列，等待在CAN总线上发送。

符号定位：[can_send](../hardware/P362_CAN控制器接口.md#ga446ee31913699de3c80be05d837b5fd5)。

### `can_get_timing_data_max`

```c
const struct can_timing * can_get_timing_data_max(const struct device *dev)
```

取得数据阶段支持的时序参数最大值。

符号定位：[can_get_timing_data_max](../hardware/P362_CAN控制器接口.md#ga47a2f6d6b42121b390aa92160c833b80)。

### `can_get_core_clock`

```c
int can_get_core_clock(const struct device *dev, uint32_t *rate)
```

取得CAN核心时钟频率。

符号定位：[can_get_core_clock](../hardware/P362_CAN控制器接口.md#ga4af6d0d9ab72b195909f511ac65cb8fa)。

### `can_get_capabilities`

```c
int can_get_capabilities(const struct device *dev, can_mode_t *cap)
```

取得CAN控制器支持的模式。

符号定位：[can_get_capabilities](../hardware/P362_CAN控制器接口.md#ga4afd7776c5039dec8acb089499dc1168)。

### `can_stats_get_bit1_errors`

```c
uint32_t can_stats_get_bit1_errors(const struct device *dev)
```

取得CAN设备的位1错误计数器值。

符号定位：[can_stats_get_bit1_errors](../hardware/P362_CAN控制器接口.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)。

### `can_stats_get_ack_errors`

```c
uint32_t can_stats_get_ack_errors(const struct device *dev)
```

取得CAN设备的应答错误计数器值。

符号定位：[can_stats_get_ack_errors](../hardware/P362_CAN控制器接口.md#ga4f8414d64b75d4d1ffb7a0feff36f698)。

### `can_get_max_filters`

```c
int can_get_max_filters(const struct device *dev, bool ide)
```

取得接收过滤器的最大数量。

符号定位：[can_get_max_filters](../hardware/P362_CAN控制器接口.md#ga526c08539094486f07dc52aad8ed0dcc)。

### `can_get_timing_min`

```c
const struct can_timing * can_get_timing_min(const struct device *dev)
```

取得支持的时序参数最小值。

符号定位：[can_get_timing_min](../hardware/P362_CAN控制器接口.md#ga5a57627de4764f0bd3b4bafe07f56e6f)。

### `can_remove_state_change_callback`

```c
int can_remove_state_change_callback(const struct device *dev, struct can_state_change_callback *callback)
```

移除CAN控制器状态变化事件的回调。

符号定位：[can_remove_state_change_callback](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)。

### `can_set_timing_data`

```c
int can_set_timing_data(const struct device *dev, const struct can_timing *timing_data)
```

配置CAN FD控制器数据阶段的总线时序。

符号定位：[can_set_timing_data](../hardware/P362_CAN控制器接口.md#ga606cf9fda4c66a0f4abf74e1d357eac2)。

### `can_get_timing_data_min`

```c
const struct can_timing * can_get_timing_data_min(const struct device *dev)
```

取得数据阶段（Data Phase）支持的时序参数最小值。

符号定位：[can_get_timing_data_min](../hardware/P362_CAN控制器接口.md#ga6399ef0cefdab3da738136f8a5c59c2f)。

### `can_stats_get_bit0_errors`

```c
uint32_t can_stats_get_bit0_errors(const struct device *dev)
```

取得CAN设备的位0错误计数器值。

符号定位：[can_stats_get_bit0_errors](../hardware/P362_CAN控制器接口.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)。

### `can_remove_rx_filter`

```c
void can_remove_rx_filter(const struct device *dev, int filter_id)
```

移除CAN接收过滤器。

符号定位：[can_remove_rx_filter](../hardware/P362_CAN控制器接口.md#ga822aa3142ea01582d5cfb8b478fb2847)。

### `can_bytes_to_dlc`

```c
static uint8_t can_bytes_to_dlc(uint8_t num_bytes)
```

将字节数转换为数据长度码（DLC）。

定义位置（Definition）：can.h:1870。

符号定位：[can_bytes_to_dlc](../hardware/P362_CAN控制器接口.md#ga8314716fe2b66d567b3fd377b8ee9dc3)。

### `can_stats_get_rx_overruns`

```c
uint32_t can_stats_get_rx_overruns(const struct device *dev)
```

取得CAN设备的接收溢出计数器值。

符号定位：[can_stats_get_rx_overruns](../hardware/P362_CAN控制器接口.md#ga8664fbaa13f4bb89540493264d2a041d)。

### `CAN_FRAME_IDE`

```c
#define CAN_FRAME_IDE
```

帧使用扩展29位CAN ID。

定义位置（Definition）：can.h:148。

符号定位：[CAN_FRAME_IDE](../hardware/P362_CAN控制器接口.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)。

### `can_dlc_to_bytes`

```c
static uint8_t can_dlc_to_bytes(uint8_t dlc)
```

将数据长度码（DLC）转换为数据字节数。

定义位置（Definition）：can.h:1855。

符号定位：[can_dlc_to_bytes](../hardware/P362_CAN控制器接口.md#gaa1d866167c0c23f8d5c0c15385589601)。

### `can_add_rx_filter_msgq`

```c
int can_add_rx_filter_msgq(const struct device *dev, struct k_msgq *msgq, const struct can_filter *filter)
```

为指定过滤器添加消息队列的简易包装函数（Wrapper）。

符号定位：[can_add_rx_filter_msgq](../hardware/P362_CAN控制器接口.md#gaaac20a068b7f32d2f38d1601d588b35c)。

### `can_rx_callback_t`

```c
void(* can_rx_callback_t)(const struct device *dev, struct can_frame *frame, void *user_data)
```

定义接收用应用程序回调处理函数的签名。

定义位置（Definition）：can.h:298。

符号定位：[can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)。

### `can_frame_matches_filter`

```c
static bool can_frame_matches_filter(const struct can_frame *frame, const struct can_filter *filter)
```

检查CAN帧是否匹配CAN过滤器。

定义位置（Definition）：can.h:1889。

符号定位：[can_frame_matches_filter](../hardware/P362_CAN控制器接口.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)。

### `can_tx_callback_t`

```c
void(* can_tx_callback_t)(const struct device *dev, int error, void *user_data)
```

定义应用程序回调处理函数的签名（Callback Handler Signature）。

定义位置（Definition）：can.h:289。

符号定位：[can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)。

### `can_get_state`

```c
int can_get_state(const struct device *dev, enum can_state *state, struct can_bus_err_cnt *err_cnt)
```

取得CAN控制器的当前状态。

符号定位：[can_get_state](../hardware/P362_CAN控制器接口.md#gab98c121578c8349d9dfb41d60f356857)。

### `can_get_mode`

```c
can_mode_t can_get_mode(const struct device *dev)
```

取得CAN控制器的工作模式。

符号定位：[can_get_mode](../hardware/P362_CAN控制器接口.md#gabd201b5b1fca54048985a8a24dd51e55)。

### `can_get_timing_max`

```c
const struct can_timing * can_get_timing_max(const struct device *dev)
```

取得支持的时序参数最大值。

符号定位：[can_get_timing_max](../hardware/P362_CAN控制器接口.md#gabe385d0f003b1e990c78ef7a2a3f9616)。

### `can_init_state_change_callback`

```c
static void can_init_state_change_callback(struct can_state_change_callback *callback, can_state_change_callback_handler_t handler)
```

初始化CAN控制器状态变化回调结构。

定义位置（Definition）：can.h:1624。

符号定位：[can_init_state_change_callback](../hardware/P362_CAN控制器接口.md#gabf813d9f21982f674b213708adee9e96)。

### `can_stats_get_form_errors`

```c
uint32_t can_stats_get_form_errors(const struct device *dev)
```

取得CAN设备的格式错误计数器值。

符号定位：[can_stats_get_form_errors](../hardware/P362_CAN控制器接口.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)。

### `can_calc_timing`

```c
int can_calc_timing(const struct device *dev, struct can_timing *res, uint32_t bitrate, uint16_t sample_pnt)
```

根据比特率和采样点（Sample Point）计算时序参数。

符号定位：[can_calc_timing](../hardware/P362_CAN控制器接口.md#gac27fe64142603f0d32d422594356b2d7)。

### `can_recover`

```c
int can_recover(const struct device *dev, k_timeout_t timeout)
```

从总线关闭状态恢复。

符号定位：[can_recover](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e)。

### `can_state`

```c
can_state
```

定义CAN控制器的状态（State）。

定义位置（Definition）：can.h:127。

符号定位：[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)。

### `can_set_state_change_callback`

```c
void can_set_state_change_callback(const struct device *dev, can_state_change_callback_t callback, void *user_data)
```

设置CAN控制器状态变化事件的回调。

符号定位：[can_set_state_change_callback](../hardware/P362_CAN控制器接口.md#gacda2bc21fa0cbd7b3406dd096827923c)。

### `can_add_state_change_callback`

```c
int can_add_state_change_callback(const struct device *dev, struct can_state_change_callback *callback)
```

添加CAN控制器状态变化事件的回调。

符号定位：[can_add_state_change_callback](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)。

### `can_get_transceiver`

```c
const struct device * can_get_transceiver(const struct device *dev)
```

取得与CAN控制器关联的CAN收发器（Transceiver）。

符号定位：[can_get_transceiver](../hardware/P362_CAN控制器接口.md#gae012d26711c2a7ce1419d21c38cae63a)。

### `can_set_mode`

```c
int can_set_mode(const struct device *dev, can_mode_t mode)
```

将CAN控制器设置为指定工作模式（Operation Mode）。

符号定位：[can_set_mode](../hardware/P362_CAN控制器接口.md#gae04c3c884b3ed26dfea4745b7dff2c5f)。

### `can_start`

```c
int can_start(const struct device *dev)
```

启动CAN控制器。

符号定位：[can_start](../hardware/P362_CAN控制器接口.md#gae48dfa8bc5b52f233b9b1a08aac2675a)。

### `can_add_rx_filter`

```c
int can_add_rx_filter(const struct device *dev, can_rx_callback_t callback, void *user_data, const struct can_filter *filter)
```

为指定CAN过滤器添加回调函数。

符号定位：[can_add_rx_filter](../hardware/P362_CAN控制器接口.md#gae9dd69a13b960f773ab07bb0bb13b5e9)。

### `CAN_FILTER_IDE`

```c
#define CAN_FILTER_IDE
```

过滤器匹配使用扩展29位CAN ID的帧。

定义位置（Definition）：can.h:208。

符号定位：[CAN_FILTER_IDE](../hardware/P362_CAN控制器接口.md#gafa40c165d016955ec0c856a7fd53168f)。

### `CAN_STATE_ERROR_ACTIVE`

```c
@ CAN_STATE_ERROR_ACTIVE
```

错误主动状态（Error-active），RX／TX错误计数小于96。

定义位置（Definition）：can.h:129。

符号定位：[CAN_STATE_ERROR_ACTIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)。

### `CAN_STATE_ERROR_WARNING`

```c
@ CAN_STATE_ERROR_WARNING
```

错误警告状态（Error-warning），RX／TX错误计数小于128。

定义位置（Definition）：can.h:131。

符号定位：[CAN_STATE_ERROR_WARNING](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)。

### `CAN_STATE_STOPPED`

```c
@ CAN_STATE_STOPPED
```

CAN控制器已停止，不参与CAN通信。

定义位置（Definition）：can.h:137。

符号定位：[CAN_STATE_STOPPED](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)。

### `CAN_STATE_BUS_OFF`

```c
@ CAN_STATE_BUS_OFF
```

总线关闭状态（Bus-off），RX／TX错误计数大于或等于256。

定义位置（Definition）：can.h:135。

符号定位：[CAN_STATE_BUS_OFF](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)。

### `CAN_STATE_ERROR_PASSIVE`

```c
@ CAN_STATE_ERROR_PASSIVE
```

错误被动状态（Error-passive），RX／TX错误计数小于256。

定义位置（Definition）：can.h:133。

符号定位：[CAN_STATE_ERROR_PASSIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)。

### `sys_slist_t`

```c
struct _slist sys_slist_t
```

单向链表（Singly Linked List）结构。

定义位置（Definition）：slist.h:54。

符号定位：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)。

### `sys_snode_t`

```c
struct _snode sys_snode_t
```

单向链表节点（Singly Linked List Node）结构。

定义位置（Definition）：slist.h:44。

符号定位：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)。

### `STATS_SECT_END`

```c
#define STATS_SECT_END
```

结束统计组结构定义。

定义位置（Definition）：stats.h:169。

符号定位：[STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)。

### `STATS_NAME`

```c
#define STATS_NAME(sectname__, entry__)
```

向统计条目名称映射添加一个条目名称。

定义位置（Definition）：stats.h:519。

符号定位：[STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)。

### `STATS_SECT_ENTRY32`

```c
#define STATS_SECT_ENTRY32(var__)
```

在统计组结构内声明一个32位统计条目。

定义位置（Definition）：stats.h:204。

符号定位：[STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)。

### `STATS_NAME_START`

```c
#define STATS_NAME_START(sectname__)
```

开始统计条目名称映射。

定义位置（Definition）：stats.h:510。

符号定位：[STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)。

### `STATS_NAME_END`

```c
#define STATS_NAME_END(sectname__)
```

结束统计条目名称映射。

定义位置（Definition）：stats.h:527。

符号定位：[STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)。

### `STATS_SECT_START`

```c
#define STATS_SECT_START(group__)
```

开始统计组结构定义。

定义位置（Definition）：stats.h:181。

符号定位：[STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)。

### `MIN`

```c
#define MIN(a, b)
```

取得两个值中的较小值。

定义位置（Definition）：util.h:406。

符号定位：[MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)。

### `ARRAY_SIZE`

```c
#define ARRAY_SIZE(array)
```

给定数组中的元素数量。

定义位置（Definition）：util.h:118。

符号定位：[ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)。

### `DIV_ROUND_UP`

```c
#define DIV_ROUND_UP(n, d)
```

相除并向上取整（Round Up）。

定义位置（Definition）：util.h:348。

符号定位：[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)。

### `ENOSYS`

```c
#define ENOSYS
```

功能未实现（Function Not Implemented）。

定义位置（Definition）：errno.h:83。

符号定位：[ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `kernel.h`

公共内核API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `state`

```c
state
```

定义位置（Definition）：parser_state.h:29。

符号定位：[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

### `stats.h`

统计信息（Statistics）。

符号定位：[stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `string.h`

符号定位：[string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。

### `can_bus_err_cnt`

CAN控制器错误计数器（Error Counters）。

定义位置（Definition）：can.h:229。

符号定位：[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

### `can_bus_err_cnt::tx_err_cnt`

```c
uint8_t tx_err_cnt
```

CAN控制器发送错误计数器的值。

定义位置（Definition）：can.h:231。

符号定位：[can_bus_err_cnt::tx_err_cnt](../hardware/P365_CAN错误计数结构.md#a01bb2cb16656d0fd4f99cfbfa1f30e98)。

### `can_bus_err_cnt::rx_err_cnt`

```c
uint8_t rx_err_cnt
```

CAN控制器接收错误计数器的值。

定义位置（Definition）：can.h:233。

符号定位：[can_bus_err_cnt::rx_err_cnt](../hardware/P365_CAN错误计数结构.md#a6be6ce6b592641ba0dce36fe1cd8902a)。

### `can_device_state`

CAN专用设备状态，允许加入CAN设备类别专用的扩展内容。

定义位置（Definition）：can.h:682。

符号定位：[can_device_state](../hardware/P368_CAN设备状态结构.md)。

### `can_device_state::devstate`

```c
struct device_state devstate
```

公共设备状态（Common Device State）。

定义位置（Definition）：can.h:684。

符号定位：[can_device_state::devstate](../hardware/P368_CAN设备状态结构.md#a28061ff1193176dd01b7bb9a88f402ec)。

### `can_device_state::stats`

```c
struct stats_can stats
```

CAN设备统计信息（Statistics）。

定义位置（Definition）：can.h:686。

符号定位：[can_device_state::stats](../hardware/P368_CAN设备状态结构.md#ae05c85eae4f6bee075ffdc4f0ab56f47)。

### `can_driver_api`

驱动操作（Driver Operations）：CAN控制器驱动操作；原提示含有格式标签。

定义位置（Definition）：can.h:566。

符号定位：[can_driver_api](../hardware/P370_CAN驱动函数表.md)。

### `can_driver_api::get_capabilities`

```c
can_get_capabilities_t get_capabilities
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:570。

符号定位：[can_driver_api::get_capabilities](../hardware/P370_CAN驱动函数表.md#a11d2ff416d459faf84905e7ffdc1a536)。

### `can_driver_api::set_timing_data`

```c
can_set_timing_data_t set_timing_data
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:631。

符号定位：[can_driver_api::set_timing_data](../hardware/P370_CAN驱动函数表.md#a1951bfc3135824e364d5f18aa9b15d09)。

### `can_driver_api::get_max_filters`

```c
can_get_max_filters_t get_max_filters
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:621。

符号定位：[can_driver_api::get_max_filters](../hardware/P370_CAN驱动函数表.md#a24a90bc4d49818985479bfe101cc21d4)。

### `can_driver_api::set_timing`

```c
can_set_timing_t set_timing
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:586。

符号定位：[can_driver_api::set_timing](../hardware/P370_CAN驱动函数表.md#a356b3761926c2a5a85fcc80b2e8a4643)。

### `can_driver_api::stop`

```c
can_stop_t stop
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:578。

符号定位：[can_driver_api::stop](../hardware/P370_CAN驱动函数表.md#a3ca1cb8bcd6713bfdf20f76cee3bc3a4)。

### `can_driver_api::add_rx_filter`

```c
can_add_rx_filter_t add_rx_filter
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:594。

符号定位：[can_driver_api::add_rx_filter](../hardware/P370_CAN驱动函数表.md#a56225a8cb458baa0d1745ff5e9202ae6)。

### `can_driver_api::timing_data_min`

```c
struct can_timing timing_data_min
```

数据阶段时序寄存器的最小值。

定义位置（Definition）：can.h:635。

符号定位：[can_driver_api::timing_data_min](../hardware/P370_CAN驱动函数表.md#a5ad424b27606f9de8f37524594d396dc)。

### `can_driver_api::state_change_callbacks_enabled`

```c
can_state_change_callbacks_enabled_t state_change_callbacks_enabled
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:613。

符号定位：[can_driver_api::state_change_callbacks_enabled](../hardware/P370_CAN驱动函数表.md#a90547b28015e2b7eea6a548b0ab2b576)。

### `can_driver_api::timing_max`

```c
struct can_timing timing_max
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:625。

符号定位：[can_driver_api::timing_max](../hardware/P370_CAN驱动函数表.md#a90dca9dd3baef96c4d3849be367129b5)。

### `can_driver_api::send`

```c
can_send_t send
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:590。

符号定位：[can_driver_api::send](../hardware/P370_CAN驱动函数表.md#a9b5ec5c71a126798c24a19d1c91f879b)。

### `can_driver_api::get_state`

```c
can_get_state_t get_state
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:609。

符号定位：[can_driver_api::get_state](../hardware/P370_CAN驱动函数表.md#aa6b8b2b7c544cf78930b45cab1e6dbb4)。

### `can_driver_api::recover`

```c
can_recover_t recover
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:604。

符号定位：[can_driver_api::recover](../hardware/P370_CAN驱动函数表.md#aba563aff4e114b7956bb824efdebb0c6)。

### `can_driver_api::timing_data_max`

```c
struct can_timing timing_data_max
```

数据阶段时序寄存器的最大值。

定义位置（Definition）：can.h:639。

符号定位：[can_driver_api::timing_data_max](../hardware/P370_CAN驱动函数表.md#ac07eeec7b96543b19041a28d70e19a97)。

### `can_driver_api::remove_rx_filter`

```c
can_remove_rx_filter_t remove_rx_filter
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:598。

符号定位：[can_driver_api::remove_rx_filter](../hardware/P370_CAN驱动函数表.md#ac264f4d66a29a5f42aaf2b6c9665f8f3)。

### `can_driver_api::start`

```c
can_start_t start
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:574。

符号定位：[can_driver_api::start](../hardware/P370_CAN驱动函数表.md#ac42f6d438d3e88f0db8e64c236621f8a)。

### `can_driver_api::set_mode`

```c
can_set_mode_t set_mode
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:582。

符号定位：[can_driver_api::set_mode](../hardware/P370_CAN驱动函数表.md#accfe8e3e40e5bae33b8c31b1af55c644)。

### `can_driver_api::get_core_clock`

```c
can_get_core_clock_t get_core_clock
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:617。

符号定位：[can_driver_api::get_core_clock](../hardware/P370_CAN驱动函数表.md#ae969c18839dc5f1cb4356df6d1ee1e20)。

### `can_driver_api::timing_min`

```c
struct can_timing timing_min
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：can.h:623。

符号定位：[can_driver_api::timing_min](../hardware/P370_CAN驱动函数表.md#aeaa8022843f787bddbb18aa407d340a5)。

### `can_driver_config`

CAN控制器驱动的公共配置（Common Configuration）。

定义位置（Definition）：can.h:377。

符号定位：[can_driver_config](../hardware/P371_CAN驱动公共配置.md)。

### `can_driver_config::sample_point`

```c
uint16_t sample_point
```

经典CAN／CAN FD仲裁阶段（Arbitration Phase）的初始采样点，单位为千分比（Permille）。

定义位置（Definition）：can.h:387。

符号定位：[can_driver_config::sample_point](../hardware/P371_CAN驱动公共配置.md#a2cd7693cd9acc0537a085cdc85688a96)。

### `can_driver_config::max_bitrate`

```c
uint32_t max_bitrate
```

CAN控制器与收发器组合支持的最高比特率。

定义位置（Definition）：can.h:383。

符号定位：[can_driver_config::max_bitrate](../hardware/P371_CAN驱动公共配置.md#a420d9f8762ae332d4d78084dd74afa6e)。

### `can_driver_config::bitrate`

```c
uint32_t bitrate
```

经典CAN／CAN FD仲裁阶段的初始比特率。

定义位置（Definition）：can.h:385。

符号定位：[can_driver_config::bitrate](../hardware/P371_CAN驱动公共配置.md#a6f4f050b5aeb8cd466a12d70c53e8423)。

### `can_driver_config::phy`

```c
const struct device * phy
```

指向关联CAN收发器设备结构的指针，或者NULL。

定义位置（Definition）：can.h:379。

符号定位：[can_driver_config::phy](../hardware/P371_CAN驱动公共配置.md#a8e9f0ec132daf25a2e947478c0b952a3)。

### `can_driver_config::min_bitrate`

```c
uint32_t min_bitrate
```

CAN控制器与收发器组合支持的最低比特率。

定义位置（Definition）：can.h:381。

符号定位：[can_driver_config::min_bitrate](../hardware/P371_CAN驱动公共配置.md#accc9f1b6202b2b30b60bbc890190d3c3)。

### `can_driver_config::sample_point_data`

```c
uint16_t sample_point_data
```

CAN FD数据阶段的初始采样点，单位为千分比。

定义位置（Definition）：can.h:390。

符号定位：[can_driver_config::sample_point_data](../hardware/P371_CAN驱动公共配置.md#afa6cd8cb79ccad28ca86caec4d92cd85)。

### `can_driver_config::bitrate_data`

```c
uint32_t bitrate_data
```

CAN FD数据阶段的初始比特率。

定义位置（Definition）：can.h:392。

符号定位：[can_driver_config::bitrate_data](../hardware/P371_CAN驱动公共配置.md#afd7a831b33b059f47dd867726e31e69b)。

### `can_driver_data`

CAN控制器驱动的公共数据（Common Data）。

定义位置（Definition）：can.h:433。

符号定位：[can_driver_data](../hardware/P372_CAN驱动公共数据.md)。

### `can_driver_data::mode`

```c
can_mode_t mode
```

CAN控制器的当前模式。

定义位置（Definition）：can.h:435。

符号定位：[can_driver_data::mode](../hardware/P372_CAN驱动公共数据.md#a1f01de3a78be9193263a47acf4181b93)。

### `can_driver_data::legacy_state_change_cb`

```c
struct can_state_change_callback legacy_state_change_cb
```

旧式状态变化回调（Legacy State Change Callback）。

定义位置（Definition）：can.h:439。

符号定位：[can_driver_data::legacy_state_change_cb](../hardware/P372_CAN驱动公共数据.md#a281054c5102f22c362691b81efbb8162)。

### `can_driver_data::started`

```c
bool started
```

CAN控制器已启动时为true，否则为false。

定义位置（Definition）：can.h:437。

符号定位：[can_driver_data::started](../hardware/P372_CAN驱动公共数据.md#a5b3983ca54213c84f8278ec36f0fb0ce)。

### `can_driver_data::state_change_callback_lock`

```c
struct k_spinlock state_change_callback_lock
```

修改状态变化回调列表所用的锁（Lock）。

定义位置（Definition）：can.h:445。

符号定位：[can_driver_data::state_change_callback_lock](../hardware/P372_CAN驱动公共数据.md#a5b8a964383a759a0144a1b72bb8835cc)。

### `can_driver_data::legacy_state_change_cb_user_data`

```c
void * legacy_state_change_cb_user_data
```

旧式状态变化回调的用户数据指针，或者NULL。

定义位置（Definition）：can.h:443。

符号定位：[can_driver_data::legacy_state_change_cb_user_data](../hardware/P372_CAN驱动公共数据.md#a646e5422136017bed629e5a0f80d4824)。

### `can_driver_data::legacy_state_change_cb_handler`

```c
can_state_change_callback_t legacy_state_change_cb_handler
```

旧式状态变化回调函数指针，或者NULL。

定义位置（Definition）：can.h:441。

符号定位：[can_driver_data::legacy_state_change_cb_handler](../hardware/P372_CAN驱动公共数据.md#af6a94bfe3b21502dc70548b470f732b4)。

### `can_driver_data::state_change_callbacks`

```c
sys_slist_t state_change_callbacks
```

状态变化回调列表。

定义位置（Definition）：can.h:447。

符号定位：[can_driver_data::state_change_callbacks](../hardware/P372_CAN驱动公共数据.md#afce7bbd484eea2660fe71f0322103265)。

### `can_filter`

CAN过滤器（Filter）结构。

定义位置（Definition）：can.h:215。

符号定位：[can_filter](../hardware/P364_CAN过滤器结构.md)。

### `can_filter::mask`

```c
uint32_t mask
```

CAN标识符匹配掩码（Matching Mask）。

定义位置（Definition）：can.h:221。

符号定位：[can_filter::mask](../hardware/P364_CAN过滤器结构.md#a15632117f3f031fbbeb28ef562f9ac94)。

### `can_filter::flags`

```c
uint8_t flags
```

标志（Flags）。

定义位置（Definition）：can.h:223。

符号定位：[can_filter::flags](../hardware/P364_CAN过滤器结构.md#a7616e21f33be5fb43094d44530a1c5de)。

### `can_filter::id`

```c
uint32_t id
```

要匹配的CAN标识符。

定义位置（Definition）：can.h:217。

符号定位：[can_filter::id](../hardware/P364_CAN过滤器结构.md#adf2b18eab11d360780707478a1f624b9)。

### `can_frame`

CAN帧（Frame）结构。

定义位置（Definition）：can.h:169。

符号定位：[can_frame](../hardware/P363_CAN帧结构.md)。

### `can_frame::dlc`

```c
uint8_t dlc
```

指示数据字节长度的数据长度码（Data Length Code，DLC）。

定义位置（Definition）：can.h:173。

符号定位：[can_frame::dlc](../hardware/P363_CAN帧结构.md#a014c42277e886906e6c761bc6f21fb47)。

### `can_frame::flags`

```c
uint8_t flags
```

标志（Flags）。

定义位置（Definition）：can.h:175。

符号定位：[can_frame::flags](../hardware/P363_CAN帧结构.md#a1e71125342a01a6e5a68a14cb075ce7c)。

### `can_frame::id`

```c
uint32_t id
```

标准11位或扩展29位CAN标识符。

定义位置（Definition）：can.h:171。

符号定位：[can_frame::id](../hardware/P363_CAN帧结构.md#a7ad0d8d62322affafbfd23839ee81d5d)。

### `can_frame::data`

```c
uint8_t data[CAN_MAX_DLEN]
```

按无符号8位值访问的有效载荷数据（Payload Data）。

定义位置（Definition）：can.h:194。

符号定位：[can_frame::data](../hardware/P363_CAN帧结构.md#ac4b43443b2a338d35f0e1d3ef8355960)。

### `can_frame::data_32`

```c
uint32_t data_32[DIV_ROUND_UP(CAN_MAX_DLEN, sizeof(uint32_t))]
```

按无符号32位值访问的有效载荷数据。

定义位置（Definition）：can.h:196。

符号定位：[can_frame::data_32](../hardware/P363_CAN帧结构.md#ad88af93a2171e4c9d617b91b403d842a)。

### `can_frame::timestamp`

```c
uint16_t timestamp
```

接收此帧时捕获的CAN控制器自由运行定时器（Free-running Timer）值。

定义位置（Definition）：can.h:184。

符号定位：[can_frame::timestamp](../hardware/P363_CAN帧结构.md#ae46f8b0821c638517959274bbbda5932)。

### `can_state_change_callback`

CAN状态变化回调（State Change Callback）。

定义位置（Definition）：can.h:342。

符号定位：[can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)。

### `can_state_change_callback::node`

```c
sys_snode_t node
```

单向链表节点。

定义位置（Definition）：can.h:344。

符号定位：[can_state_change_callback::node](../hardware/P367_CAN状态变化回调结构.md#a20e10ceff66aefd6e77340687cab3f40)。

### `can_state_change_callback::handler`

```c
can_state_change_callback_handler_t handler
```

回调函数（Callback Function）。

定义位置（Definition）：can.h:346。

符号定位：[can_state_change_callback::handler](../hardware/P367_CAN状态变化回调结构.md#a3bf66a334174307bde9c0fe12939a503)。

### `can_timing`

CAN总线时序（Bus Timing）结构。

定义位置（Definition）：can.h:268。

符号定位：[can_timing](../hardware/P366_CAN时序结构.md)。

### `can_timing::sjw`

```c
uint16_t sjw
```

同步跳转宽度（Synchronization Jump Width，SJW）。

定义位置（Definition）：can.h:270。

符号定位：[can_timing::sjw](../hardware/P366_CAN时序结构.md#a5af76a4ee9c741642ec19265a47fceb5)。

### `can_timing::phase_seg2`

```c
uint16_t phase_seg2
```

相位段2（Phase Segment 2）。

定义位置（Definition）：can.h:276。

符号定位：[can_timing::phase_seg2](../hardware/P366_CAN时序结构.md#a6ca0caf618d28a761c3c8859ed3a68d6)。

### `can_timing::prescaler`

```c
uint16_t prescaler
```

预分频器值（Prescaler Value）。

定义位置（Definition）：can.h:278。

符号定位：[can_timing::prescaler](../hardware/P366_CAN时序结构.md#a74fb8341cbb6d97721c9d0afbc7e1f3a)。

### `can_timing::phase_seg1`

```c
uint16_t phase_seg1
```

相位段1（Phase Segment 1）。

定义位置（Definition）：can.h:274。

符号定位：[can_timing::phase_seg1](../hardware/P366_CAN时序结构.md#a9941688e79fa4ce01c4b498433319089)。

### `can_timing::prop_seg`

```c
uint16_t prop_seg
```

传播段（Propagation Segment）。

定义位置（Definition）：can.h:272。

符号定位：[can_timing::prop_seg](../hardware/P366_CAN时序结构.md#ac009d40fee9788b663963978498b2ee9)。

### `device_state`

每个驱动实例的运行时设备动态结构，位于随机存取存储器（RAM）中。

定义位置（Definition）：device.h:488。

符号定位：[device_state](../device_reference/P003_设备运行状态结构.md)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `device::data`

```c
void * data
```

设备实例私有数据的地址。

定义位置（Definition）：device.h:553。

符号定位：[device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)。

### `device::config`

```c
const void * config
```

设备实例配置信息的地址。

定义位置（Definition）：device.h:547。

符号定位：[device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)。

### `k_msgq`

消息队列结构（Message Queue Structure）。

定义位置（Definition）：kernel.h:5257。

符号定位：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

### `k_spinlock`

内核自旋锁（Kernel Spin Lock）。

定义位置（Definition）：spinlock.h:45。

符号定位：[k_spinlock](../kernel/P066_自旋锁结构参考.md)。

### `k_timeout_t`

内核超时类型（Kernel Timeout Type）。

定义位置（Definition）：clock.h:65。

符号定位：[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

## 2.4\_源码跟踪译注

> 译注——控制器与收发器：CAN控制器（Controller）管理帧、仲裁和位时序，收发器（Transceiver）是单独的关联设备。can_get_transceiver读取公共配置中的phy，可能返回NULL；这不是总线连通性探测。CAN_DT_DRIVER_CONFIG_GET组合控制器／收发器比特率边界，并读取初始比特率与采样点；can_get_mode读取公共运行数据中的mode，不是重新测量总线状态。具体启动、停止和模式设置交给驱动操作。当前数据阶段时序最小／最大值查询直接返回驱动函数表内对应字段的地址，没有单独检查FD能力；不能仅以返回指针非空推断设备支持CAN FD。

> 译注——DLC与载荷长度：CAN_MAX_DLC为8，CANFD_MAX_DLC为15；CONFIG_CAN_FD_MODE控制can_frame内载荷数组为8或64字节，不等于每帧都采用FD格式。can_dlc_to_bytes把DLC 9至15映射为12、16、20、24、32、48、64字节，大于15的输入被钳位到末项。can_bytes_to_dlc向上选择可容纳长度的编码，大于48的输入均返回15；两者都不是帧合法性检查。回传统计中的dlc“指示字节长度”不应理解为dlc字段恒等于字节数。

> 译注——过滤匹配范围：can_frame_matches_filter先要求标准／扩展标识符类型相同，再计算(frame.id XOR filter.id) AND filter.mask；结果为0才匹配。掩码位为0表示不比较该位；此辅助函数不检查RTR、FDF、BRS或ESI，也不表示安装过滤器后的硬件资源一定可用。CAN_MODE_*、CAN_FRAME_*与CAN_FILTER_*属于不同对象，数值位相同不能互换语义。

> 译注——发送等待边界：can_send的timeout用于等待空闲发送邮箱（TX Mailbox）。callback为空时，公共实现安装内部完成回调；驱动接受发送后以K_FOREVER等待信号量，再返回完成状态，因此该timeout不是整个同步发送的截止时间。提供回调时，公共包装把回调和用户数据转交驱动。用户态系统调用复制帧结构并要求callback为NULL，不能据此认为用户态可以安装同样的发送完成回调。

> 译注——接收消息队列：can_add_rx_filter_msgq要求消息大小等于sizeof(struct can_frame)，回调以K_NO_WAIT复制整帧到队列。队列满时记录溢出错误，不能承诺保留该帧或自动等待空间。CAN_MSGQ_DEFINE负责静态创建匹配元素类型的队列；队列容量、过滤器数量和硬件接收容量是不同限制。消息队列包装直接调用驱动add_rx_filter，并未复用普通can_add_rx_filter入口的全部参数检查。

> 译注——参数检查的配置：公共发送与普通过滤器安装中的若干校验使用CHECKIF。默认运行时检查展开为条件判断并可返回-EINVAL；CONFIG_ASSERT_ON_ERRORS改为断言且不执行所包围的错误处理块；CONFIG_NO_RUNTIME_CHECKS在编译时省略检查。因此这些参数约束始终应由调用者满足，不能假定任意构建都会返回相同的错误码。系统调用的对象与内存访问校验是另一层边界。

> 译注——时序计算：sample_pnt以千分比表示，875对应87.5%；值0根据比特率选择默认采样点：大于800 kbit/s用750，大于500 kbit/s用800，其余用875。计算器寻找核心时钟可整除的预分频与时间量子组合；成功可能返回正的采样点误差，不应把所有非零值当失败。当前经典／仲裁阶段计算上限为1 Mbit/s，数据阶段为8 Mbit/s，这些上限不代表某个驱动或收发器一定支持。失败后不要使用输出时序。

> 译注——应用时序与补偿：can_set_bitrate及数据阶段版本还检查控制器／收发器的最低与最高比特率，计算误差超过CONFIG_CAN_SAMPLE_POINT_MARGIN时返回-ERANGE。can_set_timing检查各字段上下限，并要求sjw不大于phase_seg1和phase_seg2，再委托驱动。CAN_CALC_TDCO按(1 + prop_seg + phase_seg1)乘prescaler计算并钳位到传入边界；宏本身不验证完整时序是否适用。计算、写入时序与启动总线分别是不同动作。

> 译注——状态回调与锁：新接口用can_state_change_callback节点维护回调列表，init仅设置handler，add才加入列表。当前触发函数持有state_change_callback_lock自旋锁时依次调用handler；处理函数不能阻塞，也不能重入需要取得同一锁的增删操作。添加已有节点会先移除再追加；首次启用通知或最后禁用通知的驱动钩子即使返回错误，已经执行的链表修改也不会回滚。旧式单回调接口通过内部节点适配，且忽略增删接口的返回值。

> 译注——状态与统计：原状态提示使用RX／TX错误计数阈值作简写，这里保留其文字；实际状态由驱动get_state或状态事件报告，can_bus_err_cnt的两个字段仅为uint8_t，不能靠它们表达256并自行替代总线关闭判断。CAN_STATS_*维护独立的32位软件统计，不是这两个硬件错误计数器；bit0／bit1递增宏同时增加总bit_error，未启用统计时递增与清零宏为空。手动恢复还受CONFIG_CAN_MANUAL_RECOVERY_MODE和驱动recover操作支持情况约束。

> 译注——版本边界：本批核对控制器与收发器头文件、CAN公共实现、系统调用处理、Kconfig、GPIO收发器实现、经典CAN与CAN FD绑定以及CHECKIF定义，共九份官方源码并记录摘要。两份源码页的非注释代码分别与读取的官方头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接CAN总线、发送帧或操作硬件。

头文件相对定位：[include/zephyr/drivers/can.h](../../../include/zephyr/drivers/can.h)，关联实现／接口：[drivers/can/can_common.c](../../../drivers/can/can_common.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/can.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_common.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、连接CAN总线、收发帧或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_CAN驱动头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)
- [CAN_STATE_ERROR_ACTIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)
- [CAN_STATE_ERROR_WARNING](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)
- [CAN_STATE_ERROR_PASSIVE](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)
- [CAN_STATE_BUS_OFF](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)
- [CAN_STATE_STOPPED](../hardware/P362_CAN控制器接口.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [id](../hardware/P363_CAN帧结构.md#a7ad0d8d62322affafbfd23839ee81d5d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [dlc](../hardware/P363_CAN帧结构.md#a014c42277e886906e6c761bc6f21fb47)
- [flags](../hardware/P363_CAN帧结构.md#a1e71125342a01a6e5a68a14cb075ce7c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [timestamp](../hardware/P363_CAN帧结构.md#ae46f8b0821c638517959274bbbda5932)
- [data](../hardware/P363_CAN帧结构.md#ac4b43443b2a338d35f0e1d3ef8355960)
- [data_32](../hardware/P363_CAN帧结构.md#ad88af93a2171e4c9d617b91b403d842a)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [id](../hardware/P364_CAN过滤器结构.md#adf2b18eab11d360780707478a1f624b9)
- [mask](../hardware/P364_CAN过滤器结构.md#a15632117f3f031fbbeb28ef562f9ac94)
- [flags](../hardware/P364_CAN过滤器结构.md#a7616e21f33be5fb43094d44530a1c5de)
- [can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)
- [tx_err_cnt](../hardware/P365_CAN错误计数结构.md#a01bb2cb16656d0fd4f99cfbfa1f30e98)
- [rx_err_cnt](../hardware/P365_CAN错误计数结构.md#a6be6ce6b592641ba0dce36fe1cd8902a)
- [can_timing](../hardware/P366_CAN时序结构.md)
- [sjw](../hardware/P366_CAN时序结构.md#a5af76a4ee9c741642ec19265a47fceb5)
- [prop_seg](../hardware/P366_CAN时序结构.md#ac009d40fee9788b663963978498b2ee9)
- [phase_seg1](../hardware/P366_CAN时序结构.md#a9941688e79fa4ce01c4b498433319089)
- [phase_seg2](../hardware/P366_CAN时序结构.md#a6ca0caf618d28a761c3c8859ed3a68d6)
- [prescaler](../hardware/P366_CAN时序结构.md#a74fb8341cbb6d97721c9d0afbc7e1f3a)
- [can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)
- [device](../device_reference/P002_设备对象结构.md)
- [can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)
- [can_state_change_callback_t](../hardware/P362_CAN控制器接口.md#ga002ff7ba1f5be374510a902459dd9d3d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [can_state_change_callback](../hardware/P367_CAN状态变化回调结构.md)
- [can_state_change_callback_handler_t](../hardware/P362_CAN控制器接口.md#ga1dc18f69fe06a1d919b13f929100fa85)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../hardware/P367_CAN状态变化回调结构.md#a20e10ceff66aefd6e77340687cab3f40)
- [handler](../hardware/P367_CAN状态变化回调结构.md#a3bf66a334174307bde9c0fe12939a503)
- [can_driver_config](../hardware/P371_CAN驱动公共配置.md)
- [phy](../hardware/P371_CAN驱动公共配置.md#a8e9f0ec132daf25a2e947478c0b952a3)
- [min_bitrate](../hardware/P371_CAN驱动公共配置.md#accc9f1b6202b2b30b60bbc890190d3c3)
- [max_bitrate](../hardware/P371_CAN驱动公共配置.md#a420d9f8762ae332d4d78084dd74afa6e)
- [bitrate](../hardware/P371_CAN驱动公共配置.md#a6f4f050b5aeb8cd466a12d70c53e8423)
- [sample_point](../hardware/P371_CAN驱动公共配置.md#a2cd7693cd9acc0537a085cdc85688a96)
- [sample_point_data](../hardware/P371_CAN驱动公共配置.md#afa6cd8cb79ccad28ca86caec4d92cd85)
- [bitrate_data](../hardware/P371_CAN驱动公共配置.md#afd7a831b33b059f47dd867726e31e69b)
- [can_driver_data](../hardware/P372_CAN驱动公共数据.md)
- [mode](../hardware/P372_CAN驱动公共数据.md#a1f01de3a78be9193263a47acf4181b93)
- [started](../hardware/P372_CAN驱动公共数据.md#a5b3983ca54213c84f8278ec36f0fb0ce)
- [legacy_state_change_cb](../hardware/P372_CAN驱动公共数据.md#a281054c5102f22c362691b81efbb8162)
- [legacy_state_change_cb_handler](../hardware/P372_CAN驱动公共数据.md#af6a94bfe3b21502dc70548b470f732b4)
- [legacy_state_change_cb_user_data](../hardware/P372_CAN驱动公共数据.md#a646e5422136017bed629e5a0f80d4824)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [state_change_callback_lock](../hardware/P372_CAN驱动公共数据.md#a5b8a964383a759a0144a1b72bb8835cc)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [state_change_callbacks](../hardware/P372_CAN驱动公共数据.md#afce7bbd484eea2660fe71f0322103265)
- [can_set_timing_t](../hardware/P369_CAN控制器后端接口.md#ga01a5f028d947582dd4195b467dae8b94)
- [can_set_timing_data_t](../hardware/P369_CAN控制器后端接口.md#ga7be2d21503b59cde52369d589ccff80f)
- [can_get_capabilities_t](../hardware/P369_CAN控制器后端接口.md#ga2fd489217c19977d239d51f0b3fcfc19)
- [can_start_t](../hardware/P369_CAN控制器后端接口.md#gaecca113e6b8cc7caba3d19fdd104aaa7)
- [can_stop_t](../hardware/P369_CAN控制器后端接口.md#ga1ab69e7991b8492e36c4b3f359db1961)
- [can_set_mode_t](../hardware/P369_CAN控制器后端接口.md#ga231b61f4d1413e0d28dd5a8bc25a89b3)
- [can_send_t](../hardware/P369_CAN控制器后端接口.md#ga89108f1d99fa1ba784808f1e99763a58)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [can_add_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga3bc249502cb65bf89bce2ca87535ac6b)
- [can_remove_rx_filter_t](../hardware/P369_CAN控制器后端接口.md#ga20ee94c5122acb6fd7fe5939a20ba748)
- [can_recover_t](../hardware/P369_CAN控制器后端接口.md#ga8bcafa14e23f2ba70e17c1432449d744)
- [can_get_state_t](../hardware/P369_CAN控制器后端接口.md#ga14210ea7870ef23072cd61c10043540f)
- [can_get_core_clock_t](../hardware/P369_CAN控制器后端接口.md#ga4d44354cda4cfe0af5262189549d6523)
- [can_get_max_filters_t](../hardware/P369_CAN控制器后端接口.md#ga946dd40c12eba40c34afa7572d61456c)
- [can_state_change_callbacks_enabled_t](../hardware/P369_CAN控制器后端接口.md#ga80424a027933c3bc0d973f37333d2618)
- [can_fire_state_change_callbacks](../hardware/P369_CAN控制器后端接口.md#gaba24cc4eb2fa759ff8394dd096021982)
- [can_driver_api](../hardware/P370_CAN驱动函数表.md)
- [get_capabilities](../hardware/P370_CAN驱动函数表.md#a11d2ff416d459faf84905e7ffdc1a536)
- [start](../hardware/P370_CAN驱动函数表.md#ac42f6d438d3e88f0db8e64c236621f8a)
- [stop](../hardware/P370_CAN驱动函数表.md#a3ca1cb8bcd6713bfdf20f76cee3bc3a4)
- [set_mode](../hardware/P370_CAN驱动函数表.md#accfe8e3e40e5bae33b8c31b1af55c644)
- [set_timing](../hardware/P370_CAN驱动函数表.md#a356b3761926c2a5a85fcc80b2e8a4643)
- [send](../hardware/P370_CAN驱动函数表.md#a9b5ec5c71a126798c24a19d1c91f879b)
- [add_rx_filter](../hardware/P370_CAN驱动函数表.md#a56225a8cb458baa0d1745ff5e9202ae6)
- [remove_rx_filter](../hardware/P370_CAN驱动函数表.md#ac264f4d66a29a5f42aaf2b6c9665f8f3)
- [recover](../hardware/P370_CAN驱动函数表.md#aba563aff4e114b7956bb824efdebb0c6)
- [get_state](../hardware/P370_CAN驱动函数表.md#aa6b8b2b7c544cf78930b45cab1e6dbb4)
- [state_change_callbacks_enabled](../hardware/P370_CAN驱动函数表.md#a90547b28015e2b7eea6a548b0ab2b576)
- [get_core_clock](../hardware/P370_CAN驱动函数表.md#ae969c18839dc5f1cb4356df6d1ee1e20)
- [get_max_filters](../hardware/P370_CAN驱动函数表.md#a24a90bc4d49818985479bfe101cc21d4)
- [timing_min](../hardware/P370_CAN驱动函数表.md#aeaa8022843f787bddbb18aa407d340a5)
- [timing_max](../hardware/P370_CAN驱动函数表.md#a90dca9dd3baef96c4d3849be367129b5)
- [set_timing_data](../hardware/P370_CAN驱动函数表.md#a1951bfc3135824e364d5f18aa9b15d09)
- [timing_data_min](../hardware/P370_CAN驱动函数表.md#a5ad424b27606f9de8f37524594d396dc)
- [timing_data_max](../hardware/P370_CAN驱动函数表.md#ac07eeec7b96543b19041a28d70e19a97)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)
- [STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)
- [STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)
- [STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)
- [STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)
- [STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)
- [STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)
- [can_device_state](../hardware/P368_CAN设备状态结构.md)
- [device_state](../device_reference/P003_设备运行状态结构.md)
- [devstate](../hardware/P368_CAN设备状态结构.md#a28061ff1193176dd01b7bb9a88f402ec)
- [stats](../hardware/P368_CAN设备状态结构.md#ae05c85eae4f6bee075ffdc4f0ab56f47)
- [can_get_core_clock](../hardware/P362_CAN控制器接口.md#ga4af6d0d9ab72b195909f511ac65cb8fa)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [can_get_bitrate_min](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [can_get_bitrate_max](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)
- [can_get_timing_min](../hardware/P362_CAN控制器接口.md#ga5a57627de4764f0bd3b4bafe07f56e6f)
- [can_get_timing_max](../hardware/P362_CAN控制器接口.md#gabe385d0f003b1e990c78ef7a2a3f9616)
- [can_calc_timing](../hardware/P362_CAN控制器接口.md#gac27fe64142603f0d32d422594356b2d7)
- [can_get_timing_data_min](../hardware/P362_CAN控制器接口.md#ga6399ef0cefdab3da738136f8a5c59c2f)
- [can_get_timing_data_max](../hardware/P362_CAN控制器接口.md#ga47a2f6d6b42121b390aa92160c833b80)
- [can_calc_timing_data](../hardware/P362_CAN控制器接口.md#ga358cd73ed59c2099f4b2c6ceb397ca11)
- [can_set_timing_data](../hardware/P362_CAN控制器接口.md#ga606cf9fda4c66a0f4abf74e1d357eac2)
- [can_set_bitrate_data](../hardware/P362_CAN控制器接口.md#ga0afd2c446fc5e685370641a1678f87b7)
- [can_set_timing](../hardware/P362_CAN控制器接口.md#ga1b134af5d6286ea0fee130b6da5217da)
- [can_get_capabilities](../hardware/P362_CAN控制器接口.md#ga4afd7776c5039dec8acb089499dc1168)
- [can_get_transceiver](../hardware/P362_CAN控制器接口.md#gae012d26711c2a7ce1419d21c38cae63a)
- [can_start](../hardware/P362_CAN控制器接口.md#gae48dfa8bc5b52f233b9b1a08aac2675a)
- [can_stop](../hardware/P362_CAN控制器接口.md#ga1b0ac9185341cb0bde85ec64e4c490a5)
- [can_set_mode](../hardware/P362_CAN控制器接口.md#gae04c3c884b3ed26dfea4745b7dff2c5f)
- [can_get_mode](../hardware/P362_CAN控制器接口.md#gabd201b5b1fca54048985a8a24dd51e55)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [can_set_bitrate](../hardware/P362_CAN控制器接口.md#ga0685ebfacfb79d33131167ac3aaa6f9b)
- [can_send](../hardware/P362_CAN控制器接口.md#ga446ee31913699de3c80be05d837b5fd5)
- [can_add_rx_filter](../hardware/P362_CAN控制器接口.md#gae9dd69a13b960f773ab07bb0bb13b5e9)
- [can_add_rx_filter_msgq](../hardware/P362_CAN控制器接口.md#gaaac20a068b7f32d2f38d1601d588b35c)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [can_remove_rx_filter](../hardware/P362_CAN控制器接口.md#ga822aa3142ea01582d5cfb8b478fb2847)
- [can_get_max_filters](../hardware/P362_CAN控制器接口.md#ga526c08539094486f07dc52aad8ed0dcc)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [can_get_state](../hardware/P362_CAN控制器接口.md#gab98c121578c8349d9dfb41d60f356857)
- [can_recover](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e)
- [can_set_state_change_callback](../hardware/P362_CAN控制器接口.md#gacda2bc21fa0cbd7b3406dd096827923c)
- [can_init_state_change_callback](../hardware/P362_CAN控制器接口.md#gabf813d9f21982f674b213708adee9e96)
- [can_add_state_change_callback](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)
- [can_remove_state_change_callback](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)
- [can_stats_get_bit_errors](../hardware/P362_CAN控制器接口.md#ga27b277f3b5146590f159171f602904db)
- [can_stats_get_bit0_errors](../hardware/P362_CAN控制器接口.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)
- [can_stats_get_bit1_errors](../hardware/P362_CAN控制器接口.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)
- [can_stats_get_stuff_errors](../hardware/P362_CAN控制器接口.md#ga162fde4e622fb06dcbbcf2f31bb35d38)
- [can_stats_get_crc_errors](../hardware/P362_CAN控制器接口.md#ga31692aef7962172532f8200fed7aecd2)
- [can_stats_get_form_errors](../hardware/P362_CAN控制器接口.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)
- [can_stats_get_ack_errors](../hardware/P362_CAN控制器接口.md#ga4f8414d64b75d4d1ffb7a0feff36f698)
- [can_stats_get_rx_overruns](../hardware/P362_CAN控制器接口.md#ga8664fbaa13f4bb89540493264d2a041d)
- [can_dlc_to_bytes](../hardware/P362_CAN控制器接口.md#gaa1d866167c0c23f8d5c0c15385589601)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [can_bytes_to_dlc](../hardware/P362_CAN控制器接口.md#ga8314716fe2b66d567b3fd377b8ee9dc3)
- [can_frame_matches_filter](../hardware/P362_CAN控制器接口.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)
- [CAN_FRAME_IDE](../hardware/P362_CAN控制器接口.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)
- [CAN_FILTER_IDE](../hardware/P362_CAN控制器接口.md#gafa40c165d016955ec0c856a7fd53168f)
- [zephyr/net/canbus.h](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html)

---

[上一章](P001_CAN驱动头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_CAN收发器头文件参考.md)
