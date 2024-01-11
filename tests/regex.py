import re
from bs4 import BeautifulSoup

str = '''
<div class="col-6 col-sm-4 col-md-3 col-lg-2 mb-1 minWDanime divCardUltimosEps" title="Enen no Shouboutai - Todos os Episódios"> <article class="card cardUltimosEps" style="height:285px"> <a href="https://animefire.plus/animes/enen-no-shouboutai-todos-os-episodios">  <div class="text-block" style="display: block;"> <img class="card-img-top imgAnimes transitioning_src" src="https://animefire.plus/img/animes/enen-no-shouboutai.webp" data-src="https://animefire.plus/img/animes/enen-no-shouboutai.webp" alt="Enen no Shouboutai - Todos os Episódios" ondragstart="if (!window.__cfRLUnblockHandlers) return false; return false" oncontextmenu="if (!window.__cfRLUnblockHandlers) return false; return false"><h3 class="animeTitle">Enen no Shouboutai</h3> </div> <div class="text-block1 text-center" style="top:5px !important;width:39px;height:25px !important;padding:2px 6px 0 6px !important;"> <span class="horaUltimosEps" style="width:100%">7.69</span> </div> <div class="text-blockCapaAnimeTags text-blockCapaAnimeTagsDL" style="background-color:#e36722 !important;opacity:.8;padding:0 0px 0 1px !important;right:48px !important;top:5px !important;left:unset !important"><span class="pr-1" style="width:29px;height:22px;padding:0px 3px 0 3px;font-size:14px;display:table;margin:1px;">A14</span></div> </a> </article> </div>
'''

soup = BeautifulSoup(str, 'html.parser')

div = soup.find('img', {'alt': re.compile(r'Todos os Episódios$')})

print(div['src'])