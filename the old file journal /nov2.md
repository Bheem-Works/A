# Nov2


## Summary

- Date : it is nov2

## Highlights

- **Date : it is nov2


todolist:[
  tyai python ko ho aja chai grnai parne

]

oh yesh msg ayena note chI ayo feri dekehe feri maan tudo ma kai pani grnu skdinw k vanu mah



okay here i need to push the nvim command and in future i can grab it hope i am not missing anyothers thing's.**
- **" Initialize vim-plug
call plug#begin('~/.vim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}  " Auto-completion and LSP for JS/TS
Plug 'preservim/nerdtree'                       " Tree-style file explorer
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }  " Fuzzy finder
Plug 'junegunn/fzf.vim'                         " Vim integration for fzf
Plug 'pangloss/vim-javascript'                  " Enhanced JS syntax highlighting
Plug 'mxw/vim-jsx'                              " JSX/TSX support for React
Plug 'tpope/vim-commentary'                     " Comment code with gcc or gc
Plug 'jiangmiao/auto-pairs'                     " Auto-close brackets, quotes
Plug 'neoclide/coc-snippets'**

Tags: #journal
Date : it is nov2


todolist:[
  tyai python ko ho aja chai grnai parne

]

oh yesh msg ayena note chI ayo feri dekehe feri maan tudo ma kai pani grnu skdinw k vanu mah



okay here i need to push the nvim command and in future i can grab it hope i am not missing anyothers thing's.

" Initialize vim-plug
call plug#begin('~/.vim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}  " Auto-completion and LSP for JS/TS
Plug 'preservim/nerdtree'                       " Tree-style file explorer
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }  " Fuzzy finder
Plug 'junegunn/fzf.vim'                         " Vim integration for fzf
Plug 'pangloss/vim-javascript'                  " Enhanced JS syntax highlighting
Plug 'mxw/vim-jsx'                              " JSX/TSX support for React
Plug 'tpope/vim-commentary'                     " Comment code with gcc or gc
Plug 'jiangmiao/auto-pairs'                     " Auto-close brackets, quotes
Plug 'neoclide/coc-snippets'                    " Snippets for coc.nvim
Plug 'catppuccin/nvim', {'as': 'catppuccin'}    " Catppuccin theme
Plug 'sbdchd/neoformat'                         " Formatter with Prettier
Plug 'hrsh7th/nvim-cmp'                         " Autocompletion plugin (added from screenshot)
Plug 'hrsh7th/cmp-buffer'                       " Buffer source for cmp (added from screenshot)
Plug 'hrsh7th/cmp-nvim-lsp'                     " LSP source for cmp (added from screenshot)
Plug 'neovim/nvim-lspconfig'                    " LSP support (added from screenshot)
Plug 'williamboman/mason.nvim'                  " LSP manager (added from screenshot)
Plug 'williamboman/mason-lspconfig.nvim'        " LSP config manager (added from screenshot)
Plug 'L3MON4D3/LuaSnip'                         " Snippets engine (added from screenshot)
Plug 'rafamadriz/friendly-snippets'             " Snippet collection (added from screenshot)
call plug#end()

" Enable true color support for Catppuccin
if has('termguicolors')
  set termguicolors
endif

" Set Catppuccin Latte (light) theme
lua << EOF
require("catppuccin").setup({
    flavour = "mocha", -- Light theme
    transparent_background = false,
    term_colors = true,
})
vim.opt.background = "light" -- Force light background
EOF
colorscheme catppuccin

" Configure neoformat to use Prettier for multiple languages
let g:neoformat_enabled_javascript = ['prettier']
let g:neoformat_enabled_typescript = ['prettier']
let g:neoformat_enabled_css = ['prettier']
let g:neoformat_enabled_scss = ['prettier']
let g:neoformat_enabled_less = ['prettier']
let g:neoformat_enabled_json = ['prettier']
let g:neoformat_enabled_graphql = ['prettier']
let g:neoformat_enabled_markdown = ['prettier']
let g:neoformat_enabled_yaml = ['prettier']
let g:neoformat_enabled_html = ['prettier']
let g:neoformat_enabled_vue = ['prettier']
let g:neoformat_enabled_svelte = ['prettier']

let g:neoformat_javascript_prettier = {
      \ 'exe': 'prettier',
      \ 'args': ['--stdin-filepath', '"%:p"', '--single-quote', 'true', '--trailing-comma', 'es5', '--tab-width', '2'],
      \ 'stdin': 1,
      \ }
let g:neoformat_typescript_prettier = g:neoformat_javascript_prettier
let g:neoformat_css_prettier = g:neoformat_javascript_prettier
let g:neoformat_scss_prettier = g:neoformat_javascript_prettier
let g:neoformat_less_prettier = g:neoformat_javascript_prettier
let g:neoformat_json_prettier = g:neoformat_javascript_prettier
let g:neoformat_graphql_prettier = g:neoformat_javascript_prettier
let g:neoformat_markdown_prettier = g:neoformat_javascript_prettier
let g:neoformat_yaml_prettier = g:neoformat_javascript_prettier
let g:neoformat_html_prettier = g:neoformat_javascript_prettier
let g:neoformat_vue_prettier = g:neoformat_javascript_prettier
let g:neoformat_svelte_prettier = g:neoformat_javascript_prettier

" Automatically format on save for supported filetypes
augroup fmt
  autocmd!
  autocmd BufWritePre *.js,*.ts,*.css,*.scss,*.less,*.json,*.graphql,*.md,*.yaml,*.html,*.vue,*.svelte try | undojoin | Neoformat | catch | endtry
augroup END

" coc.nvim setup for JavaScript/TypeScript
let g:coc_global_extensions = ['coc-tsserver', 'coc-snippets']
autocmd FileType javascript,javascriptreact,typescript,typescriptreact setlocal formatoptions-=r
autocmd FileType javascript,javascriptreact,typescript,typescriptreact let b:coc_root_patterns = ['.git', 'package.json']

" LSP configuration (added from screenshot)
lua << EOF
require('mason').setup()
require('mason-lspconfig').setup()
require('lspconfig').tsserver.setup{}

local cmp = require'cmp'
cmp.setup({
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end,
  },
  mapping = cmp.mapping.preset.insert({
    ['<C-b>'] = cmp.mapping.scroll_docs(-4),
    ['<C-f>'] = cmp.mapping.scroll_docs(4),
    ['<C-Space>'] = cmp.mapping.complete(),
    ['<C-e>'] = cmp.mapping.abort(),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
  }),
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'luasnip' },
  }, {
    { name = 'buffer' },
  })
})
EOF

" Basic settings
set number
set relativenumber
set shiftwidth=2
set expandtab
set autoindent
set smartindent
set mouse=a
set ignorecase
set smartcase
set incsearch
set hlsearch
set cursorline
set splitbelow
set splitright
set guicursor=n-v-c:block,i-ci:ver25,r-cr:hor20
set formatoptions-=cro
set hidden
autocmd TermClose * if !&hidden | bd | endif

" Keybindings
nnoremap <leader>/ :nohlsearch<CR>
nnoremap <Leader>rr :qa!<CR>:nvim<CR>
nnoremap x :w<CR>:!node %<CR>
" compile and run c file
command! RunC w | split | terminal gcc % -o %:r.exe && %:r.exe
nnoremap <C-Alt-n> :RunC<CR>
nnoremap <Leader>z :RunC<CR>
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
nnoremap m :echo "Executing: " . expand('%')<CR>:luafile %<CR>
nnoremap <A-Up> :m .-2<CR>
nnoremap <A-Down> :m .+1<CR>
vnoremap <A-Up> :m '<-2<CR>gv
vnoremap <A-Down> :m '>+1<CR>gv

" NERDTree settings
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>
let g:NERDTreeQuitOnOpen = 0
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" fzf.vim keybindings
nnoremap <leader>p :Files<CR>
nnoremap <leader>g :Rg<CR>

" Tab and buffer navigation
nnoremap <leader>t :tabnew<CR>
nnoremap <leader>tn :tabnext<CR>
nnoremap <leader>tp :tabprevious<CR>
nnoremap <leader>bn :bnext<CR>
nnoremap <leader>bp :bprevious<CR>

" coc.nvim key mappings
inoremap <silent><expr> <Tab> pumvisible() ? coc#_select_confirm() : coc#expandableOrJumpable() ? "\<C-r>=coc#rpc#request('doKeymap', ['snippets-expand-jump',''])\<CR>" : CheckBackSpace() ? "\<Tab>" : coc#refresh()
inoremap <silent><expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<C-h>"
inoremap <silent><expr> <CR> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
inoremap <C-Enter> <Down><End><Enter>

function! CheckBackSpace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunctionT
