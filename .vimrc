version 6.0
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <expr> <S-Tab> pumvisible() ? "" : "<S-Tab>"
map! <S-Insert> <MiddleMouse>
map d :call RopeShowDoc()
map f :call RopeFindOccurrences()
map g :call RopeGotoDefinition()
map ru :call RopeUseFunction()
map rad :call RopeShowDoc()
map rac :call RopeShowCalltip()
map rx :call RopeRestructure()
map r1r :call RopeRenameCurrentModule()
map rr :call RopeRename()
map ro :call RopeOrganizeImports()
map r1v :call RopeMoveCurrentModule()
map rv :call RopeMove()
map r1p :call RopeModuleToPackage()
map ra? :call RopeLuckyAssist()
map raj :call RopeJumpToGlobal()
map rf :call RopeIntroduceFactory()
map ri :call RopeInline()
map rag :call RopeGotoDefinition()
map rnv :call RopeGenerateVariable()
map rnp :call RopeGeneratePackage()
map rnm :call RopeGenerateModule()
map rnf :call RopeGenerateFunction()
map rnc :call RopeGenerateClass()
map raf :call RopeFindOccurrences()
map rai :call RopeFindImplementations()
map rl :call RopeExtractVariable()
map rm :call RopeExtractMethod()
map ra/ :call RopeCodeAssist()
map rs :call RopeChangeSignature()
map  h
snoremap <silent> 	 i<Right>=TriggerSnippet()
snoremap <NL> i<Right>=TriggerSnippet()
nmap <NL> j
xmap <NL> j
omap <NL> j
map  k
map  l
map pu :call RopeUndo()
map pr :call RopeRedo()
map pc :call RopeProjectConfig()
map po :call RopeOpenProject()
map p4f :call RopeFindFileOtherWindow()
map pf :call RopeFindFile()
map pnp :call RopeCreatePackage()
map pnm :call RopeCreateModule()
map pnf :call RopeCreateFile()
map pnd :call RopeCreateDirectory()
map pk :call RopeCloseProject()
snoremap  b<BS>
snoremap % b<BS>%
snoremap ' b<BS>'
map ,mq <Plug>MBEMarkCurrent
map ,mbt <Plug>TMiniBufExplorer
map ,mbu <Plug>UMiniBufExplorer
map ,mbc <Plug>CMiniBufExplorer
map ,mbe <Plug>MiniBufExplorer
nmap <silent> ,b :CommandTBuffer
nnoremap ,S :%s/\s\+$//:let @/=''
nnoremap ,  :nohlsearch
nnoremap ,q :q
map ,p "+gP
nnoremap ,. :lcd %:p:h
map ,r :RopeRename
map ,j :RopeGotoDefinition
map ,g :GundoToggle
nmap ,a :Ack!
map ,f :CommandT
map ,n :NERDTreeToggle
nmap ,cc :cclose
nmap ,c :copen
map <silent> ,V :source ~/.vimrc:filetype detect:exe ":echo 'vimrc reloaded'"
map ,v :sp ~/.vimrc_
map ,dt :set makeprg=python\ manage.py\ test|:call MakeGreen()
nmap <silent> ,te :Pytest error
nmap <silent> ,tp :Pytest previous
nmap <silent> ,tn :Pytest next
nmap <silent> ,tm :Pytest method
nmap <silent> ,tc :Pytest class
nmap <silent> ,tf :Pytest file
map ,td <Plug>TaskList
imap ¿ =RopeLuckyAssistInsertMode()
imap ¯ =RopeCodeAssistInsertMode()
xmap S <Plug>VSurround
snoremap U b<BS>U
snoremap \ b<BS>\
snoremap ^ b<BS>^
snoremap ` b<BS>`
nmap cs <Plug>Csurround
nmap ds <Plug>Dsurround
nmap gx <Plug>NetrwBrowseX
xmap gS <Plug>VgSurround
xmap s <Plug>Vsurround
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
snoremap <Left> bi
snoremap <Right> a
snoremap <BS> b<BS>
snoremap <silent> <S-Tab> i<Right>=BackwardsSnippet()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
map <S-Insert> <MiddleMouse>
imap S <Plug>ISurround
imap s <Plug>Isurround
imap <expr> 	 pumvisible() ? "" : "	"
inoremap <NL> =TriggerSnippet()
inoremap <silent> 	 =ShowAvailableSnips()
imap  <Plug>Isurround
imap  
inoremap # #
map ¿ :call RopeLuckyAssist()
map ¯ :call RopeCodeAssist()
cmap W! w !sudo tee % >/dev/null
cmap w!! w !sudo tee % >/dev/null
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=2
set completeopt=menuone,longest,preview
set confirm
set noequalalways
set errorformat=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set fileformats=unix,dos,mac
set grepprg=ack-grep
set guifont=Inconsolata\ Medium\ 12
set helplang=pl
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set matchpairs=(:),{:},[:],<:>
set mouse=a
set omnifunc=pythoncomplete#Complete
set printoptions=paper:a4
set pumheight=6
set report=0
set ruler
set runtimepath=~/.vim,~/.vim/bundle/ack,~/.vim/bundle/acp,~/.vim/bundle/command-t,~/.vim/bundle/fugitive,~/.vim/bundle/git,~/.vim/bundle/gundo,~/.vim/bundle/makegreen,~/.vim/bundle/minibufexpl,~/.vim/bundle/nerdtree,~/.vim/bundle/pep8,~/.vim/bundle/pydoc,~/.vim/bundle/pyflakes,~/.vim/bundle/pytest,~/.vim/bundle/ropevim,~/.vim/bundle/snipmate,~/.vim/bundle/solarized,~/.vim/bundle/surround,~/.vim/bundle/tasklist,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim73,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/bundle/snipmate/after,~/.vim/after
set scrolloff=3
set shiftround
set shiftwidth=4
set shortmess=filnxtToOa
set showcmd
set showmatch
set smartcase
set smartindent
set smarttab
set softtabstop=4
set nostartofline
set statusline=[%l,%v\ %P%M]\ %f\ %r%h%w\ (%{&ff})\ %{fugitive#statusline()}
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set switchbuf=useopen
set tabstop=4
set termencoding=utf-8
set title
set updatetime=300
set virtualedit=block
set visualbell
set wildignore=*.o,*.obj,.git,*.pyc
set wildmenu
set window=54
" vim: set ft=vim :
