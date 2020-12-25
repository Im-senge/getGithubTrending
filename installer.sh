#!/bin/bash
whiptail --title "警告" --yesno "本代码免费并遵循GNU通用公共许可协议(GNU General Public License)\n如果您通过付费获取本代码, 请立即申请退款，并举报。\n举报邮箱：a1356872768@gmail.com" --yes-button "同意" --no-button "拒绝" 15 70
if [ $? -ne 0 ]; then
  echo -e "您未确认安装"
  exit 1
else
  wget https://raw.githubusercontent.com/Im-senge/getGithubTrending/main/GithubCrawler.py ~/.GuthubCrawler.py
  if [ $? -ne 0 ]; then
    echo "安装失败，请检查网络连接！"
    exit 1
  fi
  OPTION=$(whiptail --title "写入数据" --menu "您使用的是什么终端？" 15 60 4 \
    "1" "bash" \
    "2" "zsh" \
    "3" "fish" \
    "4" "其他"   3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
      case "$OPTION" in
      1)
        echo "alias gettrending=\"python ~/.GithubCrawler.py\"" >> ~/.bashrc;;
      2)
        echo "alias gettrending=\"python ~/.GithubCrawler.py\"" >> ~/.zshrc;;
      3)
        echo "alias gettrending=\"python ~/.GithubCrawler.py\"" >> ~/.fishrc;;
      4)
        echo "请手动执行python ~/.GithubCrawler.py来执行脚本"
      esac
    fi
    echo "请先安装BeautifulSoup插件，否则脚本无法运行"
fi
