---
id: learning.zephyr-docs.api-source-supplement-reference.page-25
title: cellular.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_cellular.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)。

## 25.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
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
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00205"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
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
<a id="foldopen00349"></a>
<a id="l00349"></a>
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
<a id="foldopen00373"></a>
<a id="l00373"></a>
<a id="l00374"></a>
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
<a id="foldopen00397"></a>
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
<a id="foldopen00421"></a>
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
<a id="foldopen00449"></a>
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
<a id="foldopen00476"></a>
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
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="foldopen00520"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__cellular__interface__backend_html_ga03095206ae2b77ce232dd05b172bd56d"></a>
<a id="agroup__cellular__interface__backend_html_ga08a0966933caa70d7044342ed2ad8eb6"></a>
<a id="agroup__cellular__interface__backend_html_ga30f5fef993f17b001e2df9c89bdaf288"></a>
<a id="agroup__cellular__interface__backend_html_ga6aa2c51fa80d5420593021c35444308a"></a>
<a id="agroup__cellular__interface__backend_html_ga71ddc5b9e09da398d02caadc91ef3cfc"></a>
<a id="agroup__cellular__interface__backend_html_ga75cac77838970288d4d23647eaafd30b"></a>
<a id="agroup__cellular__interface__backend_html_ga975fe3a63ed2dd936faa619846f8b701"></a>
<a id="agroup__cellular__interface__backend_html_gabf5bd5a939a300b8493f7c803b9128f0"></a>
<a id="agroup__cellular__interface__backend_html_gacbf9c85b2ea95321beee0ba75d5977f7"></a>
<a id="agroup__cellular__interface_html_ga022eb4eecc300b14110107a46824cac0"></a>
<a id="agroup__cellular__interface_html_ga12d74b4ec0821f5eed95f24350789ed3"></a>
<a id="agroup__cellular__interface_html_ga168002533ce39996e68bda2c2e92428e"></a>
<a id="agroup__cellular__interface_html_ga27c0b71128c782a7f42832b82eb94411"></a>
<a id="agroup__cellular__interface_html_ga4494e4d41149ea48fd1e0d8fe9b441dd"></a>
<a id="agroup__cellular__interface_html_ga70340d22df56665b1d113abc8b314a95"></a>
<a id="agroup__cellular__interface_html_ga7309390ed507748fdb72cf078b8e08a4"></a>
<a id="agroup__cellular__interface_html_ga746c0862b9a5da7c766e42e4d6025f47"></a>
<a id="agroup__cellular__interface_html_ga757f0802fd72d61d035a81057f23d5ca"></a>
<a id="agroup__cellular__interface_html_ga7b6e210b9e5222b789af52b4ef8cc850"></a>
<a id="agroup__cellular__interface_html_ga84efd3405e5233358514c7d634710042"></a>
<a id="agroup__cellular__interface_html_gaa53d52e58221c998eec272a4d063bdd4"></a>
<a id="agroup__cellular__interface_html_gac9d02d18ed6e0af07e480cde678afdc1"></a>
<a id="agroup__cellular__interface_html_gad1e37b428eaacc7442f6a6cb2e1404a5"></a>
<a id="agroup__cellular__interface_html_gad6e38e31d82075c51933fcbb2ff2de30"></a>
<a id="agroup__cellular__interface_html_gae0ca6816f75b89055aa31370196e2c98"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a"></a>
<a id="agroup__cellular__interface_html_gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0"></a>
<a id="agroup__cellular__interface_html_gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910"></a>
<a id="agroup__cellular__interface_html_gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c"></a>
<a id="agroup__cellular__interface_html_gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb"></a>
<a id="agroup__cellular__interface_html_gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a"></a>
<a id="agroup__cellular__interface_html_gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3"></a>
<a id="agroup__cellular__interface_html_gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d"></a>
<a id="agroup__cellular__interface_html_gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338"></a>
<a id="agroup__cellular__interface_html_gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a"></a>
<a id="agroup__cellular__interface_html_gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027"></a>
<a id="agroup__cellular__interface_html_ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructcellular__driver__api_html"></a>
<a id="astructcellular__driver__api_html_a0bf599ed34ee55aacf4be01e22d86b30"></a>
<a id="astructcellular__driver__api_html_a17153560e19ddd9a64991780372a2531"></a>
<a id="astructcellular__driver__api_html_a32ede01e742a2e7c18e9cb4f963b90fe"></a>
<a id="astructcellular__driver__api_html_a40a6b2d890790e1a521f227e5c296b5b"></a>
<a id="astructcellular__driver__api_html_a4982b88e4342abd6582d10b02f2e6ed0"></a>
<a id="astructcellular__driver__api_html_a7641d06668b65b007fd4a3a900bbde0e"></a>
<a id="astructcellular__driver__api_html_a7d64a630e4dafd57c00b04d3dfea1b79"></a>
<a id="astructcellular__driver__api_html_ab03cc8706fafd729c21cec9569eae8db"></a>
<a id="astructcellular__driver__api_html_ac219c2c960f838bc8c0fd41307a3ff05"></a>
<a id="astructcellular__evt__modem__comms__check__result_html"></a>
<a id="astructcellular__evt__modem__comms__check__result_html_a86871d448e51af8535fffa445606f9a7"></a>
<a id="astructcellular__evt__modem__info_html"></a>
<a id="astructcellular__evt__modem__info_html_a4dde2a070347472bff450618ec6edc58"></a>
<a id="astructcellular__evt__network__status_html"></a>
<a id="astructcellular__evt__network__status_html_a05560bf076d95474ab31446dae885929"></a>
<a id="astructcellular__evt__network__status_html_a5bc9286d12c896dafceaa360fcf0ee88"></a>
<a id="astructcellular__evt__network__status_html_a745836b09443091c3bde36c948618e88"></a>
<a id="astructcellular__evt__network__status_html_a7bcc34cb84634f0486e522d489d91ca4"></a>
<a id="astructcellular__evt__network__status_html_a880a490f7b9d32e281db74c8514070ce"></a>
<a id="astructcellular__evt__network__status_html_a8cbeeb2f3c189d4c88cbc9cbbe126a1a"></a>
<a id="astructcellular__evt__network__status_html_a91a24ffc204b5a5aa02ed06f6595dbaa"></a>
<a id="astructcellular__evt__network__status_html_aa74bd93e515506bf39ff5a7691982092"></a>
<a id="astructcellular__evt__network__status_html_ac8192ebc31182517665b27534bffc58c"></a>
<a id="astructcellular__evt__network__status_html_adbd6f936f455eff7e3b9217bd7c1d3d4"></a>
<a id="astructcellular__evt__network__status_html_aee20974803aa32c8fd6e6f4beacc16f9"></a>
<a id="astructcellular__evt__network__status_html_aeeae2197619a01211463ee194c643f59"></a>
<a id="astructcellular__evt__network__status_html_af1e429365b99183adc51689e04ff1079"></a>
<a id="astructcellular__evt__registration__status_html"></a>
<a id="astructcellular__evt__registration__status_html_a24432c0d1d942d08e4d7daa55c3fce51"></a>
<a id="astructcellular__network_html"></a>
<a id="astructcellular__network_html_a9313dcce10911b0febd56022c380f283"></a>
<a id="astructcellular__network_html_ab54057fc7cea1387c5ad3694103b0686"></a>
<a id="astructcellular__network_html_ad7afde61da3322e80f935c2b963eacf0"></a>
<a id="astructcellular__stats_html"></a>
<a id="astructcellular__stats_html_a48298ae752e4950d81929c2e77724f9f"></a>
<a id="astructcellular__stats_html_a5385d92eca6a89ebce4845624aa5b52a"></a>
<a id="astructcellular__stats_html_a55182117beb8835b88933fc06bbf456b"></a>
<a id="astructcellular__stats_html_a802456c378f817a07404c4d3cd488109"></a>
<a id="astructcellular__stats_html_ad5bd53938a943cac53c0efadcc292022"></a>
<a id="astructcellular__stats_html_aea6fa41e067af9130a8680c2f2b65af6"></a>
<a id="astructcellular__stats_html_af542f63589fdeecc4c6f108865177841"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2023 Bjarki Arge Andreasen
 * Copyright (c) 2023 Lucas Denefle
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CELLULAR_H_
#define ZEPHYR_INCLUDE_DRIVERS_CELLULAR_H_


#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum cellular_access_technology {
        CELLULAR_ACCESS_TECHNOLOGY_GSM = 0,
        CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT = 1,
        CELLULAR_ACCESS_TECHNOLOGY_UTRAN = 2,
        CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS = 3,
        CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA = 4,
        CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA = 5,
        CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA = 6,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN = 7,
        CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT = 8,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1 = 9,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN = 10,
        CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN = 11,
        CELLULAR_ACCESS_TECHNOLOGY_NG_RAN = 12,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL = 13,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT = 14,
        CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT = 15,
        CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT = 16,
        CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN = 255,
};

struct cellular_network {
        enum cellular_access_technology technology;
        uint16_t *bands;
        uint16_t size;
};

enum cellular_signal_type {
        CELLULAR_SIGNAL_RSSI,
        CELLULAR_SIGNAL_RSRP,
        CELLULAR_SIGNAL_RSRQ,
};

enum cellular_modem_info_type {
        CELLULAR_MODEM_INFO_IMEI,
        CELLULAR_MODEM_INFO_MODEL_ID,
        CELLULAR_MODEM_INFO_MANUFACTURER,
        CELLULAR_MODEM_INFO_FW_VERSION,
        CELLULAR_MODEM_INFO_SIM_IMSI,
        CELLULAR_MODEM_INFO_SIM_ICCID,
        CELLULAR_MODEM_INFO_SERIAL_NUMBER,
};

enum cellular_registration_status {
        CELLULAR_REGISTRATION_NOT_REGISTERED = 0,
        CELLULAR_REGISTRATION_REGISTERED_HOME = 1,
        CELLULAR_REGISTRATION_SEARCHING = 2,
        CELLULAR_REGISTRATION_DENIED = 3,
        CELLULAR_REGISTRATION_UNKNOWN = 4,
        CELLULAR_REGISTRATION_REGISTERED_ROAMING = 5,
        CELLULAR_REGISTRATION_SMS_ONLY_HOME = 6,
        CELLULAR_REGISTRATION_SMS_ONLY_ROAMING = 7,
        CELLULAR_REGISTRATION_EMERGENCY_ONLY = 8,
        CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME = 9,
        CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING = 10,
        CELLULAR_REGISTRATION_RLOS = 11,
};

enum cellular_event {
        CELLULAR_EVENT_MODEM_INFO_CHANGED = BIT(0),
        CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED = BIT(1),
        CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT = BIT(2),
        CELLULAR_EVENT_NETWORK_STATUS_CHANGED = BIT(3),
        CELLULAR_EVENT_MODEM_SUSPENDED = BIT(4),
};

/* Opaque bit-mask large enough for all current & future events */
typedef uint32_t cellular_event_mask_t;

struct cellular_evt_modem_info {
        enum cellular_modem_info_type field;
};

struct cellular_evt_registration_status {
        enum cellular_registration_status status;
};

struct cellular_evt_modem_comms_check_result {
        bool success;
};

#define CELLULAR_EUTRAN_CELL_ID_MAX     0xFFFFFFFU
#define CELLULAR_EUTRAN_CELL_ID_INVALID UINT32_MAX

struct cellular_evt_network_status {
        enum cellular_registration_status status;
        enum cellular_access_technology access_tech;
        union {
                struct {
                        uint16_t mcc;
                        uint16_t mnc;
                        uint32_t tac;
                        uint32_t earfcn;
                        uint32_t gci;
                        uint16_t phys_cell_id;
                        uint16_t band;
                        int16_t rsrp;
                        int8_t rsrq;
                } lte;
        } cell;
};

struct cellular_stats {
        uint32_t outage_ms;
        uint32_t deregistrations;
        uint32_t link_drops;
        uint32_t command_failures;
        uint32_t command_errors_cme;
        uint32_t recoveries;
        uint32_t cmux_disconnects;
};

typedef void (*cellular_event_cb_t)(const struct device *dev, enum cellular_event event,
                                    const void *payload, void *user_data);


typedef int (*cellular_api_configure_networks)(const struct device *dev,
                                               const struct cellular_network *networks,
                                               uint8_t size);

typedef int (*cellular_api_get_supported_networks)(const struct device *dev,
                                                   const struct cellular_network **networks,
                                                   uint8_t *size);

typedef int (*cellular_api_get_signal)(const struct device *dev,
                                       const enum cellular_signal_type type, int16_t *value);

typedef int (*cellular_api_get_modem_info)(const struct device *dev,
                                           const enum cellular_modem_info_type type, char *info,
                                           size_t size);

typedef int (*cellular_api_get_registration_status)(const struct device *dev,
                                                    enum cellular_access_technology tech,
                                                    enum cellular_registration_status *status);

typedef int (*cellular_api_get_network_status)(const struct device *dev,
                                               struct cellular_evt_network_status *status);

typedef int (*cellular_api_set_apn)(const struct device *dev, const char *apn);

typedef int (*cellular_api_set_callback)(const struct device *dev, cellular_event_mask_t mask,
                                         cellular_event_cb_t cb, void *user_data);

typedef const struct cellular_stats *(*cellular_api_get_stats)(const struct device *dev);

__subsystem struct cellular_driver_api {
        cellular_api_configure_networks configure_networks;
        cellular_api_get_supported_networks get_supported_networks;
        cellular_api_get_signal get_signal;
        cellular_api_get_modem_info get_modem_info;
        cellular_api_get_registration_status get_registration_status;
        cellular_api_get_network_status get_network_status;
        cellular_api_set_apn set_apn;
        cellular_api_set_callback set_callback;
        cellular_api_get_stats get_stats;
};


static inline int cellular_configure_networks(const struct device *dev,
                                              const struct cellular_network *networks, uint8_t size)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->configure_networks == NULL) {
                return -ENOSYS;
        }

        return api->configure_networks(dev, networks, size);
}

static inline int cellular_get_supported_networks(const struct device *dev,
                                                  const struct cellular_network **networks,
                                                  uint8_t *size)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_supported_networks == NULL) {
                return -ENOSYS;
        }

        return api->get_supported_networks(dev, networks, size);
}

static inline int cellular_get_signal(const struct device *dev,
                                      const enum cellular_signal_type type, int16_t *value)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_signal == NULL) {
                return -ENOSYS;
        }

        return api->get_signal(dev, type, value);
}

static inline int cellular_get_modem_info(const struct device *dev,
                                          const enum cellular_modem_info_type type, char *info,
                                          size_t size)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_modem_info == NULL) {
                return -ENOSYS;
        }

        return api->get_modem_info(dev, type, info, size);
}

static inline int cellular_get_registration_status(const struct device *dev,
                                                   enum cellular_access_technology tech,
                                                   enum cellular_registration_status *status)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_registration_status == NULL) {
                return -ENOSYS;
        }

        return api->get_registration_status(dev, tech, status);
}

static inline int cellular_get_network_status(const struct device *dev,
                                              struct cellular_evt_network_status *status)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_network_status == NULL) {
                return -ENOSYS;
        }

        return api->get_network_status(dev, status);
}

static inline int cellular_set_apn(const struct device *dev, const char *apn)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->set_apn == NULL) {
                return -ENOSYS;
        }

        return api->set_apn(dev, apn);
}

static inline int cellular_set_callback(const struct device *dev, cellular_event_mask_t mask,
                                        cellular_event_cb_t cb, void *user_data)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->set_callback == NULL) {
                return -ENOSYS;
        }

        return api->set_callback(dev, mask, cb, user_data);
}

static inline const struct cellular_stats *cellular_get_stats(const struct device *dev)
{
        const struct cellular_driver_api *api = DEVICE_API_GET(cellular, dev);

        if (api->get_stats == NULL) {
                return NULL;
        }

        return api->get_stats(dev);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CELLULAR_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Bjarki Arge Andreasen。

版权（Copyright）：© 2023 Lucas Denefle。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 158 行

不透明位掩码（Opaque bit-mask），其大小足以容纳当前和未来的所有事件。

### 注释 3：原第 539 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CELLULAR_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM_COMPACT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae873585f9cbcf08668b15c9975dbce2a)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072ced96c691fab5cb85d5575fa7b08c)
- [CELLULAR_ACCESS_TECHNOLOGY_GSM_EGPRS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab57f563e0bd20ca624ed4eba17a6d8cc)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eafa5e3d789a6ca355973ee72aa1fe5bc0)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea869253283f89a0a650d9f160e9290c74)
- [CELLULAR_ACCESS_TECHNOLOGY_UTRAN_HSDPA_HSUPA](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea76229e892337f56e214c6311af63cb30)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea5adc6a7b3ba0fc14ab94db30c94903a1)
- [CELLULAR_ACCESS_TECHNOLOGY_EC_GSM_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea072356e9786d90a3c063cdb43367dd55)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea4f74ce0a42248588e5d8d050738eb6f2)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead3212a0d14946d5ba8211196be62bd7f)
- [CELLULAR_ACCESS_TECHNOLOGY_NR_5G_CN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ead028d3220aadf7833fee04e6e0137d37)
- [CELLULAR_ACCESS_TECHNOLOGY_NG_RAN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea50df1e2a57d3eee30acdbda37f766273)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRA_NR_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea3fd5a8ea6e5c029afcf6a4f5f22a155a)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_NB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428ea658c1d3ccbc40e2d20994ef9df203b15)
- [CELLULAR_ACCESS_TECHNOLOGY_E_UTRAN_WB_S1_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab7f50acc7cb82d3a1c69d14e353c64de)
- [CELLULAR_ACCESS_TECHNOLOGY_NG_RAN_SAT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eae70a9d212ee846be7071a29aedbd9383)
- [CELLULAR_ACCESS_TECHNOLOGY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga168002533ce39996e68bda2c2e92428eab151715b8b7659774f3e17107986b117)
- [cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)
- [technology](../modem_wireless_model_reference/P007_cellular_network_结构体.md#ad7afde61da3322e80f935c2b963eacf0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bands](../modem_wireless_model_reference/P007_cellular_network_结构体.md#a9313dcce10911b0febd56022c380f283)
- [size](../modem_wireless_model_reference/P007_cellular_network_结构体.md#ab54057fc7cea1387c5ad3694103b0686)
- [cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)
- [CELLULAR_SIGNAL_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a)
- [CELLULAR_SIGNAL_RSRP](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a)
- [CELLULAR_SIGNAL_RSRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338)
- [cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)
- [CELLULAR_MODEM_INFO_IMEI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de)
- [CELLULAR_MODEM_INFO_MODEL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8)
- [CELLULAR_MODEM_INFO_MANUFACTURER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1)
- [CELLULAR_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027)
- [CELLULAR_MODEM_INFO_SIM_IMSI](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245)
- [CELLULAR_MODEM_INFO_SIM_ICCID](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)
- [CELLULAR_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [CELLULAR_REGISTRATION_NOT_REGISTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27)
- [CELLULAR_REGISTRATION_REGISTERED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe)
- [CELLULAR_REGISTRATION_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175)
- [CELLULAR_REGISTRATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e)
- [CELLULAR_REGISTRATION_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1)
- [CELLULAR_REGISTRATION_REGISTERED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d)
- [CELLULAR_REGISTRATION_SMS_ONLY_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a8b009c5bf5a90654159e99d76143991b)
- [CELLULAR_REGISTRATION_SMS_ONLY_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a94abe9b635eed7676fffefe8c725de27)
- [CELLULAR_REGISTRATION_EMERGENCY_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4af8c395ea7856c2d055628a0cccda01d3)
- [CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_HOME](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4acbe368932e155a47f9a7599240c8a252)
- [CELLULAR_REGISTRATION_CSFB_NOT_PREFERRED_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4a3e5fd74f719359a8814e601c47de9d97)
- [CELLULAR_REGISTRATION_RLOS](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga7309390ed507748fdb72cf078b8e08a4ad17cb225c92748c0e51aeca35a24810b)
- [cellular_event](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga27c0b71128c782a7f42832b82eb94411)
- [CELLULAR_EVENT_MODEM_INFO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a)
- [CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)
- [CELLULAR_EVENT_NETWORK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ac2dbb518ff14d7f0d44c9a7177cc0e99)
- [CELLULAR_EVENT_MODEM_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a84372dd685d58830ab721748f003737c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)
- [cellular_evt_modem_info](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md)
- [field](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md#a4dde2a070347472bff450618ec6edc58)
- [cellular_evt_registration_status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md)
- [status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md#a24432c0d1d942d08e4d7daa55c3fce51)
- [cellular_evt_modem_comms_check_result](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md)
- [success](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md#a86871d448e51af8535fffa445606f9a7)
- [cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)
- [status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a05560bf076d95474ab31446dae885929)
- [access_tech](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#ac8192ebc31182517665b27534bffc58c)
- [mcc](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aeeae2197619a01211463ee194c643f59)
- [mnc](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a745836b09443091c3bde36c948618e88)
- [tac](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a91a24ffc204b5a5aa02ed06f6595dbaa)
- [earfcn](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#af1e429365b99183adc51689e04ff1079)
- [gci](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aa74bd93e515506bf39ff5a7691982092)
- [phys_cell_id](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a5bc9286d12c896dafceaa360fcf0ee88)
- [band](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a8cbeeb2f3c189d4c88cbc9cbbe126a1a)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [rsrp](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#adbd6f936f455eff7e3b9217bd7c1d3d4)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [rsrq](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a7bcc34cb84634f0486e522d489d91ca4)
- [lte](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a880a490f7b9d32e281db74c8514070ce)
- [cell](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aee20974803aa32c8fd6e6f4beacc16f9)
- [cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)
- [outage_ms](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a55182117beb8835b88933fc06bbf456b)
- [deregistrations](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#aea6fa41e067af9130a8680c2f2b65af6)
- [link_drops](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#ad5bd53938a943cac53c0efadcc292022)
- [command_failures](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a5385d92eca6a89ebce4845624aa5b52a)
- [command_errors_cme](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a48298ae752e4950d81929c2e77724f9f)
- [recoveries](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#af542f63589fdeecc4c6f108865177841)
- [cmux_disconnects](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a802456c378f817a07404c4d3cd488109)
- [cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)
- [device](../device_reference/P002_设备对象结构.md)
- [cellular_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga71ddc5b9e09da398d02caadc91ef3cfc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cellular_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga6aa2c51fa80d5420593021c35444308a)
- [cellular_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga75cac77838970288d4d23647eaafd30b)
- [cellular_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga03095206ae2b77ce232dd05b172bd56d)
- [cellular_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga08a0966933caa70d7044342ed2ad8eb6)
- [cellular_api_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga30f5fef993f17b001e2df9c89bdaf288)
- [cellular_api_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gabf5bd5a939a300b8493f7c803b9128f0)
- [cellular_api_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gacbf9c85b2ea95321beee0ba75d5977f7)
- [cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)
- [configure_networks](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#ac219c2c960f838bc8c0fd41307a3ff05)
- [get_supported_networks](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a32ede01e742a2e7c18e9cb4f963b90fe)
- [get_signal](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a7d64a630e4dafd57c00b04d3dfea1b79)
- [get_modem_info](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#ab03cc8706fafd729c21cec9569eae8db)
- [get_registration_status](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a7641d06668b65b007fd4a3a900bbde0e)
- [get_network_status](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a17153560e19ddd9a64991780372a2531)
- [set_apn](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a40a6b2d890790e1a521f227e5c296b5b)
- [set_callback](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a4982b88e4342abd6582d10b02f2e6ed0)
- [cellular_api_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga975fe3a63ed2dd936faa619846f8b701)
- [get_stats](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a0bf599ed34ee55aacf4be01e22d86b30)
- [cellular_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gaa53d52e58221c998eec272a4d063bdd4)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [cellular_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga70340d22df56665b1d113abc8b314a95)
- [cellular_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga022eb4eecc300b14110107a46824cac0)
- [cellular_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga757f0802fd72d61d035a81057f23d5ca)
- [cellular_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gae0ca6816f75b89055aa31370196e2c98)
- [cellular_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad1e37b428eaacc7442f6a6cb2e1404a5)
- [cellular_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga4494e4d41149ea48fd1e0d8fe9b441dd)
- [cellular_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7b6e210b9e5222b789af52b4ef8cc850)
- [cellular_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga12d74b4ec0821f5eed95f24350789ed3)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [cellular_driver_api::get_stats](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a0bf599ed34ee55aacf4be01e22d86b30)
- [cellular_driver_api::get_network_status](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a17153560e19ddd9a64991780372a2531)
- [cellular_driver_api::get_supported_networks](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a32ede01e742a2e7c18e9cb4f963b90fe)
- [cellular_driver_api::set_apn](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a40a6b2d890790e1a521f227e5c296b5b)
- [cellular_driver_api::set_callback](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a4982b88e4342abd6582d10b02f2e6ed0)
- [cellular_driver_api::get_registration_status](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a7641d06668b65b007fd4a3a900bbde0e)
- [cellular_driver_api::get_signal](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#a7d64a630e4dafd57c00b04d3dfea1b79)
- [cellular_driver_api::get_modem_info](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#ab03cc8706fafd729c21cec9569eae8db)
- [cellular_driver_api::configure_networks](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md#ac219c2c960f838bc8c0fd41307a3ff05)
- [cellular_evt_modem_comms_check_result::success](../modem_wireless_model_reference/P003_cellular_evt_modem_comms_check_result_结构体.md#a86871d448e51af8535fffa445606f9a7)
- [cellular_evt_modem_info::field](../modem_wireless_model_reference/P004_cellular_evt_modem_info_结构体.md#a4dde2a070347472bff450618ec6edc58)
- [cellular_evt_network_status::status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a05560bf076d95474ab31446dae885929)
- [cellular_evt_network_status::phys_cell_id](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a5bc9286d12c896dafceaa360fcf0ee88)
- [cellular_evt_network_status::mnc](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a745836b09443091c3bde36c948618e88)
- [cellular_evt_network_status::rsrq](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a7bcc34cb84634f0486e522d489d91ca4)
- [cellular_evt_network_status::lte](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a880a490f7b9d32e281db74c8514070ce)
- [cellular_evt_network_status::band](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a8cbeeb2f3c189d4c88cbc9cbbe126a1a)
- [cellular_evt_network_status::tac](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#a91a24ffc204b5a5aa02ed06f6595dbaa)
- [cellular_evt_network_status::gci](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aa74bd93e515506bf39ff5a7691982092)
- [cellular_evt_network_status::access_tech](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#ac8192ebc31182517665b27534bffc58c)
- [cellular_evt_network_status::rsrp](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#adbd6f936f455eff7e3b9217bd7c1d3d4)
- [cellular_evt_network_status::cell](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aee20974803aa32c8fd6e6f4beacc16f9)
- [cellular_evt_network_status::mcc](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#aeeae2197619a01211463ee194c643f59)
- [cellular_evt_network_status::earfcn](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md#af1e429365b99183adc51689e04ff1079)
- [cellular_evt_registration_status::status](../modem_wireless_model_reference/P006_cellular_evt_registration_status_结构体.md#a24432c0d1d942d08e4d7daa55c3fce51)
- [cellular_network::bands](../modem_wireless_model_reference/P007_cellular_network_结构体.md#a9313dcce10911b0febd56022c380f283)
- [cellular_network::size](../modem_wireless_model_reference/P007_cellular_network_结构体.md#ab54057fc7cea1387c5ad3694103b0686)
- [cellular_network::technology](../modem_wireless_model_reference/P007_cellular_network_结构体.md#ad7afde61da3322e80f935c2b963eacf0)
- [cellular_stats::command_errors_cme](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a48298ae752e4950d81929c2e77724f9f)
- [cellular_stats::command_failures](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a5385d92eca6a89ebce4845624aa5b52a)
- [cellular_stats::outage_ms](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a55182117beb8835b88933fc06bbf456b)
- [cellular_stats::cmux_disconnects](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#a802456c378f817a07404c4d3cd488109)
- [cellular_stats::link_drops](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#ad5bd53938a943cac53c0efadcc292022)
- [cellular_stats::deregistrations](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#aea6fa41e067af9130a8680c2f2b65af6)
- [cellular_stats::recoveries](../modem_wireless_model_reference/P008_cellular_stats_结构体.md#af542f63589fdeecc4c6f108865177841)

---

[上一章](P024_cdc_acm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P026_ch32v00x-reset.h_源码浏览.md)
