<%inherit file="/species/show.mako" />

<script type="text/javascript" src="/rdbsea/fancybox/jquery.fancybox-1.3.1.pack.js"></script>
<link rel="stylesheet" href="/rdbsea/fancybox/jquery.fancybox-1.3.1.css" type="text/css" media="screen" />

<div class="span-30 alt">
    <h2>CERoPath species measurements compare with literature data</h2>
</div>

<div class="span-23">
    ${h.ui.Measurements(_id, publications_list, measures_infos, traits, full=True)}
</div>

<div class="span-7 last">
&nbsp;
% if image_paths:
    % for image_path in image_paths:
        <div>
            <a class="image" href="${image_path}"><img align="righ" style="padding-bottom:10px;padding-top:10px;" src="${image_path}" width="250px" /></a>
        </div>
    % endfor
% endif
</div>

<script>
$('document').ready(function(){
    $("a.image").fancybox({
        'titlePosition'  : 'over',
        'transitionIn'  :   'elastic',
        'transitionOut' :   'elastic',
        'speedIn'       :   600, 
        'speedOut'      :   200, 
        'overlayShow'   :   true,
    });
});
</script>
