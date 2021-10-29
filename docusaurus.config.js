// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PureDarwin',
  tagline: 'PureDarwin is a community project that aims to make Darwin more usable.',
  url: 'https://www.puredarwin.org/',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'PureDarwin', // Usually your GitHub org/user name.
  projectName: 'PureDarwin', // Usually your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: "/",
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/PureDarwin/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        switchConfig: {
          darkIcon: '☾',
          lightIcon: '☀︎',
        },
      },
      navbar: {
        title: 'PureDarwin',
        logo: {
          alt: 'PureDarwin Logo',
          src: 'img/PureDarwin.png',
        },
        items: [
          {
            href: 'https://github.com/PureDarwin/',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Development',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/PureDarwin',
              },
              {
                label: 'Google Code (Archive)',
                href: 'https://code.google.com/archive/p/puredarwin/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.gg/9kz8XXRRcT',
              },
              {
                label: 'Reddit',
                href: 'https://reddit.com/r/PureDarwin',
              },
            ],
          },
          {
            title: 'Documentation',
            items: [
              {
                label: 'GitHub Wiki',
                href: 'https://github.com/PureDarwin/PureDarwin/wiki',
              },
              {
                label: 'Google Site (Archive)',
                href: 'https://sites.google.com/a/puredarwin.org/puredarwin/',
              },
            ],
          },
          {
            title: 'Social',
            items: [
              {
                label: 'Twitter',
                href: 'https://www.twitter.com/puredarwin',
              },
              {
                label: 'Facebook',
                href: 'https://www.facebook.com/groups/puredarwin/',
              },
            ]
          }
        ],
        copyright: `Copyright © ${new Date().getFullYear()} PureDarwin Developers`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
